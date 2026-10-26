#!/usr/bin/env python3
"""Build one reading pack per paper from the extracted PDF text and vocabulary."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "14_llm-papers"
TEXT_DIR = Path.home() / "english" / "data" / "paper-text"
PDF_ROOT = Path.home() / "llm-papers"
OUT = PAPERS_DIR / "packs"

STOP = set("a an the and or but if while of to in on at by for from with without as is are was were be been being this that these those it its their our we you they he she i not no can could may might should would will".split())
SENSITIVE = re.compile(r"date rape|rape drug|child sexual|porn|suicide|self-harm|how to (?:kill|attack|harm)|attack someone|mass shooting|bomb", re.I)
BLOCK = {"self-harm", "suicide", "pornographic", "pornography", "porn", "rape", "bomb", "terrorist", "terrorism", "murder", "kill", "weapon", "sex", "sexual", "nude", "drug", "drugs", "sic", "acc", "pos"}


def md_escape(text: str) -> str:
    return text.replace("[", "\\[").replace("]", "\\]")


def clean(text: str) -> str:
    text = (text.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff")
            .replace("ﬃ", "ffi").replace("ﬄ", "ffl"))
    text = re.sub(r"-\s*\n\s*", "", text)
    return re.sub(r"\s+", " ", text)


def sentences(text: str):
    text = clean(text)
    text = re.split(r"\n\s*(?:References|REFERENCES|Bibliography|BIBLIOGRAPHY)\s*\n", text, maxsplit=1)[0]
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(0-9])", text)
    return [p.strip() for p in parts if 30 <= len(p.strip()) <= 600]


def parse_papers():
    papers = {}
    for f in sorted(PAPERS_DIR.glob("stage-*.md")):
        stage = int(f.name.split("-")[1])
        current = None
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^## (\d{2}-\d{2}) (.+)$", line)
            if m:
                current = m.group(1)
                papers[current] = {"stage": stage, "title": m.group(2).strip(),
                                   "chinese": "", "summary": ""}
                continue
            if current:
                if line.startswith("**中文标题**"):
                    papers[current]["chinese"] = line.split("：", 1)[-1].strip()
                elif line.startswith("**一句话概括**"):
                    papers[current]["summary"] = line.split("：", 1)[-1].strip()
    return papers


def pdf_for(pid):
    stage, num = int(pid.split("-")[0]), int(pid.split("-")[1])
    dirs = {0: "00_总览综述", 1: "01_大模型", 2: "02_多模态", 3: "03_音乐检索理解",
            4: "04_音乐生成", 5: "05_世界模型", 6: "06_强化学习"}
    base = PDF_ROOT / dirs[stage] / "PDF"
    for p in base.glob(f"{num:02d}_*.pdf"):
        return p
    return None


def arxiv_map():
    m = {}
    manifest = PDF_ROOT / "manifest.txt"
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("#") or "|" not in line:
                continue
            arxiv, path = line.split("|", 1)
            m[Path(path).name] = arxiv.strip()
    return m


def good_sentence(s: str) -> bool:
    if not (50 <= len(s) <= 600):
        return False
    if re.search(r"arXiv|★|Equal contribution|@|University|Institute|Department|Corresponding|Proceedings|Conference", s):
        return False
    if s.count(",") > 10 or s.count(" and ") > 8:
        return False
    if SENSITIVE.search(s):
        return False
    return True


def abstract_of(text: str, pdf, amap) -> str:
    if pdf:
        arxiv = amap.get(pdf.name, "")
        ap = PDF_ROOT / ".tmp_abstracts" / f"{arxiv}.txt"
        if arxiv and ap.exists():
            a = clean(ap.read_text(encoding="utf-8", errors="ignore"))
            if len(a) > 200:
                return a[:1400]
    if len(text) < 1000:
        return ""
    m = re.search(r"\bAbstract\b[:\s]*(.{200,3000}?)(?:\n\s*(?:1\s+)?Introduction|I\.\s+INTRODUCTION|Keywords?\b)", text, re.I | re.S)
    if m:
        a = clean(m.group(1))
    else:
        a = clean(text)[:1200]
    # cut at a sentence boundary around 1000 chars
    if len(a) > 1100:
        cut = a[:1100].rfind(".")
        if cut > 500:
            a = a[: cut + 1]
    return a


def slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:55] or "paper"


def load_vocab():
    per_paper = {}
    with (PAPERS_DIR / "vocabulary.csv").open(encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            per_paper.setdefault(row["paper_id"], []).append(row)
    master = {}
    with (PAPERS_DIR / "vocabulary-10k" / "master.csv").open(encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            master[row["word"].lower()] = row
    return per_paper, master


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    papers = parse_papers()
    per_paper, master = load_vocab()
    index = []
    for pid, info in papers.items():
        text = (TEXT_DIR / f"{pid}.txt").read_text(encoding="utf-8", errors="ignore")
        pdf = pdf_for(pid)
        words = per_paper.get(pid, [])
        # S first, then frequency
        words = [r for r in words if r["word"].lower() not in BLOCK]
        words = sorted(words, key=lambda r: (0 if r.get("level") == "S" else 1,
                                             -int(r.get("freq") or 0)))[:12]
        sents = sentences(text)
        word_blocks = []
        for r in words:
            w = r["word"]
            m = master.get(w.lower(), {})
            sentence = ""
            pat = re.compile(r"\b" + re.escape(w) + r"\b", re.I)
            for s in sents:
                if pat.search(s) and good_sentence(s):
                    sentence = s
                    break
            if not sentence:
                sentence = m.get("sentence", "") or r.get("context", "")
            if SENSITIVE.search(sentence):
                sentence = ""
            word_blocks.append({
                "word": w,
                "ipa": m.get("phonetic", ""),
                "chinese": r.get("chinese", "") or m.get("chinese", ""),
                "level": r.get("level", ""),
                "sentence": sentence,
            })
        abstract = abstract_of(text, pdf, arxiv_map())
        if SENSITIVE.search(abstract):
            abstract = info["summary"] or "PDF 语境含敏感内容，已省略；请直接阅读原文。"
        scanned = len(text) < 1000
        if not abstract:
            abstract = info["summary"] or "PDF 无可提取文本，请直接阅读 PDF。"
        fname = f"{pid}-{slug(info['title'])}.md"
        lines = [
            "---", "type: paper-pack", f'paper_id: "{pid}"', f'stage: {info["stage"]}',
            f'title: "{info["title"]}"', f'pdf: "{pdf or ""}"',
            "tags: [topic/paper, skill/reading, status/learning]", "---", "",
            f"# {pid} {info['title']}", "",
            f"**中文标题**：{info['chinese'] or '—'}", "",
            f"**一句话概括**：{info['summary'] or '—'}", "",
            "## 读前 2 分钟",
            "",
            "| 词 | 音标 | 中文 | 级别 |", "|---|---|---|---|",
        ]
        for b in word_blocks:
            lines.append(f"| {b['word']} | /{b['ipa']}/ | {b['chinese']} | {b['level']} |")
        lines += ["", "### 原句（保留完整句子）", ""]
        for b in word_blocks:
            if b["sentence"]:
                lines.append(f"- **{b['word']}** — “{md_escape(b['sentence'])}”")
        lines += [
            "", "## Abstract（自动提取）" if not scanned else "## 摘要提示（PDF 文本不可提取）", "",
            f"> {md_escape(abstract)}", "",
            "## 读中 30 分钟", "",
            "- [ ] 问题：这篇论文解决什么？",
            "- [ ] 方法：核心组件和数据流是什么？",
            "- [ ] 数据/指标：在哪些数据集、用什么指标？",
            "- [ ] 结果：主结果和消融说明了什么？",
            "- [ ] 局限：作者承认什么？我还有什么疑问？",
            "", "## 5 个理解问题", "",
            "1. What problem does the paper address, and why does it matter?",
            "2. What is the key idea, and what does it replace or improve?",
            "3. What data, baselines, and metrics are used?",
            "4. Which result is the most convincing, and which is weakest?",
            "5. What is one limitation, and what would you test next?",
            "", "## 60 秒复述", "",
            "> The paper addresses … The authors propose … The key idea is … They evaluate on … The results show … One limitation is …",
            "", "录音：`11_attachments/`", "",
            "## 写 3 句", "",
            "- The paper addresses …",
            "- The key idea is …",
            "- One limitation is …",
            "", "## 词汇复习", "",
            "- 把上面 10–12 个词加入 Anki；先读原句，再看中文。",
            "- 词库入口：[[14_llm-papers/vocabulary-10k/_index|论文 10k 词库]]",
            "", "## 相关", "",
            "- [[14_llm-papers/reading-plan|12 周阅读计划]]",
            f"- [[14_llm-papers/stage-0{info['stage']}-{'surveys' if info['stage']==0 else 'llm' if info['stage']==1 else 'multimodal' if info['stage']==2 else 'music-retrieval' if info['stage']==3 else 'music-generation' if info['stage']==4 else 'world-models' if info['stage']==5 else 'rl'}|阶段 {info['stage']}]]",
            "",
            f"PDF：`{pdf}`" if pdf else "PDF：未找到",
            "",
        ]
        (OUT / fname).write_text("\n".join(lines), encoding="utf-8")
        index.append((info["stage"], pid, info["title"], fname, scanned, len(word_blocks)))

    idx = ["---", "type: hub", "title: 168 篇阅读包", "tags: [hub, topic/paper, skill/reading]", "---", "",
           "# 168 篇阅读包", "",
           "> 每篇包含：8–12 个目标词、完整原句、自动摘要、5 个理解问题、60 秒复述模板。",
           "> `scanned` 表示 PDF 没有可提取文本，请直接读 PDF。", "",
           "| 阶段 | 论文 | 状态 | 词数 | 阅读包 |", "|---|---|---|---|---|"]
    for stage, pid, title, fname, scanned, n in sorted(index):
        idx.append(f"| {stage} | {pid} {title} | {'scanned' if scanned else 'text'} | {n} | [[14_llm-papers/packs/{fname[:-3]}\\|打开]] |")
    (OUT / "_index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print("packs", len(index), "scanned", sum(1 for x in index if x[4]))


if __name__ == "__main__":
    main()
