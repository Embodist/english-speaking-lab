#!/usr/bin/env python3
"""Install the English Lab dictionaries into a local qwerty-learner clone.

Usage:
  python scripts/install_qwerty_dicts.py /path/to/qwerty-learner

Copies 19_qwerty-learner/dicts/*.json to <repo>/public/dicts/ and adds a
generated `englishLabDicts` array to src/resources/dictionary.ts.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "19_qwerty-learner"
MANIFEST = SRC / "manifest.json"
DICTS = SRC / "dicts"
MARKER = "// English Lab dictionaries (generated)"
END_MARKER = "// End English Lab dictionaries"
ARRAY_NAME = "englishLabDicts"


def ts_string(value):
    return json.dumps(value, ensure_ascii=False)


def build_block(manifest):
    lines = [MARKER, f"const {ARRAY_NAME}: DictionaryResource[] = ["]
    for item in manifest:
        lines.append("  {")
        lines.append(f"    id: {ts_string(item['id'])},")
        lines.append(f"    name: {ts_string(item['name'])},")
        lines.append(f"    description: {ts_string(item['description'])},")
        lines.append(f"    category: {ts_string(item['category'])},")
        tags = ", ".join(ts_string(tag) for tag in item["tags"])
        lines.append(f"    tags: [{tags}],")
        lines.append(f"    url: {ts_string('/dicts/' + item['file'])},")
        lines.append(f"    length: {item['length']},")
        lines.append(f"    language: {ts_string(item['language'])},")
        lines.append(f"    languageCategory: {ts_string(item['languageCategory'])},")
        lines.append("  },")
    lines.append("]")
    lines.append(END_MARKER)
    return "\n".join(lines)


def patch_registry(path, block):
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        start = text.index(MARKER)
        end = text.index(END_MARKER, start) + len(END_MARKER)
        text = text[:start] + text[end:].lstrip("\n")
    insert_at = text.find("/**\n * Built-in dictionaries in an array.")
    if insert_at < 0:
        insert_at = text.find("export const dictionaryResources")
    if insert_at < 0:
        raise SystemExit("could not find dictionaryResources in dictionary.ts")
    text = text[:insert_at] + block + "\n\n" + text[insert_at:]

    start = text.index("export const dictionaryResources: DictionaryResource[] = [")
    open_bracket = text.index("= [", start) + 3
    if f"...{ARRAY_NAME}" not in text:
        text = text[:open_bracket] + f"\n  ...{ARRAY_NAME}," + text[open_bracket:]
    path.write_text(text, encoding="utf-8")


LOCAL_TTS_MARKER = "// English Lab local TTS"


def patch_pronunciation(repo):
    path = repo / "src" / "hooks" / "usePronunciation.ts"
    if not path.is_file():
        print(f"skip pronunciation patch: {path} not found")
        return
    text = path.read_text(encoding="utf-8")
    if LOCAL_TTS_MARKER not in text:
        anchor = "const pronunciationApi = 'https://dict.youdao.com/dictvoice?audio='"
        if anchor not in text:
            print("skip pronunciation patch: anchor not found")
            return
        text = text.replace(
            anchor,
            anchor + "\nconst LOCAL_TTS_API = 'http://127.0.0.1:8010/tts?word=' " + LOCAL_TTS_MARKER,
        )
        old_cases = """    case 'uk':
      return `${pronunciationApi}${word}&type=1`
    case 'us':
      return `${pronunciationApi}${word}&type=2`"""
        new_cases = """    case 'uk':
    case 'us':
      return `${LOCAL_TTS_API}${encodeURIComponent(word)}&lang=${pronunciation}`"""
        if old_cases in text:
            text = text.replace(old_cases, new_cases)
    if "format: ['wav', 'mp3']" not in text:
        text = text.replace("format: ['mp3']", "format: ['wav', 'mp3']")
    path.write_text(text, encoding="utf-8")
    print(f"patched pronunciation: {path}")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    repo = Path(sys.argv[1]).expanduser().resolve()
    dict_dir = repo / "public" / "dicts"
    registry = repo / "src" / "resources" / "dictionary.ts"
    if not dict_dir.is_dir() or not registry.is_file():
        raise SystemExit(f"not a qwerty-learner repo: {repo}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for item in manifest:
        shutil.copy2(DICTS / item["file"], dict_dir / item["file"])
    patch_registry(registry, build_block(manifest))
    patch_pronunciation(repo)
    print(f"copied {len(manifest)} dictionaries to {dict_dir}")
    print(f"patched {registry}")
    print("next: cd", repo, "&& yarn install && yarn dev")
    print("then open http://localhost:5173 and choose category 'English Lab'")
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    repo = Path(sys.argv[1]).expanduser().resolve()
    dict_dir = repo / "public" / "dicts"
    registry = repo / "src" / "resources" / "dictionary.ts"
    if not dict_dir.is_dir() or not registry.is_file():
        raise SystemExit(f"not a qwerty-learner repo: {repo}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for item in manifest:
        shutil.copy2(DICTS / item["file"], dict_dir / item["file"])
    patch_registry(registry, build_block(manifest))
    print(f"copied {len(manifest)} dictionaries to {dict_dir}")
    print(f"patched {registry}")
    print("next: cd", repo, "&& yarn install && yarn dev")
    print("then open http://localhost:5173 and choose category 'English Lab'")


if __name__ == "__main__":
    main()
