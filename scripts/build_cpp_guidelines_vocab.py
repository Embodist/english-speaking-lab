#!/usr/bin/env python3
"""Build a vocabulary deck from the C++ Core Guidelines.

Source: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines

The page is parsed as prose only (all <pre>/<code> blocks are dropped), so the
deck contains English vocabulary rather than C++ identifiers.  General words
are deduplicated against the existing 10k paper deck; C++ terms are curated
separately with technical senses.

Outputs (16_cpp-core-guidelines/):
  master.csv
  dictionary-general.md
  domain-terms.md
  anki-01.csv
  cpp-core-guidelines.apkg
"""
import collections
import csv
import html
import re
import sqlite3
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import genanki
import lemminflect
from wordfreq import zipf_frequency

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT.parent / "data"
CACHE = DATA_DIR / "cpp-core-guidelines.html"
ECDICT = DATA_DIR / "ecdict.sqlite"
OUT = ROOT / "16_cpp-core-guidelines"
URL = "https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines"

DECK_ID = 1436534930
MODEL_ID = 1436534931
DECK_NAME = "C++ Core Guidelines"
MODEL_NAME = "Vocab (C++ Core Guidelines)"

GENERAL_ZIPF_MIN = 3.0
GENERAL_ZIPF_MAX = 4.6
GENERAL_MIN_DF = 2
GENERAL_LIMIT = 700

STOP = set("""
a an the and or but if while of to in on at by for from with without as is are was were be been being
this that these those it its their our we you they he she i not no can could may might should would will
shall do does did done have has had also than then there here which who whom whose what when where why how
all any both each few more most other some such only own same so too very just about into over under again
further once during before after above below up down out off between through because paper papers work works
study studies show shows shown using used use uses based propose proposes proposed present presents presented
provide provides provided result results method methods approach approaches model models task tasks data dataset
datasets training train trained learn learning learned performance figure figures table tables section sections
appendix arxiv preprint et al ieee conference proceedings pages page doi url http https github com www email
authors author corresponding supplementary supplement algorithm algorithms equation equations eq fig tab
reference references introduction related abstract keywords keyword university institute department school inc
ltd copyright license permission cpp cplusplus iso wg21 stroustrup bjarne sutter herb editor editors jun
copy copying modification creation derivative works project mit style contributing contributor accompanying
file details plan modify extend document understanding improves language available libraries improve commenting
please note notes example examples good bad right wrong rule rules guideline guidelines see user users
don doesn didn isn aren wasn weren hasn haven hadn won wouldn couldn shouldn mustn needn let
""".split())

BOILER = set("""
cpp cplusplus iso gsl stroustrup sutter bjarne herb github www http https email
enum struct bool coro dtor ctor ptr std tmp var expr stmt decl typedef typename decltype
stdlib memcpy memset setjmp longjmp vtable zstring czstring varargs vararg isocpp nullptr
""".split())

# Generic words that survive the frequency filter but add little for this document.
GENERAL_BLOCK = set("""
alway acros proces serie basi hier chao gues vely coro util memcpy memset setjmp longjmp
overrider clash sparingly keynote litter snag caricature widget heartbeat longish reseat
onward naked factory dangle destruct detached unmanageable
""".split())

# Gerunds that should not be reduced to their verb lemma.
KEEP_ING = set("""
programming testing computing binding casting forwarding mapping locking hashing encoding decoding threading
profiling streaming parsing rendering scheduling caching linking loading packing logging benchmarking
initialization deallocation allocation abstraction encapsulation polymorphism metaprogramming vectorization
synchronization contention starvation reasoning
""".split())

ALIASES = {
    "programme": "program",
    "programmes": "program",
    "behaviour": "behavior",
    "behaviours": "behavior",
    "initialisation": "initialization",
    "serialisation": "serialization",
    "deserialise": "deserialize",
    "deserialisation": "deserialization",
    "optimise": "optimize",
    "optimised": "optimize",
    "optimisation": "optimization",
    "organise": "organize",
    "utilise": "utilize",
    "analyse": "analyze",
    "analysed": "analyze",
    "modelling": "modeling",
    "labelled": "labeled",
}

# Inflected forms that should be handled by a curated domain term.
DOMAIN_FORMS = {
    "refactoring": "refactor", "refactored": "refactor", "refactors": "refactor",
    "deallocated": "deallocate", "deallocates": "deallocate", "deallocating": "deallocate",
    "dereferencing": "dereference", "dereferenced": "dereference", "dereferences": "dereference",
    "initializers": "initializer", "enumerators": "enumerator", "callees": "callee",
    "callers": "caller", "allocators": "allocator", "polymorphically": "polymorphic",
    "downcasting": "downcast", "downcasted": "downcast",
    "overridden": "override", "overriding": "override",
    "asserted": "assert", "asserting": "assert",
    "specializations": "specialization", "specialised": "specialization",
    "compilables": "compilable", "templatized": "templatize",
    "implementers": "implementer", "handlers": "handler",
    "setters": "setter", "getters": "getter", "casting": "cast",
}

