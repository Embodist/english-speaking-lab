#!/usr/bin/env python3
"""Chinese -> English draft translation via a local llama-server (Hy-MT2-1.8B)."""
import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


def build_prompt(text: str, target: str, style: str, glossary: list[str]) -> str:
    lines: list[str] = []
    if glossary:
        lines.append("参考下面的翻译：")
        lines.extend(glossary)
        lines.append("")
    if style:
        lines.append(f"请将以下文本翻译为{target}。注意翻译的风格要严格符合【{style}】：")
    else:
        lines.append(f"将以下文本翻译为{target}，注意只需要输出翻译后的结果，不要额外解释：")
    lines.append("")
    lines.append(text)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", nargs="?", help="Chinese text to translate")
    parser.add_argument("--file", type=Path, help="read Chinese text from a file")
    parser.add_argument("--stdin", action="store_true", help="read Chinese text from stdin")
    parser.add_argument("--target", default="英语", help="target language (Chinese name, default: 英语)")
    parser.add_argument("--style", default="", help="optional style, e.g. 技术面试口语 / 简洁书面")
    parser.add_argument("--glossary", type=Path, help="optional term file: 中文=English per line")
    parser.add_argument("--no-glossary", action="store_true", help="do not load the default glossary")
    parser.add_argument("--port", type=int, default=8081)
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--timeout", type=float, default=300)
    parser.add_argument("--json", action="store_true", help="print the raw JSON response")
    args = parser.parse_args()

    if args.file:
        text = args.file.read_text(encoding="utf-8")
    elif args.stdin:
        text = sys.stdin.read()
    elif args.text:
        text = args.text
    else:
        parser.error("provide text, --file, or --stdin")
    if not text.strip():
        parser.error("empty input")

    glossary: list[str] = []
    glossary_file = args.glossary
    if glossary_file is None and not args.no_glossary:
        default = Path(__file__).resolve().parent.parent / "15_resume" / "translation-glossary.txt"
        if default.exists():
            glossary_file = default
    if glossary_file:
        for line in glossary_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                zh, en = line.split("=", 1)
                glossary.append(f"{zh.strip()} 翻译成 {en.strip()}")
            else:
                glossary.append(line)

    prompt = build_prompt(text, args.target, args.style, glossary)
    payload = {
        "model": "hy-mt2-1.8b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": args.temperature,
        "top_p": 0.6,
        "top_k": 20,
        "max_tokens": args.max_tokens,
        "stream": False,
    }
    req = urllib.request.Request(
        f"http://127.0.0.1:{args.port}/v1/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=args.timeout) as resp:
            data = json.load(resp)
    except urllib.error.URLError as exc:
        print(
            "Translation server is not reachable. Start it with:\n"
            f"  bash {Path(__file__).resolve().parent / 'start-translate.sh'} --background\n"
            f"Error: {exc}",
            file=sys.stderr,
        )
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"Translation failed: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0
    try:
        content = data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError):
        print(f"Unexpected response: {data}", file=sys.stderr)
        return 1
    print(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
