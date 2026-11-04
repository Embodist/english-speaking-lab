---
type: dictionary
title: C++ Core Guidelines 领域术语
tags: [library/word-bank, topic/cpp, skill/reading]
---

# C++ Core Guidelines 领域术语

> 人工校订的技术义；例句来自规范原文。先理解定义，再用原句记搭配。

| 术语 | 词性 | 中文 | 英文释义 | 出处 |
|---|---|---|---|---|
| **constructor** | n. | 构造函数 | A special member function that initializes an object. | C.2: Use if the class has an invariant; use if the data members can vary independently |
| **destructor** | n. | 析构函数 | A special member function that releases an object's resources. | F.52: Prefer capturing by reference in lambdas that will be used locally, including passed to algorithms |
| **initialization** | n. | 初始化 | Giving an object its initial value. | C.42: If a constructor cannot construct a valid object, throw an exception |
| **namespace** | n. | 命名空间 | A scope that groups related names. | I.1: Make interfaces explicit |
| **GSL** | n. | 指南支持库 | The Guidelines Support Library. | P.11: Encapsulate messy constructs, rather than spreading through the code |
| **initializer** | n. | 初始化器 | A value or expression used to initialize an object. | C.13: If data member uses another data member , declare before |
| **RAII** | n. | 资源获取即初始化 | Tying resource lifetime to object lifetime. | E.6: Use RAII to prevent leaks |
| **copyable** | adj. | 可拷贝的 | A type whose objects can be copied. | F.7: For general use, take or arguments rather than smart pointers |
| **concurrency** | n. | 并发 | Executing tasks that make progress during overlapping periods. | CP.1: Assume that your code will run as part of a multi-threaded program |
| **postcondition** | n. | 后置条件 | A condition that must hold after a function returns. | I.7: State postconditions |
| **deallocation** | n. | 释放 | Releasing memory that was previously allocated. | P.8: Don’t leak any resources |
| **default constructor** | n. | 默认构造函数 | A constructor callable with no arguments. | C.43: Ensure that a copyable class has a default constructor |
| **enumeration** | n. | 枚举 | A type whose values are named constants. | Enum.2: Use enumerations to represent sets of related named constants |
| **polymorphic** | adj. | 多态的 | Supporting operations whose behavior depends on the dynamic type. | C.67: A polymorphic class should suppress public copy/move |
| **rvalue** | n. | 右值 | A temporary value that does not have a stable identity. | F.19: For “forward” parameters, pass by and only the parameter |
| **coroutine** | n. | 协程 | A function that can suspend and later resume execution. | CP.51: Do not use capturing lambdas that are coroutines |
| **iterator** | n. | 迭代器 | An object that traverses the elements of a container. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **precondition** | n. | 前置条件 | A condition that must hold before a function is called. | I.6: Prefer for expressing preconditions |
| **dereference** | v. | 解引用 | Accessing the object that a pointer refers to. | ES.65: Don’t dereference an invalid pointer |
| **enumerator** | n. | 枚举成员 | A named value of an enumeration type. | Enum.2: Use enumerations to represent sets of related named constants |
| **copy constructor** | n. | 拷贝构造函数 | A constructor that creates an object from another object of the same type. | C.67: A polymorphic class should suppress public copy/move |
| **move constructor** | n. | 移动构造函数 | A constructor that takes an rvalue reference and steals resources. | C.21: If you define or any copy, move, or destructor function, define or them all |
| **variadic** | adj. | 可变参数的 | Accepting an arbitrary number of arguments. | T.100: Use variadic templates when you need a function that takes a variable number of arguments of a variety of types |
| **indirection** | n. | 间接访问 | Extra access through a pointer, reference, or handle. | F.16: For “in” parameters, pass cheaply-copied types by value and others by reference to |
| **metaprogramming** | n. | 元编程 | Writing code that generates or manipulates code. | T.10: Specify concepts for all template arguments |
| **STL** | n. | 标准模板库 | The Standard Template Library, the containers and algorithms part of the standard library. | C.100: Follow the STL when defining a container |
| **deadlock** | n. | 死锁 | A state where threads wait forever for each other. | CP.9: Whenever feasible use tools to validate your concurrent code |
| **implementer** | n. | 实现者 | A person or component that provides an implementation. | C.129: When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance |
| **lvalue** | n. | 左值 | An expression that refers to an object with a stable identity. | ES.56: Write only when you need to explicitly move an object to another scope |
| **parallelism** | n. | 并行 | Executing tasks at the same time on multiple processors. | CP.par: Parallelism |
| **variadic template** | n. | 可变参数模板 | A template that accepts an arbitrary number of arguments. | I.9: If an interface is a template, document its parameters using concepts |
| **mutable** | adj. | 可变的 | Allowed to change after creation. | I.2: Avoid non- global variables |
| **refactor** | v. | 重构 | Improving code structure without changing behavior. | C.32: If a class has a raw pointer () or reference (), consider whether it might be owning |
| **rvalue reference** | n. | 右值引用 | A reference that can bind to temporaries and enable move semantics. | ES.56: Write only when you need to explicitly move an object to another scope |
| **callee** | n. | 被调用者 | The function that is called at a call site. | F.45: Don’t return a |
| **debug** | v. | 调试 | Finding and fixing defects. | I.6: Prefer for expressing preconditions |
| **idiom** | n. | 惯用法 | A conventional way of expressing something in a language. | C.41: A constructor should create a fully initialized object |
| **mutex** | n. | 互斥量 | A lock that allows only one thread into a critical section. | CP.22: Never call unknown code while holding a lock (e.g., a callback) |
| **TMP** | n. | 模板元编程 | Template metaprogramming: computing with templates at compile time. | T.121: Use template metaprogramming primarily to emulate concepts |
| **vectorization** | n. | 向量化 | Using SIMD instructions to process multiple values at once. | CP.mess: Message passing |
| **checkable** | adj. | 可检查的 | Able to be verified by a tool or test. | In.struct: The structure of this document |
| **linker** | n. | 链接器 | A tool that combines object files into an executable. | Glossary |
| **callback** | n. | 回调 | A function passed to be called later by another component. | F.1: “Package” meaningful operations as carefully named functions |
| **const** | n. | 常量限定 | A qualifier promising that a value will not be modified. | ES.56: Write only when you need to explicitly move an object to another scope |
| **deallocate** | v. | 释放 | To release memory that was previously allocated. | R.5: Prefer scoped objects, don’t heap-allocate unnecessarily |
| **declarator** | n. | 声明符 | The part of a declaration that gives a name and type. | ES.10: Declare one name (only) per declaration |
| **fallthrough** | n. | 贯穿 | Continuing into the next case of a switch statement. | ES.78: Don’t rely on implicit fallthrough in statements |
| **getter** | n. | 访问器 | A member function that returns a value. | C.131: Avoid trivial getters and setters |
| **pImpl** | n. | 实现指针惯用法 | Pointer-to-implementation idiom for separating interface and implementation. | I.27: For stable library ABI, consider the Pimpl idiom |
| **recompilation** | n. | 重新编译 | The act of compiling code again. | I.27: For stable library ABI, consider the Pimpl idiom |
| **setter** | n. | 修改器 | A member function that sets a value. | C.131: Avoid trivial getters and setters |
| **type erasure** | n. | 类型擦除 | Hiding concrete types behind a uniform interface. | T.49: Where possible, avoid type-erasure |
| **bool** | n. | 布尔类型 | The built-in type with values true and false. | ES.87: Don’t add redundant or to conditions |
| **callable** | adj. | 可调用的 | A type whose objects can be invoked like a function. | Discussion: Use a factory function if you need “virtual behavior” during initialization |
| **deleter** | n. | 删除器 | A callable that releases a resource owned by a smart pointer. | Discussion: Never return or throw while holding a resource not owned by a handle |
| **encapsulation** | n. | 封装 | Hiding internal details behind a stable interface. | Glossary |
| **immutability** | n. | 不可变性 | The property of not changing after creation. | P.10: Prefer immutable data to mutable data |
| **noexcept** | n. | 不抛出异常 | A specifier promising that a function will not throw. | C.37: Make destructors |
| **NVI** | n. | 非虚接口 | Non-Virtual Interface idiom. | Discussion: Make base class destructors public and virtual, or protected and non-virtual |
| **polymorphism** | n. | 多态 | Treating objects of different types through a common interface. | C.146: Use where class hierarchy navigation is unavoidable |
| **recompile** | v. | 重新编译 | To compile code again after a change. | C.129: When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance |
| **rollback** | n. | 回滚 | Restoring a previous state after a failure. | Discussion: Destructors, deallocation, and swap must never fail |
| **struct** | n. | 结构体 | A class whose members are public by default. | C.11: Make concrete types regular |
| **unary** | adj. | 一元的 | Taking one operand or argument. | R.31: If you have non- smart pointers, follow the basic pattern from |
| **verbosity** | n. | 冗长 | The amount of unnecessary code or text. | C.162: Overload operations that are roughly equivalent |
| **allocator** | n. | 分配器 | An object that manages memory allocation for containers. | T.61: Do not over-parameterize members (SCARY) |
| **async** | adj. | 异步的 | Not waiting for an operation to finish before continuing. | C.13: If data member uses another data member , declare before |
| **constexpr** | n. | 常量表达式 | A function or variable that can be evaluated at compile time. | Per.11: Move computation from run time to compile time |
| **covariant** | adj. | 协变的 | Preserving the inheritance relationship of a type parameter. | C.130: For making deep copies of polymorphic classes prefer a virtual function instead of public copy construction/assignment |
| **downcast** | n./v. | 向下转型 | Converting a base-class pointer or reference to a derived type. | C.146: Use where class hierarchy navigation is unavoidable |
| **freestanding** | adj. | 独立的 | An implementation that need not provide the full hosted library. | C.129: When designing a class hierarchy, distinguish between implementation inheritance and interface inheritance |
| **invalidation** | n. | 失效 | Making a pointer, reference, or iterator no longer usable. | F.43: Never (directly or indirectly) return a pointer or a reference to a local object |
| **negation** | n. | 否定 | A requirement that a condition must not hold. | ES.87: Don’t add redundant or to conditions |
| **nullptr** | n. | 空指针字面量 | The null pointer literal introduced in C++11. | C.43: Ensure that a copyable class has a default constructor |
| **subexpression** | n. | 子表达式 | An expression nested inside a larger expression. | R.13: Perform at most one explicit resource allocation in a single expression statement |
| **vtable** | n. | 虚函数表 | The table used to dispatch virtual function calls. | C.90: Rely on constructors and assignment operators, not and |
| **writable** | adj. | 可写的 | A type or object whose value can be modified. | CP.3: Minimize explicit sharing of writable data |
| **copy elision** | n. | 拷贝消除 | Avoiding unnecessary copy or move operations. | Discussion: Return containers by value (relying on move or copy elision for efficiency) |
| **elision** | n. | 省略 | Avoiding an unnecessary copy or move operation. | Discussion: Return containers by value (relying on move or copy elision for efficiency) |
| **scalable** | adj. | 可扩展的 | Continuing to work well as size or load grows. | CP.102: Carefully study the literature |
| **stack unwinding** | n. | 栈展开 | Destroying local objects while propagating an exception. | Discussion: Destructors, deallocation, and swap must never fail |
| **underflow** | n. | 下溢 | A value falling below the range its type can represent. | ES.104: Don’t underflow |
| **pointer** | n. | 指针 | An object that stores the address of another object. | P.1: Express ideas directly in code |
| **template** | n. | 模板 | A parameterized type or function. | ES.11: Use to avoid redundant repetition of type names |
| **parameter** | n. | 形参 | A named variable declared in a function signature. | I.12: Declare a pointer that must not be null as |
| **compiler** | n. | 编译器 | A tool that translates source code into machine code. | C.146: Use where class hierarchy navigation is unavoidable |
| **explicit** | adj. | 显式的 | A constructor qualifier that prevents implicit conversions. | F.20: For “out” output values, prefer return values to output parameters |
| **semantics** | n. | 语义 | The meaning of code, as opposed to its syntax. | T.10: Specify concepts for all template arguments |
| **macro** | n. | 宏 | A preprocessor text substitution. | ES.9: Avoid names |
| **invariant** | n. | 不变量 | A condition that must always hold during execution. | C.2: Use if the class has an invariant; use if the data members can vary independently |
| **header** | n. | 头文件 | A file included to declare interfaces and types. | ES.8: Avoid similar-looking names |
| **lambda** | n. | 匿名函数 | An unnamed function object defined inline. | F.50: Use a lambda when a function won’t do (to capture local variables, or to write a local function) |
| **overload** | v./n. | 重载 | Providing multiple functions with the same name and different parameters. | C.170: If you feel like overloading a lambda, use a generic lambda |
| **allocation** | n. | 分配 | Reserving memory for an object. | Pro.bounds: Bounds safety profile |
| **bounds** | n. | 边界 | The limits of a valid range, especially array indices. | In.force: Enforcement |
| **compile time** | n. | 编译期 | The phase when source code is translated. | Per.11: Move computation from run time to compile time |
| **smart pointer** | n. | 智能指针 | An object that owns a resource and releases it automatically. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **caller** | n. | 调用者 | The code that calls a function. | I.1: Make interfaces explicit |
| **error-prone** | adj. | 易出错的 | Likely to cause mistakes. | In.aims: Aims |
| **ISO** | n. | 国际标准化组织 | The body that standardizes C++. | P.2: Write in ISO Standard C++ |
| **undefined behavior** | n. | 未定义行为 | Behavior for which the C++ standard imposes no requirements. | P.2: Write in ISO Standard C++ |
| **raw pointer** | n. | 裸指针 | A pointer without ownership semantics. | I.10: Use exceptions to signal a failure to perform a required task |
| **class hierarchy** | n. | 类层次结构 | A tree of classes connected by inheritance. | C.133: Avoid data |
| **optimization** | n. | 优化 | Improving efficiency without changing behavior. | P.9: Don’t waste time or space |
| **abstraction** | n. | 抽象 | Hiding implementation details behind a simpler, stable interface. | CPL.3: If you must use C for interfaces, use C++ in the calling code using such interfaces |
| **unsigned** | adj. | 无符号的 | A type that represents only non-negative values. | ES.46: Avoid lossy (narrowing, truncating) arithmetic conversions |
| **alias** | n. | 别名 | An alternative name for a type or entity. | T.42: Use template aliases to simplify notation and hide implementation details |
| **trivial** | adj. | 平凡的 | A type or operation with no user-defined behavior. | C.131: Avoid trivial getters and setters |
| **reuse** | n./v. | 复用 | Using code or resources again. | CP.61: Use to spawn concurrent tasks |
| **template argument** | n. | 模板实参 | The actual type or value supplied to a template. | T.2: Use templates to express algorithms that apply to many argument types |
| **ABI** | n. | 应用二进制接口 | The binary-level calling and layout contract between compiled code. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **overhead** | n. | 开销 | Extra cost in time, memory, or complexity. | F.23: Use a to indicate that “null” is not a valid value |
| **unnamed** | adj. | 未命名的 | Without a name. | F.9: Unused parameters should be unnamed |
| **cleanup** | n. | 清理 | Releasing resources or restoring state. | E.16: Destructors, deallocation, , and exception type copy/move construction must never fail |
| **generic programming** | n. | 泛型编程 | Writing code that works with many types. | C.162: Overload operations that are roughly equivalent |
| **overflow** | n. | 溢出 | A value exceeding the range its type can represent. | P.5: Prefer compile-time checking to run-time checking |
| **template parameter** | n. | 模板参数 | A type or value parameter of a template. | ES.56: Write only when you need to explicitly move an object to another scope |
| **locking** | n. | 加锁 | Using a lock to protect shared data. | CP.111: Use a conventional pattern if you really need double-checked locking |
| **synchronization** | n. | 同步 | Coordinating concurrent accesses to shared state. | F.53: Avoid capturing by reference in lambdas that will be used non-locally, including returned, stored on the heap, or passed to another thread |
| **dangling pointer** | n. | 悬空指针 | A pointer to an object whose lifetime has ended. | F.7: For general use, take or arguments rather than smart pointers |
| **heap** | n. | 堆 | Memory for dynamically allocated objects. | FAQ.58: Is the same as or the proposed ? |
| **assertion** | n. | 断言 | A statement that a condition must be true. | GSL.assert: Assertions |
| **analyzer** | n. | 分析器 | A tool that inspects code or data. | P.12: Use supporting tools as appropriate |
| **bounds safety** | n. | 边界安全 | Ensuring accesses stay within valid ranges. | Pro.safety: Type-safety profile |
| **cache** | n./v. | 缓存 | Fast storage for frequently used data. | P.9: Don’t waste time or space |
| **handler** | n. | 处理器 | Code that responds to an event or error. | I.10: Use exceptions to signal a failure to perform a required task |
| **inline** | adj./v. | 内联 | A request to expand a function at its call site. | F.3: Keep functions short and simple |
| **override** | v./n. | 重写 | Replacing a virtual function in a derived class. | C.120: Use class hierarchies to represent concepts with inherent hierarchical structure (only) |
| **swap** | n./v. | 交换 | Exchanging the values of two objects. | C.83: For value-like types, consider providing a swap function |
| **portable** | adj. | 可移植的 | Working across different platforms and compilers. | ES.64: Use the notation for construction |
| **specialization** | n. | 特化 | A version of a template for specific arguments. | R.31: If you have non- smart pointers, follow the basic pattern from |
| **atomic** | adj. | 原子的 | Indivisible with respect to concurrent operations. | F.27: Use a to share ownership |
| **resource leak** | n. | 资源泄漏 | A resource that is acquired but never released. | E.1: Develop an error-handling strategy early in a design |
| **static analysis** | n. | 静态分析 | Finding problems by analyzing code without running it. | I.12: Declare a pointer that must not be null as |
| **detached** | adj. | 分离的 | A thread that runs independently of its creator. | CP.24: Think of a as a global container |
| **movable** | adj. | 可移动的 | A type whose resources can be transferred by move. | F.7: For general use, take or arguments rather than smart pointers |
| **singleton** | n. | 单例 | A design that restricts a class to one instance. | I.3: Avoid singletons |
| **value semantics** | n. | 值语义 | Copying a value produces an independent object. | C.61: A copy operation should copy |
| **wrapper** | n. | 包装器 | A type or function that adapts another interface. | ES.50: Don’t cast away |
| **API** | n. | 应用编程接口 | The interface through which code calls a library. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **forwarding** | n. | 转发 | Passing an argument on while preserving its value category. | F.45: Don’t return a |
| **naked pointer** | n. | 裸指针 | A raw pointer without ownership semantics. | R.11: Avoid calling and explicitly |
| **assert** | v. | 断言 | To state that a condition must be true. | Glossary |
| **diagnostic** | n. | 诊断信息 | A message from a tool that reports a problem. | I.12: Declare a pointer that must not be null as |
| **directive** | n. | 指示/指令 | An instruction to the compiler or preprocessor. | SF.13: Use portable header identifiers in statements |
| **move semantics** | n. | 移动语义 | Transferring ownership of resources instead of copying them. | P.9: Don’t waste time or space |
| **zero-overhead** | adj. | 零开销 | An abstraction that costs no more than hand-written code. | In.aims: Aims |
| **buffer overflow** | n. | 缓冲区溢出 | Writing past the bounds of a buffer. | ES.27: Use or for arrays on the stack |
| **copy semantics** | n. | 拷贝语义 | Creating a new object with the same value as an existing one. | C.130: For making deep copies of polymorphic classes prefer a virtual function instead of public copy construction/assignment |
| **cyclic** | adj. | 循环的 | Depending on itself, directly or indirectly. | R.24: Use to break cycles of s |
| **header-only** | adj. | 仅头文件 | A library provided entirely in header files. | A.2: Express potentially reusable parts as a library |
| **linking** | n. | 链接 | Combining object files and libraries into a program. | T.83: Do not declare a member function template virtual |
| **aggregate** | n. | 聚合体 | A class or array type initialized directly from a brace-enclosed list. | F.27: Use a to share ownership |
| **dynamic allocation** | n. | 动态分配 | Allocating memory at run time. | C.10: Prefer concrete types over class hierarchies |
| **forwarding reference** | n. | 转发引用 | A T&& parameter that preserves the argument's value category. | ES.56: Write only when you need to explicitly move an object to another scope |
| **inline function** | n. | 内联函数 | A function defined in a header and expanded at call sites. | SF.2: A header file must not contain object definitions or non-inline function definitions |
| **intrusive** | adj. | 侵入式的 | A container design that requires elements to embed bookkeeping data. | C.136: Use multiple inheritance to represent the union of implementation attributes |
| **robust** | adj. | 健壮的 | Able to handle unexpected inputs without failing. | E.2: Throw an exception to signal that a function can’t perform its assigned task |
| **shared pointer** | n. | 共享指针 | A smart pointer that shares ownership of a resource. | C.127: A class with a virtual function should have a virtual or protected destructor |
| **type deduction** | n. | 类型推导 | Letting the compiler infer a type from context. | F.45: Don’t return a |
| **unspecified behavior** | n. | 未指定行为 | Behavior chosen from a set of allowed alternatives. | A.4: There should be no cycles among libraries |
| **unwind** | v. | 展开 | Leaving nested scopes, especially while propagating an exception. | Discussion: Destructors, deallocation, and swap must never fail |
| **dangling reference** | n. | 悬空引用 | A reference to an object whose lifetime has ended. | In.force: Enforcement |
| **perfect forwarding** | n. | 完美转发 | Forwarding arguments while preserving their value category. | F.45: Don’t return a |
| **regression** | n. | 回归 | A defect that breaks previously working behavior. | CP.101: Distrust your hardware/compiler combination |
| **runtime** | n. | 运行时 | The support code and environment in which a program executes. | FAQ.58: Is the same as or the proposed ? |
| **object** | n. | 对象 | An entity with a type and a lifetime. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **member** | n. | 成员 | A data field or function belonging to a class. | I.5: State preconditions (if any) |
| **exception** | n. | 异常 | An object used to signal and propagate errors. | R.13: Perform at most one explicit resource allocation in a single expression statement |
| **interface** | n. | 接口 | The operations a type exposes to its users. | C.135: Use multiple inheritance to represent multiple distinct interfaces |
| **reference** | n. | 引用 | An alias to an existing object. | P.1: Express ideas directly in code |
| **variable** | n. | 变量 | A named object whose value can change. | I.10: Use exceptions to signal a failure to perform a required task |
| **argument** | n. | 实参 | A value passed to a function at a call site. | F.7: For general use, take or arguments rather than smart pointers |
| **implementation** | n. | 实现 | The concrete code behind an interface. | Per.7: Design to enable optimization |
| **handle** | n. | 句柄 | An object that owns and manages a resource. | C.con: Containers and other resource handles |
| **resource** | n. | 资源 | Something that must be acquired and released, such as memory, a file, or a lock. | Glossary |
| **concept** | n. | 概念 | A named set of requirements on template parameters (C++20). | I.4: Make interfaces precisely and strongly typed |
| **scope** | n. | 作用域 | The region of code where a name is visible. | P.12: Use supporting tools as appropriate |
| **access** | n./v. | 访问 | The ability to read or modify an object or resource. | C.145: Access polymorphic objects through pointers and references |
| **standard library** | n. | 标准库 | The library defined by the C++ standard. | F.17: For “in-out” parameters, pass by reference to non- |
| **virtual** | adj. | 虚的 | Allowing a derived class to override a function. | C.120: Use class hierarchies to represent concepts with inherent hierarchical structure (only) |
| **thread** | n. | 线程 | A single flow of execution within a process. | CP.1: Assume that your code will run as part of a multi-threaded program |
| **container** | n. | 容器 | A type that stores and manages a collection of elements. | ES.64: Use the notation for construction |
| **array** | n. | 数组 | A contiguous sequence of elements of the same type. | Per.7: Design to enable optimization |
| **assignment** | n. | 赋值 | Replacing the value of an object with another value. | C.67: A polymorphic class should suppress public copy/move |
| **operator** | n. | 运算符 | A symbol that performs an operation. | F.47: Return from assignment operators |
| **definition** | n. | 定义 | Providing the implementation or storage for an entity. | SF.22: Use an unnamed (anonymous) namespace for all internal/non-exported entities |
| **statement** | n. | 语句 | A unit of execution in a program. | I.6: Prefer for expressing preconditions |
| **base class** | n. | 基类 | A class from which other classes inherit. | C.67: A polymorphic class should suppress public copy/move |
| **declaration** | n. | 声明 | Introducing a name and its type to the compiler. | C.7: Don’t define a class or enum and declare a variable of its type in the same statement |
| **performance** | n. | 性能 | How efficiently a program uses time and resources. | I.10: Use exceptions to signal a failure to perform a required task |
| **programming** | n. | 编程 | Writing code; designing and implementing programs. | In.0: Don’t panic! |
| **cast** | n./v. | 类型转换 | An explicit conversion from one type to another. | ES.64: Use the notation for construction |
| **expression** | n. | 表达式 | A sequence of operators and operands that produces a value. | ES.42: Keep use of pointers simple and straightforward |
| **behavior** | n. | 行为 | The observable actions of a program or object. | C.67: A polymorphic class should suppress public copy/move |
| **leak** | n./v. | 泄漏 | Failing to release a resource such as memory. | R.1: Manage resources automatically using resource handles and RAII (Resource Acquisition Is Initialization) |
| **ownership** | n. | 所有权 | Responsibility for releasing a resource. | P.6: What cannot be checked at compile time should be checkable at run time |
| **string** | n. | 字符串 | A sequence of characters. | R.2: In interfaces, use raw pointers to denote individual objects (only) |
| **derived class** | n. | 派生类 | A class that inherits from a base class. | C.10: Prefer concrete types over class hierarchies |
| **static** | adj. | 静态的 | Having a lifetime or scope fixed at compile time. | ES.42: Keep use of pointers simple and straightforward |
| **run time** | n. | 运行期 | The phase when a program executes. | In.force: Enforcement |
| **lifetime** | n. | 生命周期 | The period during which an object exists. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **profile** | n. | 规范集 | A set of rules that enforce a property such as type safety. | Pro.safety: Type-safety profile |
| **violation** | n. | 违规 | Breaking a rule or contract. | In.not: Non-aims |
| **return value** | n. | 返回值 | The value a function yields to its caller. | F.23: Use a to indicate that “null” is not a valid value |
| **data race** | n. | 数据竞争 | Conflicting unsynchronized accesses to the same memory. | CP.9: Whenever feasible use tools to validate your concurrent code |
| **enforcement** | n. | 强制实施 | Automatic checking that a rule is followed. | In.force: Enforcement |
| **destruction** | n. | 销毁 | Releasing an object's resources at the end of its lifetime. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **non-local** | adj. | 非局部的 | Not limited to the current scope or function. | R.37: Do not pass a pointer or reference obtained from an aliased smart pointer |
| **resource management** | n. | 资源管理 | Acquiring and releasing resources correctly. | P.6: What cannot be checked at compile time should be checkable at run time |
| **stack** | n. | 栈 | Memory for local objects with automatic lifetime. | R.5: Prefer scoped objects, don’t heap-allocate unnecessarily |
| **function object** | n. | 函数对象 | An object that can be called like a function. | CP.23: Think of a joining as a scoped container |
| **concrete type** | n. | 具体类型 | A type with a complete, directly usable definition. | C.10: Prefer concrete types over class hierarchies |
| **non-virtual** | adj. | 非虚的 | Not dispatched through the virtual function mechanism. | C.35: A base class destructor should be either public and virtual, or protected and non-virtual |
| **move assignment** | n. | 移动赋值 | Transferring resources from one object to another by assignment. | ES.56: Write only when you need to explicitly move an object to another scope |
| **contract** | n. | 契约 | A documented precondition, postcondition, or invariant. | C.41: A constructor should create a fully initialized object |
| **lock-free** | adj. | 无锁的 | An algorithm that guarantees progress without mutual exclusion locks. | CP.free: Lock-free programming |
| **factory function** | n. | 工厂函数 | A function that creates and returns an object. | C.41: A constructor should create a fully initialized object |
| **type-safe** | adj. | 类型安全的 | Guaranteeing that operations are valid for their types. | ES.49: If you must use a cast, use a named cast |
| **abstract class** | n. | 抽象类 | A class that cannot be instantiated directly; used to define an interface. | Glossary |
| **global variable** | n. | 全局变量 | A variable visible and accessible across a whole program. | E.28: Avoid error handling based on global state (e.g. ) |
| **copy assignment** | n. | 拷贝赋值 | Assigning one object's value to another object. | C.21: If you define or any copy, move, or destructor function, define or them all |
| **lifetime safety** | n. | 生命周期安全 | Ensuring no use after an object's lifetime ends. | F.7: For general use, take or arguments rather than smart pointers |
| **exception handling** | n. | 异常处理 | Throwing, catching, and cleaning up after exceptions. | NR.3: Don’t avoid exceptions |
| **race condition** | n. | 竞态条件 | A result that depends on the timing of concurrent operations. | I.7: State postconditions |
| **source file** | n. | 源文件 | A file containing implementation code. | SF.22: Use an unnamed (anonymous) namespace for all internal/non-exported entities |
| **type safety** | n. | 类型安全 | Ensuring operations are valid for the types they are applied to. | Pro.safety: Type-safety profile |
| **suspension** | n. | 挂起 | Pausing a coroutine or thread until it is resumed. | CP.51: Do not use capturing lambdas that are coroutines |
| **user-defined type** | n. | 用户定义类型 | A type defined by the programmer, such as a class or enum. | C: Classes and class hierarchies |
| **error code** | n. | 错误码 | A value returned to indicate success or failure. | C.42: If a constructor cannot construct a valid object, throw an exception |
| **thread-safe** | adj. | 线程安全的 | Correct when called from multiple threads. | I.3: Avoid singletons |
| **shared ownership** | n. | 共享所有权 | Multiple owners share responsibility for a resource. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **implementation-defined** | adj. | 实现定义的 | Behavior the C++ standard leaves to each implementation. | P.2: Write in ISO Standard C++ |
| **object code** | n. | 目标代码 | Compiler output before linking. | Glossary |
| **legacy code** | n. | 遗留代码 | Old code that must keep working. | R.3: A raw pointer (a ) is non-owning |
| **side effect** | n. | 副作用 | An observable change beyond returning a value. | F.52: Prefer capturing by reference in lambdas that will be used locally, including passed to algorithms |
| **thread safety** | n. | 线程安全 | Correct behavior when code runs concurrently. | CP.1: Assume that your code will run as part of a multi-threaded program |
| **constant expression** | n. | 常量表达式 | An expression evaluable at compile time. | F.4: If a function might have to be evaluated at compile time, declare it |
| **message passing** | n. | 消息传递 | Communication between threads by sending messages. | CP.3: Minimize explicit sharing of writable data |
| **trade-off** | n. | 权衡 | A balance between competing goals. | I.27: For stable library ABI, consider the Pimpl idiom |
| **code review** | n. | 代码审查 | Examining code for defects and design issues. | In.force: Enforcement |
| **exception safety** | n. | 异常安全 | A guarantee about object state when an exception is thrown. | R.22: Use to make s |
| **ownership transfer** | n. | 所有权转移 | Moving responsibility for a resource to another owner. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **pass by reference** | phr. | 按引用传递 | Passing a reference to an argument to a function. | F.52: Prefer capturing by reference in lambdas that will be used locally, including passed to algorithms |
| **pass by value** | phr. | 按值传递 | Passing a copy of an argument to a function. | CP.3: Minimize explicit sharing of writable data |
| **pure function** | n. | 纯函数 | A function whose result depends only on its arguments and has no side effects. | F.8: Prefer pure functions |
| **thread pool** | n. | 线程池 | A set of worker threads that execute queued tasks. | CP.61: Use to spawn concurrent tasks |
| **unit test** | n. | 单元测试 | A test of one small piece of code in isolation. | A.1: Separate stable code from less stable code |
| **value type** | n. | 值类型 | A type whose values behave like independent copies. | E.15: Throw by value, catch exceptions from a hierarchy by reference |
| **exclusive ownership** | n. | 独占所有权 | Exactly one owner is responsible for a resource. | I.11: Never transfer ownership by a raw pointer () or reference () |
| **garbage collection** | n. | 垃圾回收 | Automatically reclaiming unreachable memory. | P.8: Don’t leak any resources |
| **memory leak** | n. | 内存泄漏 | Allocated memory that is never released. | E: Error handling |
| **translation unit** | n. | 翻译单元 | A source file after preprocessing, compiled as one unit. | I.22: Avoid complex initialization of global objects |