# Curated C++ / programming terms: (POS, Chinese, English definition).
# Only terms that actually occur in the document are emitted.
DOMAIN_TERMS = {
    "abstract class": ("n.", "抽象类", "A class that cannot be instantiated directly; used to define an interface."),
    "abstraction": ("n.", "抽象", "Hiding implementation details behind a simpler, stable interface."),
    "access": ("n./v.", "访问", "The ability to read or modify an object or resource."),
    "aggregate": ("n.", "聚合体", "A class or array type initialized directly from a brace-enclosed list."),
    "alias": ("n.", "别名", "An alternative name for a type or entity."),
    "allocation": ("n.", "分配", "Reserving memory for an object."),
    "deallocation": ("n.", "释放", "Releasing memory that was previously allocated."),
    "argument": ("n.", "实参", "A value passed to a function at a call site."),
    "array": ("n.", "数组", "A contiguous sequence of elements of the same type."),
    "assertion": ("n.", "断言", "A statement that a condition must be true."),
    "assignment": ("n.", "赋值", "Replacing the value of an object with another value."),
    "base class": ("n.", "基类", "A class from which other classes inherit."),
    "derived class": ("n.", "派生类", "A class that inherits from a base class."),
    "behavior": ("n.", "行为", "The observable actions of a program or object."),
    "bounds": ("n.", "边界", "The limits of a valid range, especially array indices."),
    "cast": ("n./v.", "类型转换", "An explicit conversion from one type to another."),
    "class hierarchy": ("n.", "类层次结构", "A tree of classes connected by inheritance."),
    "compiler": ("n.", "编译器", "A tool that translates source code into machine code."),
    "compile time": ("n.", "编译期", "The phase when source code is translated."),
    "run time": ("n.", "运行期", "The phase when a program executes."),
    "concurrency": ("n.", "并发", "Executing tasks that make progress during overlapping periods."),
    "parallelism": ("n.", "并行", "Executing tasks at the same time on multiple processors."),
    "concept": ("n.", "概念", "A named set of requirements on template parameters (C++20)."),
    "const": ("n.", "常量限定", "A qualifier promising that a value will not be modified."),
    "constexpr": ("n.", "常量表达式", "A function or variable that can be evaluated at compile time."),
    "consteval": ("n.", "立即求值函数", "A function that must be evaluated at compile time."),
    "constinit": ("n.", "常量初始化", "A variable that must be statically initialized."),
    "constructor": ("n.", "构造函数", "A special member function that initializes an object."),
    "destructor": ("n.", "析构函数", "A special member function that releases an object's resources."),
    "container": ("n.", "容器", "A type that stores and manages a collection of elements."),
    "copy semantics": ("n.", "拷贝语义", "Creating a new object with the same value as an existing one."),
    "coroutine": ("n.", "协程", "A function that can suspend and later resume execution."),
    "dangling pointer": ("n.", "悬空指针", "A pointer to an object whose lifetime has ended."),
    "dangling reference": ("n.", "悬空引用", "A reference to an object whose lifetime has ended."),
    "data race": ("n.", "数据竞争", "Conflicting unsynchronized accesses to the same memory."),
    "deadlock": ("n.", "死锁", "A state where threads wait forever for each other."),
    "declaration": ("n.", "声明", "Introducing a name and its type to the compiler."),
    "definition": ("n.", "定义", "Providing the implementation or storage for an entity."),
    "dereference": ("v.", "解引用", "Accessing the object that a pointer refers to."),
    "encapsulation": ("n.", "封装", "Hiding internal details behind a stable interface."),
    "enumeration": ("n.", "枚举", "A type whose values are named constants."),
    "exception": ("n.", "异常", "An object used to signal and propagate errors."),
    "exception safety": ("n.", "异常安全", "A guarantee about object state when an exception is thrown."),
    "explicit": ("adj.", "显式的", "A constructor qualifier that prevents implicit conversions."),
    "expression": ("n.", "表达式", "A sequence of operators and operands that produces a value."),
    "function object": ("n.", "函数对象", "An object that can be called like a function."),
    "generic programming": ("n.", "泛型编程", "Writing code that works with many types."),
    "global variable": ("n.", "全局变量", "A variable visible and accessible across a whole program."),
    "handle": ("n.", "句柄", "An object that owns and manages a resource."),
    "header": ("n.", "头文件", "A file included to declare interfaces and types."),
    "immutability": ("n.", "不可变性", "The property of not changing after creation."),
    "implementation": ("n.", "实现", "The concrete code behind an interface."),
    "implementation-defined": ("adj.", "实现定义的", "Behavior the C++ standard leaves to each implementation."),
    "initialization": ("n.", "初始化", "Giving an object its initial value."),
    "inline": ("adj./v.", "内联", "A request to expand a function at its call site."),
    "interface": ("n.", "接口", "The operations a type exposes to its users."),
    "invariant": ("n.", "不变量", "A condition that must always hold during execution."),
    "iterator": ("n.", "迭代器", "An object that traverses the elements of a container."),
    "lambda": ("n.", "匿名函数", "An unnamed function object defined inline."),
    "leak": ("n./v.", "泄漏", "Failing to release a resource such as memory."),
    "lifetime": ("n.", "生命周期", "The period during which an object exists."),
    "lock-free": ("adj.", "无锁的", "An algorithm that guarantees progress without mutual exclusion locks."),
    "macro": ("n.", "宏", "A preprocessor text substitution."),
    "member": ("n.", "成员", "A data field or function belonging to a class."),
    "memory leak": ("n.", "内存泄漏", "Allocated memory that is never released."),
    "metaprogramming": ("n.", "元编程", "Writing code that generates or manipulates code."),
    "move semantics": ("n.", "移动语义", "Transferring ownership of resources instead of copying them."),
    "mutable": ("adj.", "可变的", "Allowed to change after creation."),
    "namespace": ("n.", "命名空间", "A scope that groups related names."),
    "noexcept": ("n.", "不抛出异常", "A specifier promising that a function will not throw."),
    "null pointer": ("n.", "空指针", "A pointer that points to no object."),
    "object": ("n.", "对象", "An entity with a type and a lifetime."),
    "operator": ("n.", "运算符", "A symbol that performs an operation."),
    "overload": ("v./n.", "重载", "Providing multiple functions with the same name and different parameters."),
    "override": ("v./n.", "重写", "Replacing a virtual function in a derived class."),
    "ownership": ("n.", "所有权", "Responsibility for releasing a resource."),
    "parameter": ("n.", "形参", "A named variable declared in a function signature."),
    "performance": ("n.", "性能", "How efficiently a program uses time and resources."),
    "pointer": ("n.", "指针", "An object that stores the address of another object."),
    "polymorphism": ("n.", "多态", "Treating objects of different types through a common interface."),
    "precondition": ("n.", "前置条件", "A condition that must hold before a function is called."),
    "postcondition": ("n.", "后置条件", "A condition that must hold after a function returns."),
    "profile": ("n.", "规范集", "A set of rules that enforce a property such as type safety."),
    "pure function": ("n.", "纯函数", "A function whose result depends only on its arguments and has no side effects."),
    "RAII": ("n.", "资源获取即初始化", "Tying resource lifetime to object lifetime."),
    "raw pointer": ("n.", "裸指针", "A pointer without ownership semantics."),
    "reference": ("n.", "引用", "An alias to an existing object."),
    "resource": ("n.", "资源", "Something that must be acquired and released, such as memory, a file, or a lock."),
    "return value": ("n.", "返回值", "The value a function yields to its caller."),
    "scope": ("n.", "作用域", "The region of code where a name is visible."),
    "semantics": ("n.", "语义", "The meaning of code, as opposed to its syntax."),
    "shared_ptr": ("n.", "共享指针", "A smart pointer with shared ownership."),
    "unique_ptr": ("n.", "独占指针", "A smart pointer with exclusive ownership."),
    "side effect": ("n.", "副作用", "An observable change beyond returning a value."),
    "smart pointer": ("n.", "智能指针", "An object that owns a resource and releases it automatically."),
    "source file": ("n.", "源文件", "A file containing implementation code."),
    "statement": ("n.", "语句", "A unit of execution in a program."),
    "static": ("adj.", "静态的", "Having a lifetime or scope fixed at compile time."),
    "string": ("n.", "字符串", "A sequence of characters."),
    "template": ("n.", "模板", "A parameterized type or function."),
    "thread": ("n.", "线程", "A single flow of execution within a process."),
    "thread safety": ("n.", "线程安全", "Correct behavior when code runs concurrently."),
    "translation unit": ("n.", "翻译单元", "A source file after preprocessing, compiled as one unit."),
    "type safety": ("n.", "类型安全", "Ensuring operations are valid for the types they are applied to."),
    "undefined behavior": ("n.", "未定义行为", "Behavior for which the C++ standard imposes no requirements."),
    "unspecified behavior": ("n.", "未指定行为", "Behavior chosen from a set of allowed alternatives."),
    "value semantics": ("n.", "值语义", "Copying a value produces an independent object."),
    "variable": ("n.", "变量", "A named object whose value can change."),
    "variadic template": ("n.", "可变参数模板", "A template that accepts an arbitrary number of arguments."),
    "virtual": ("adj.", "虚的", "Allowing a derived class to override a function."),
    "zero-overhead": ("adj.", "零开销", "An abstraction that costs no more than hand-written code."),
    "ABI": ("n.", "应用二进制接口", "The binary-level calling and layout contract between compiled code."),
    "API": ("n.", "应用编程接口", "The interface through which code calls a library."),
    "GSL": ("n.", "指南支持库", "The Guidelines Support Library."),
    "ISO": ("n.", "国际标准化组织", "The body that standardizes C++."),
    "NVI": ("n.", "非虚接口", "Non-Virtual Interface idiom."),
    "pImpl": ("n.", "实现指针惯用法", "Pointer-to-implementation idiom for separating interface and implementation."),
    "ABI stability": ("n.", "二进制兼容性", "Keeping binary compatibility across library versions."),
    "bounds safety": ("n.", "边界安全", "Ensuring accesses stay within valid ranges."),
    "lifetime safety": ("n.", "生命周期安全", "Ensuring no use after an object's lifetime ends."),
    "resource management": ("n.", "资源管理", "Acquiring and releasing resources correctly."),
    "ownership transfer": ("n.", "所有权转移", "Moving responsibility for a resource to another owner."),
    "copy elision": ("n.", "拷贝消除", "Avoiding unnecessary copy or move operations."),
    "pass by value": ("phr.", "按值传递", "Passing a copy of an argument to a function."),
    "pass by reference": ("phr.", "按引用传递", "Passing a reference to an argument to a function."),
    "constant expression": ("n.", "常量表达式", "An expression evaluable at compile time."),
    "template parameter": ("n.", "模板参数", "A type or value parameter of a template."),
    "template argument": ("n.", "模板实参", "The actual type or value supplied to a template."),
    "const correctness": ("n.", "const 正确性", "Using const to express and enforce immutability."),
    "type deduction": ("n.", "类型推导", "Letting the compiler infer a type from context."),
    "perfect forwarding": ("n.", "完美转发", "Forwarding arguments while preserving their value category."),
    "move constructor": ("n.", "移动构造函数", "A constructor that takes an rvalue reference and steals resources."),
    "copy constructor": ("n.", "拷贝构造函数", "A constructor that creates an object from another object of the same type."),
    "copy assignment": ("n.", "拷贝赋值", "Assigning one object's value to another object."),
    "move assignment": ("n.", "移动赋值", "Transferring resources from one object to another by assignment."),
    "default constructor": ("n.", "默认构造函数", "A constructor callable with no arguments."),
    "user-defined type": ("n.", "用户定义类型", "A type defined by the programmer, such as a class or enum."),
    "value type": ("n.", "值类型", "A type whose values behave like independent copies."),
    "concrete type": ("n.", "具体类型", "A type with a complete, directly usable definition."),
    "resource leak": ("n.", "资源泄漏", "A resource that is acquired but never released."),
    "overflow": ("n.", "溢出", "A value exceeding the range its type can represent."),
    "underflow": ("n.", "下溢", "A value falling below the range its type can represent."),
    "buffer overflow": ("n.", "缓冲区溢出", "Writing past the bounds of a buffer."),
    "diagnostic": ("n.", "诊断信息", "A message from a tool that reports a problem."),
    "enforcement": ("n.", "强制实施", "Automatic checking that a rule is followed."),
    "violation": ("n.", "违规", "Breaking a rule or contract."),
    "idiom": ("n.", "惯用法", "A conventional way of expressing something in a language."),
    "legacy code": ("n.", "遗留代码", "Old code that must keep working."),
    "refactor": ("v.", "重构", "Improving code structure without changing behavior."),
    "robust": ("adj.", "健壮的", "Able to handle unexpected inputs without failing."),
    "portable": ("adj.", "可移植的", "Working across different platforms and compilers."),
    "scalable": ("adj.", "可扩展的", "Continuing to work well as size or load grows."),
    "trade-off": ("n.", "权衡", "A balance between competing goals."),
    "overhead": ("n.", "开销", "Extra cost in time, memory, or complexity."),
    "bottleneck": ("n.", "瓶颈", "The part that limits overall performance."),
    "cache": ("n./v.", "缓存", "Fast storage for frequently used data."),
    "vectorization": ("n.", "向量化", "Using SIMD instructions to process multiple values at once."),
    "message passing": ("n.", "消息传递", "Communication between threads by sending messages."),
    "synchronization": ("n.", "同步", "Coordinating concurrent accesses to shared state."),
    "atomic": ("adj.", "原子的", "Indivisible with respect to concurrent operations."),
    "mutex": ("n.", "互斥量", "A lock that allows only one thread into a critical section."),
    "semaphore": ("n.", "信号量", "A counter used to control access to a resource."),
    "contention": ("n.", "争用", "Competition among threads for a shared resource."),
    "starvation": ("n.", "饥饿", "A thread being indefinitely denied a resource."),
    "livelock": ("n.", "活锁", "Threads keep responding to each other without making progress."),
    "priority inversion": ("n.", "优先级反转", "A high-priority task waiting on a low-priority one."),
    "race condition": ("n.", "竞态条件", "A result that depends on the timing of concurrent operations."),
    "thread pool": ("n.", "线程池", "A set of worker threads that execute queued tasks."),
    "exception handling": ("n.", "异常处理", "Throwing, catching, and cleaning up after exceptions."),
    "stack unwinding": ("n.", "栈展开", "Destroying local objects while propagating an exception."),
    "error code": ("n.", "错误码", "A value returned to indicate success or failure."),
    "contract": ("n.", "契约", "A documented precondition, postcondition, or invariant."),
    "static analysis": ("n.", "静态分析", "Finding problems by analyzing code without running it."),
    "code review": ("n.", "代码审查", "Examining code for defects and design issues."),
    "unit test": ("n.", "单元测试", "A test of one small piece of code in isolation."),
    "regression": ("n.", "回归", "A defect that breaks previously working behavior."),
    "debug": ("v.", "调试", "Finding and fixing defects."),
    "profiling": ("n.", "性能分析", "Measuring where a program spends time or memory."),
    "benchmark": ("n./v.", "基准测试", "A repeatable measurement used to compare performance."),
    "optimization": ("n.", "优化", "Improving efficiency without changing behavior."),
    "inline function": ("n.", "内联函数", "A function defined in a header and expanded at call sites."),
    "const reference": ("n.", "常量引用", "A reference through which the object cannot be modified."),
    "lvalue": ("n.", "左值", "An expression that refers to an object with a stable identity."),
    "rvalue": ("n.", "右值", "A temporary value that does not have a stable identity."),
    "rvalue reference": ("n.", "右值引用", "A reference that can bind to temporaries and enable move semantics."),
    "forwarding reference": ("n.", "转发引用", "A T&& parameter that preserves the argument's value category."),
    "trivial type": ("n.", "平凡类型", "A type with trivial default construction, copy, and destruction."),
    "standard library": ("n.", "标准库", "The library defined by the C++ standard."),
    "STL": ("n.", "标准模板库", "The Standard Template Library, the containers and algorithms part of the standard library."),
    "header-only": ("adj.", "仅头文件", "A library provided entirely in header files."),
    "linker": ("n.", "链接器", "A tool that combines object files into an executable."),
    "object code": ("n.", "目标代码", "Compiler output before linking."),
    "machine code": ("n.", "机器码", "Instructions executed directly by the CPU."),
    "runtime": ("n.", "运行时", "The support code and environment in which a program executes."),
    "dynamic allocation": ("n.", "动态分配", "Allocating memory at run time."),
    "stack": ("n.", "栈", "Memory for local objects with automatic lifetime."),
    "heap": ("n.", "堆", "Memory for dynamically allocated objects."),
    "garbage collection": ("n.", "垃圾回收", "Automatically reclaiming unreachable memory."),
    "callee": ("n.", "被调用者", "The function that is called at a call site."),
    "caller": ("n.", "调用者", "The code that calls a function."),
    "enumerator": ("n.", "枚举成员", "A named value of an enumeration type."),
    "initializer": ("n.", "初始化器", "A value or expression used to initialize an object."),
    "copyable": ("adj.", "可拷贝的", "A type whose objects can be copied."),
    "movable": ("adj.", "可移动的", "A type whose resources can be transferred by move."),
    "variadic": ("adj.", "可变参数的", "Accepting an arbitrary number of arguments."),
    "callable": ("adj.", "可调用的", "A type whose objects can be invoked like a function."),
    "writable": ("adj.", "可写的", "A type or object whose value can be modified."),
    "allocator": ("n.", "分配器", "An object that manages memory allocation for containers."),
    "deallocate": ("v.", "释放", "To release memory that was previously allocated."),
    "covariant": ("adj.", "协变的", "Preserving the inheritance relationship of a type parameter."),
    "refactor": ("v.", "重构", "Improving code structure without changing behavior."),
    "async": ("adj.", "异步的", "Not waiting for an operation to finish before continuing."),
    "wrapper": ("n.", "包装器", "A type or function that adapts another interface."),
    "callback": ("n.", "回调", "A function passed to be called later by another component."),
    "forwarding": ("n.", "转发", "Passing an argument on while preserving its value category."),
    "indirection": ("n.", "间接访问", "Extra access through a pointer, reference, or handle."),
    "specialization": ("n.", "特化", "A version of a template for specific arguments."),
    "type erasure": ("n.", "类型擦除", "Hiding concrete types behind a uniform interface."),
    "downcast": ("n./v.", "向下转型", "Converting a base-class pointer or reference to a derived type."),
    "unary": ("adj.", "一元的", "Taking one operand or argument."),
    "assert": ("v.", "断言", "To state that a condition must be true."),
    "fallthrough": ("n.", "贯穿", "Continuing into the next case of a switch statement."),
    "declarator": ("n.", "声明符", "The part of a declaration that gives a name and type."),
    "nullptr": ("n.", "空指针字面量", "The null pointer literal introduced in C++11."),
    "vtable": ("n.", "虚函数表", "The table used to dispatch virtual function calls."),
    "bool": ("n.", "布尔类型", "The built-in type with values true and false."),
    "struct": ("n.", "结构体", "A class whose members are public by default."),
    "chrono": ("n.", "时间库", "The standard library facilities for time and durations."),
    "freestanding": ("adj.", "独立的", "An implementation that need not provide the full hosted library."),
    "elision": ("n.", "省略", "Avoiding an unnecessary copy or move operation."),
    "subexpression": ("n.", "子表达式", "An expression nested inside a larger expression."),
    "deleter": ("n.", "删除器", "A callable that releases a resource owned by a smart pointer."),
    "recompile": ("v.", "重新编译", "To compile code again after a change."),
    "recompilation": ("n.", "重新编译", "The act of compiling code again."),
    "verbosity": ("n.", "冗长", "The amount of unnecessary code or text."),
    "intrusive": ("adj.", "侵入式的", "A container design that requires elements to embed bookkeeping data."),
    "invalidation": ("n.", "失效", "Making a pointer, reference, or iterator no longer usable."),
    "rollback": ("n.", "回滚", "Restoring a previous state after a failure."),
    "naked pointer": ("n.", "裸指针", "A raw pointer without ownership semantics."),
    "factory function": ("n.", "工厂函数", "A function that creates and returns an object."),
    "detached": ("adj.", "分离的", "A thread that runs independently of its creator."),
    "checkable": ("adj.", "可检查的", "Able to be verified by a tool or test."),
    "setter": ("n.", "修改器", "A member function that sets a value."),
    "getter": ("n.", "访问器", "A member function that returns a value."),
    "polymorphic": ("adj.", "多态的", "Supporting operations whose behavior depends on the dynamic type."),
    "cyclic": ("adj.", "循环的", "Depending on itself, directly or indirectly."),
    "negation": ("n.", "否定", "A requirement that a condition must not hold."),
    "implementer": ("n.", "实现者", "A person or component that provides an implementation."),
    "handler": ("n.", "处理器", "Code that responds to an event or error."),
    "TMP": ("n.", "模板元编程", "Template metaprogramming: computing with templates at compile time."),
    "error-prone": ("adj.", "易出错的", "Likely to cause mistakes."),
    "type-safe": ("adj.", "类型安全的", "Guaranteeing that operations are valid for their types."),
    "thread-safe": ("adj.", "线程安全的", "Correct when called from multiple threads."),
    "exception-safe": ("adj.", "异常安全的", "Leaving objects in a valid state when an exception is thrown."),
    "non-local": ("adj.", "非局部的", "Not limited to the current scope or function."),
    "non-virtual": ("adj.", "非虚的", "Not dispatched through the virtual function mechanism."),
    "programming": ("n.", "编程", "Writing code; designing and implementing programs."),
    "singleton": ("n.", "单例", "A design that restricts a class to one instance."),
    "analyzer": ("n.", "分析器", "A tool that inspects code or data."),
    "cleanup": ("n.", "清理", "Releasing resources or restoring state."),
    "swap": ("n./v.", "交换", "Exchanging the values of two objects."),
    "locking": ("n.", "加锁", "Using a lock to protect shared data."),
    "unnamed": ("adj.", "未命名的", "Without a name."),
    "unsigned": ("adj.", "无符号的", "A type that represents only non-negative values."),
    "reuse": ("n./v.", "复用", "Using code or resources again."),
    "destruction": ("n.", "销毁", "Releasing an object's resources at the end of its lifetime."),
    "suspension": ("n.", "挂起", "Pausing a coroutine or thread until it is resumed."),
    "linking": ("n.", "链接", "Combining object files and libraries into a program."),
    "unwind": ("v.", "展开", "Leaving nested scopes, especially while propagating an exception."),
    "directive": ("n.", "指示/指令", "An instruction to the compiler or preprocessor."),
    "shared ownership": ("n.", "共享所有权", "Multiple owners share responsibility for a resource."),
    "exclusive ownership": ("n.", "独占所有权", "Exactly one owner is responsible for a resource."),
    "shared pointer": ("n.", "共享指针", "A smart pointer that shares ownership of a resource."),
    "trivial": ("adj.", "平凡的", "A type or operation with no user-defined behavior."),
}

CSS = """
.card {
  font-family: -apple-system, "Segoe UI", "Noto Sans CJK SC", sans-serif;
  font-size: 20px; line-height: 1.5; text-align: center;
  color: #1f2328; background: #ffffff;
}
.word { font-size: 34px; font-weight: 600; margin-bottom: 6px; }
.phonetic { color: #57606a; font-size: 18px; margin-bottom: 16px; }
.pos { color: #57606a; font-size: 18px; margin-bottom: 16px; font-style: italic; }
.meaning { font-size: 24px; font-weight: 600; margin: 12px 0; }
.def { font-size: 16px; color: #57606a; text-align: left; margin: 10px 0; }
.sentence {
  font-size: 16px; font-style: italic; text-align: left;
  border-left: 3px solid #d0d7de; padding-left: 10px; margin: 12px 0;
}
.meta { font-size: 12px; color: #8c959f; }
hr#answer { border: 0; border-top: 1px solid #d0d7de; margin: 14px 0; }
.nightMode .card { color: #e6edf3; background: #0d1117; }
.nightMode .phonetic, .nightMode .def { color: #8b949e; }
.nightMode .sentence { border-left-color: #30363d; }
.nightMode .meta { color: #6e7681; }
.nightMode hr#answer { border-top-color: #30363d; }
"""

MODEL = genanki.Model(
    MODEL_ID,
    MODEL_NAME,
    fields=[{"name": n} for n in [
        "Word", "Phonetic", "POS", "Chinese", "Definition", "Sentence", "Section",
    ]],
    templates=[
        {
            "name": "Word to Meaning",
            "qfmt": (
                '<div class="word">{{Word}}</div>'
                '{{#Phonetic}}<div class="phonetic">/{{Phonetic}}/</div>{{/Phonetic}}'
                '{{#POS}}<div class="pos">{{POS}}</div>{{/POS}}'
            ),
            "afmt": (
                "{{FrontSide}}"
                '<hr id="answer">'
                '<div class="meaning">{{Chinese}}</div>'
                '{{#Definition}}<div class="def">{{Definition}}</div>{{/Definition}}'
                '{{#Sentence}}<div class="sentence">{{Sentence}}</div>{{/Sentence}}'
                '{{#Section}}<div class="meta">{{Section}}</div>{{/Section}}'
            ),
        }
    ],
    css=CSS,
)

TOKEN = re.compile(r"[A-Za-z][A-Za-z'\-]{2,}")
CLEAN_TRANS = re.compile(r"\[[^\]]{1,8}\]")
SENT_SPLIT = re.compile(r"(?<!e\.g\.)(?<!i\.e\.)(?<!etc\.)(?<=[.!?])\s+(?=[A-Z(\"'0-9])")
FRAGMENTS = {"tional", "ments", "tions", "sion", "ically", "ization", "isation", "ness", "ingly"}


SECTION_CODE = re.compile(
    r"^[A-Za-z]+(?:\.[A-Za-z0-9]+)+:\s*|^[A-Za-z]+\.\d+:\s*"
)


def strip_section_code(text):
    return SECTION_CODE.sub("", text, count=1).strip()


class DocExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.started = False
        self.stopped = False
        self.pre = 0
        self.code = 0
        self.block_buf = None
        self.heading_buf = None
        self.block_tag = ""
        self.block_is_toc = False
        self.pending_id = ""
        self.section = ""
        self.blocks = []  # (plain text, section, is_heading)

    def handle_starttag(self, tag, attrs):
        if self.stopped:
            return
        if tag in ("script", "style", "pre"):
            self.pre += 1
            return
        if tag == "code":
            self.code += 1
            return
        if tag in ("h1", "h2", "h3"):
            self._flush_block()
            self.heading_buf = []
            self.pending_id = dict(attrs).get("id", "")
            return
        if tag in ("p", "li", "dt", "dd"):
            self._flush_block()
            self.block_buf = []
            self.block_tag = tag
            self.block_is_toc = False
            return
        if tag == "a" and self.block_tag == "li":
            href = dict(attrs).get("href", "")
            if href.startswith("#"):
                self.block_is_toc = True

    def handle_endtag(self, tag):
        if self.stopped:
            return
        if tag in ("script", "style", "pre"):
            if self.pre:
                self.pre -= 1
            return
        if tag == "code":
            if self.code:
                self.code -= 1
                if self.code == 0 and self.pre == 0 and self.started and self.block_buf is not None:
                    self.block_buf.append(" … ")
            return
        if tag in ("h1", "h2", "h3") and self.heading_buf is not None:
            original = self._clean("".join(self.heading_buf))
            self.heading_buf = None
            if not self.started and (
                "core guidelines" in original.lower() or self.pending_id == "c-core-guidelines"
            ):
                self.started = True
            if self.started:
                if original.lower().startswith("bibliography"):
                    self.stopped = True
                    return
                self.section = original
                plain = strip_section_code(original)
                if plain:
                    self.blocks.append((plain, original, True))
        elif tag in ("p", "li", "dt", "dd") and self.block_buf is not None:
            self._flush_block()

    def handle_data(self, data):
        if self.stopped or self.pre or self.code:
            return
        if self.heading_buf is not None:
            self.heading_buf.append(data)
        elif self.block_buf is not None and self.started:
            self.block_buf.append(data)

    def _flush_block(self):
        if self.block_buf is not None:
            if self.started and not self.block_is_toc:
                text = self._clean("".join(self.block_buf))
                text = re.sub(r"\s*…(\s*…)+\s*", " … ", text)
                if 15 <= len(text) <= 2000:
                    self.blocks.append((text, self.section, False))
            self.block_buf = None
            self.block_tag = ""
            self.block_is_toc = False

    @staticmethod
    def _clean(text):
        text = text.replace(" ", " ")
        text = re.sub(r"\s+", " ", text)
        return text.strip()


def fetch_html():
    if CACHE.exists() and CACHE.stat().st_size > 500_000:
        return CACHE.read_text(encoding="utf-8")
    import requests

    resp = requests.get(URL, timeout=90)
    resp.raise_for_status()
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(resp.text, encoding="utf-8")
    return resp.text


def normalize_text(text):
    return (text.replace("’", "'").replace("‘", "'")
            .replace("“", '"').replace("”", '"'))


def sentence_split(text):
    text = normalize_text(text)
    return [p.strip() for p in SENT_SPLIT.split(text) if p.strip()]


def load_existing_words():
    path = ROOT / "14_llm-papers" / "vocabulary-10k" / "master.csv"
    words = set()
    if not path.exists():
        return words
    with path.open(encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            word = (row.get("word") or "").strip().lower()
            if word:
                words.add(word)
    return words


def entry_lookup(con, word):
    return con.execute(
        "select word, phonetic, definition, translation, pos, tag, bnc, frq "
        "from entries where word=? collate nocase",
        (word,),
    ).fetchone()


def lemma_of(word, con, cache):
    if word.isupper() and 2 <= len(word) <= 6:
        return word
    if word in KEEP_ING:
        return word
    best = None
    for pos in ("NOUN", "VERB", "ADJ", "ADV"):
        for lem in lemminflect.getAllLemmas(word).get(pos, ()):
            z = zipf_frequency(lem, "en")
            if best is None or z > best[1]:
                best = (lem, z)
    lem = best[0] if best else word
    if lem in ALIASES:
        lem = ALIASES[lem]
    # Guard against lemmatizer artifacts such as always -> alway.
    if lem != word and zipf_frequency(lem, "en") < zipf_frequency(word, "en") - 0.8:
        lem = word
    # Technical plurals such as "destructors" are unknown to lemminflect.
    if lem == word and len(word) > 4 and word.endswith("s"):
        base = word[:-1]
        if base in DOMAIN_TERMS or base in cache or entry_lookup(con, base):
            lem = base
    return lem


def clean_translation(text):
    if not text:
        return ""
    text = text.replace("\\n", "\n")
    lines = []
    for line in text.splitlines():
        line = CLEAN_TRANS.sub("", line).strip(" ;，,")
        if line and line not in lines:
            lines.append(line)
    return "；".join(lines[:2])[:160]


def clean_definition(text):
    if not text:
        return ""
    text = text.replace("\\n", " ")
    text = CLEAN_TRANS.sub("", text)
    return re.sub(r"\s+", " ", text).strip()[:280]


def pos_from_translation(text):
    m = re.match(r"\s*((?:n|v|vt|vi|a|ad|adv|prep|conj|pron|num)\.)", text or "")
    return m.group(1) if m else ""


def ipa_cache_factory():
    cache = {}

    def ipa(word):
        if word in cache:
            return cache[word]
        try:
            out = subprocess.run(
                ["espeak-ng", "--ipa", "-q", word],
                capture_output=True, text=True, timeout=5,
            ).stdout.strip().splitlines()
            value = out[0].strip() if out else ""
        except Exception:
            value = ""
        cache[word] = value
        return value

    return ipa


def _word_forms(word):
    forms = {word, word + "s"}
    if word.endswith(("s", "x", "z", "ch", "sh")):
        forms.add(word + "es")
    if word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
        forms |= {word[:-1] + "ies", word[:-1] + "ied"}
    if word.endswith("e"):
        forms |= {word + "d", word[:-1] + "ing"}
    else:
        forms |= {word + "ed", word + "ing"}
    return forms


def term_regex(term):
    parts = [p for p in re.split(r"[\s\-]+", term) if p]
    if not parts:
        return None
    last = parts[-1]
    forms = {last, last + "s"} if last.isupper() else _word_forms(last.lower())
    last_pat = "(?:" + "|".join(
        sorted((re.escape(f) for f in forms), key=len, reverse=True)
    ) + ")"
    pieces = [re.escape(p) for p in parts[:-1]] + [last_pat]
    body = r"[\s\-]+".join(pieces)
    return re.compile(r"(?<![A-Za-z])" + body + r"(?![A-Za-z])", re.I)


def truncate(text, limit=420):
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def is_noise(text):
    return "???" in text or (text.count(" – ") >= 2 and len(text) < 300)


def definition_words(definition):
    return {w for w in re.findall(r"[a-z]{4,}", definition.lower()) if w not in STOP}


# Definitions alone cannot disambiguate every sense (e.g. exception = 异常 vs 例外).
CONTEXT_HINTS = {
    "exception": (r"\b(throw|catch|error|handling|propagat)\w*", r"\bno exception to\b"),
    "pointer": (r"\b(raw|smart|dangling|null|object|ownership|memory)\w*", r"\bdestructor\b"),
    "template": (r"\b(function|class|parameter|instantiat|generic)\w*", r"\bflag\b"),
    "encapsulation": (r"\b(interface|implementation|data|hide|detail)\w*", None),
    "reference": (r"\b(object|alias|const|pointer|dangl)\w*", r"\breference (number|section)\b"),
    "handle": (r"\b(resource|own|class)\w*", None),
    "invariant": (r"\b(class|constructor|condition|member|object|establish)\w*", r"\bjet\b"),
    "resource": (r"\b(manage|release|acquire|leak|handle|owner)\w*", None),
    "object": (r"\b(type|lifetime|entity|class|value)\w*", r"\bobject to\b"),
    "concept": (r"\b(require|template|satisf|constraint)\w*", None),
    "interface": (r"\b(class|type|operation|abstract|implement)\w*", None),
}

# Terms whose best context is a glossary definition rather than a rule example.
CONTEXT_OVERRIDES = {
    "encapsulation": "protecting something meant to be private",
}


def context_score(sentence, section, is_heading):
    if len(sentence) < 30 or "???" in sentence:
        return -100
    score = 0
    if SECTION_CODE.match(section):
        score += 4
    elif re.match(r"^[A-Z][A-Za-z]*:", section):
        score += 2
    if 60 <= len(sentence) <= 300:
        score += 2
    if " – " in sentence:
        score -= 3
    if is_heading:
        score -= 2
    if re.search(
        r"\b(?:is|are|was|were|can|should|must|may|will|use|uses|prefer|avoid|"
        r"return|returns|call|calls|pass|passes|provide|provides|ensure|ensures|"
        r"guarantee|guarantees)\b",
        sentence, re.I,
    ):
        score += 1
    return score


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    html_text = fetch_html()

    parser = DocExtractor()
    parser.feed(html_text)
    blocks = parser.blocks
    if not blocks:
        sys.exit("no prose extracted; the page structure may have changed")

    sentences = []
    for text, section, is_heading in blocks:
        if not is_heading and is_noise(text):
            continue
        if is_heading:
            sentences.append((text, section, True))
        else:
            for s in sentence_split(text):
                if 20 <= len(s) <= 600 and not is_noise(s):
                    sentences.append((s, section, False))

    con = sqlite3.connect(ECDICT)
    con.row_factory = sqlite3.Row
    cache = {}
    tf = collections.Counter()
    df = collections.Counter()
    upper = collections.Counter()
    ctx = {}

    for text, section, is_heading in blocks:
        if not is_heading and is_noise(text):
            continue
        seen = set()
        for raw in TOKEN.findall(normalize_text(text)):
            w = raw.lower().strip("'-")
            if "'" in w:
                continue
            if len(w) < 3 or w in STOP or w in BOILER:
                continue
            lem = lemma_of(w, con, cache)
            if lem in STOP or lem in BOILER or lem in FRAGMENTS:
                continue
            cache.setdefault(lem, True)
            tf[lem] += 1
            if raw[:1].isupper() or raw.isupper():
                upper[lem] += 1
            seen.add(lem)
        for lem in seen:
            df[lem] += 1

    for s, section, is_heading in sentences:
        score = context_score(s, section, is_heading)
        if score <= -50:
            continue
        for raw in TOKEN.findall(normalize_text(s)):
            w = raw.lower().strip("'-")
            if "'" in w:
                continue
            if len(w) < 3 or w in STOP or w in BOILER:
                continue
            lem = lemma_of(w, con, cache)
            if lem in STOP or lem in BOILER or lem in FRAGMENTS:
                continue
            if lem not in ctx or score > ctx[lem][0]:
                ctx[lem] = (score, truncate(s), section)

    existing = load_existing_words()
    general = []
    for word, count in tf.items():
        if len(word) < 4 and not word.isupper():
            continue
        if "-" in word:
            continue
        base = DOMAIN_FORMS.get(word, word)
        if base in DOMAIN_TERMS or word in existing or word in GENERAL_BLOCK:
            continue
        z = zipf_frequency(word, "en")
        if not (GENERAL_ZIPF_MIN <= z <= GENERAL_ZIPF_MAX):
            continue
        if df[word] < GENERAL_MIN_DF:
            continue
        min_tf = 2 if z <= 3.5 else 3
        if count < min_tf:
            continue
        e = entry_lookup(con, word)
        if not e or not clean_translation(e["translation"]):
            continue
        tags = (e["tag"] if e else "") or ""
        if upper[word] >= 0.6 * count and not word.isupper() and not tags:
            continue
        score = df[word] * 10 + min(count, 100) + z * 2
        if tags:
            score += 8
        general.append((score, word, e, z))
    general = [item for item in general if item[1] in ctx]
    general.sort(reverse=True)
    general = general[:GENERAL_LIMIT]

    # Domain terms that actually appear in the prose.
    domain = []
    dropped_domain = []
    for term, (pos, chinese, definition) in DOMAIN_TERMS.items():
        rx = term_regex(term)
        if not rx:
            continue
        hits = 0
        best = (-999, "", "")
        dw = definition_words(definition)
        hint = CONTEXT_HINTS.get(term)
        override = CONTEXT_OVERRIDES.get(term)
        for s, section, is_heading in sentences:
            if rx.search(s):
                hits += 1
                words = set(re.findall(r"[a-z]{4,}", s.lower()))
                score = context_score(s, section, is_heading) + 1.5 * len(dw & words)
                if hint:
                    include, avoid = hint
                    if re.search(include, s, re.I):
                        score += 2
                    if avoid and re.search(avoid, s, re.I):
                        score -= 3
                if override and override.lower() in s.lower():
                    score += 20
                if score > best[0]:
                    best = (score, truncate(s), section)
        if not hits:
            dropped_domain.append(term)
            continue
        z = round(zipf_frequency(term, "en"), 2)
        level = "B" if z >= 4.0 else ("A" if z >= 3.0 else "S")
        domain.append({
            "kind": "domain",
            "word": term,
            "pos": pos,
            "chinese": chinese,
            "definition": definition,
            "sentence": best[1],
            "section": best[2],
            "hits": hits,
            "level": level,
            "zipf": z,
            "ecdict": entry_lookup(con, term),
        })
    level_order = {"S": 0, "A": 1, "B": 2}
    domain.sort(key=lambda r: (level_order[r["level"]], -r["hits"], r["word"].lower()))

    ipa = ipa_cache_factory()
    rows = []

    for rank, (score, word, e, z) in enumerate(general, 1):
        src = ctx.get(word)
        phonetic = ipa(word) or ((e["phonetic"] if e else "") or "").strip("/ ")
        translation = clean_translation(e["translation"] if e else "")
        definition = clean_definition(e["definition"] if e else "")
        pos = pos_from_translation(e["translation"] if e else "") or ((e["pos"] if e else "") or "")
        tags = (e["tag"] if e else "") or ""
        level = "B" if z >= 4.0 else ("A" if z >= 3.5 else "S")
        rows.append({
            "kind": "general",
            "rank": rank,
            "word": word,
            "pos": pos,
            "phonetic": phonetic,
            "chinese": translation,
            "definition": definition,
            "sentence": src[1] if src else "",
            "section": src[2] if src else "",
            "tags": tags,
            "level": level,
            "doc_freq": tf.get(word, 0),
            "doc_blocks": df.get(word, 0),
            "zipf": round(z, 2),
            "score": score,
        })

    for i, item in enumerate(domain, 1):
        e = item["ecdict"]
        phonetic = ipa(item["word"])
        if not phonetic and e:
            phonetic = (e["phonetic"] or "").strip("/ ")
        rows.append({
            "kind": "domain",
            "rank": i,
            "word": item["word"],
            "pos": item["pos"],
            "phonetic": phonetic,
            "chinese": item["chinese"],
            "definition": item["definition"],
            "sentence": item["sentence"],
            "section": item["section"],
            "tags": "cpp domain",
            "level": item["level"],
            "doc_freq": item["hits"],
            "doc_blocks": item["hits"],
            "zipf": item["zipf"],
            "score": 0,
        })

    # master.csv
    columns = [
        "kind", "rank", "word", "pos", "phonetic", "chinese", "definition",
        "sentence", "section", "tags", "level", "doc_freq", "doc_blocks", "zipf", "score",
    ]
    with (OUT / "master.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=columns)
        w.writeheader()
        w.writerows(rows)

    write_dictionary(rows)
    write_domain_terms([r for r in rows if r["kind"] == "domain"])
    write_anki_csv(rows)
    write_apkg(rows)

    print(f"extracted blocks: {len(blocks)}, sentences: {len(sentences)}")
    print(f"general: {len(general)}  domain: {len(domain)}  total: {len(rows)}")
    if dropped_domain:
        print(f"domain terms not found in prose ({len(dropped_domain)}): "
              + ", ".join(dropped_domain[:20])
              + (" ..." if len(dropped_domain) > 20 else ""))
    print(f"wrote: {OUT}")


def md_escape(text):
    return (text or "").replace("[", "\\[").replace("]", "\\]")


def write_dictionary(rows):
    general = [r for r in rows if r["kind"] == "general"]
    for old in OUT.glob("dictionary-*.md"):
        old.unlink()
    lines = [
        "---",
        "type: dictionary",
        f"title: C++ Core Guidelines 通用词 1-{len(general)}",
        "tags: [library/word-bank, topic/cpp, skill/reading]",
        "---",
        "",
        f"# C++ Core Guidelines 通用词 1-{len(general)}",
        "",
        "> 音标/释义来自 ECDICT，例句来自 C++ Core Guidelines 原文；已剔除代码块，并与 10k 论文词库去重。先读例句，再记词。",
        "",
    ]
    for r in general:
        tags = f" · {r['tags']}" if r["tags"] else ""
        sentence = f'｜“{md_escape(r["sentence"])}”' if r["sentence"] else ""
        section = f"（{md_escape(r['section'])}）" if r["section"] else ""
        lines.append(
            f"- **{r['word']}** /{r['phonetic']}/ — {md_escape(r['chinese'])}"
            f"（{r['level']}{tags}）{sentence}{section}"
        )
    (OUT / "dictionary-general.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_domain_terms(rows):
    lines = [
        "---",
        "type: dictionary",
        "title: C++ Core Guidelines 领域术语",
        "tags: [library/word-bank, topic/cpp, skill/reading]",
        "---",
        "",
        "# C++ Core Guidelines 领域术语",
        "",
        "> 人工校订的技术义；例句来自规范原文。先理解定义，再用原句记搭配。",
        "",
        "| 术语 | 词性 | 中文 | 英文释义 | 出处 |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| **{md_escape(r['word'])}** | {r['pos']} | {md_escape(r['chinese'])} | "
            f"{md_escape(r['definition'])} | {md_escape(r['section'])} |"
        )
    (OUT / "domain-terms.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_anki_csv(rows):
    cols = ["word", "phonetic", "pos", "chinese", "definition", "sentence", "section", "tags"]
    with (OUT / "anki-01.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in cols})


def write_apkg(rows):
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for r in rows:
        tag_kind = "cpp-domain" if r["kind"] == "domain" else "cpp-vocab"
        tags = ["cpp", tag_kind, f"level-{r['level']}"]
        if r["kind"] == "domain":
            tags.append("domain")
        deck.add_note(
            genanki.Note(
                model=MODEL,
                fields=[
                    html.escape(r["word"], quote=False),
                    html.escape(r["phonetic"], quote=False),
                    html.escape(r["pos"], quote=False),
                    html.escape(r["chinese"], quote=False),
                    html.escape(r["definition"], quote=False),
                    html.escape(r["sentence"], quote=False),
                    html.escape(r["section"], quote=False),
                ],
                tags=sorted(set(tags)),
                guid=genanki.guid_for("cpp-core-guidelines", r["kind"], r["word"].lower()),
            )
        )
    out = OUT / "cpp-core-guidelines.apkg"
    genanki.Package(deck).write_to_file(out)
    print(f"apkg: {out} ({out.stat().st_size / 1_048_576:.1f} MB)")


if __name__ == "__main__":
    build()
