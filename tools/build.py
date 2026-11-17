#!/usr/bin/env python3
"""Fail-closed builder for The Reading Room. Source files are never modified."""
from __future__ import annotations
import hashlib, html, json, re, shutil, sys
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"site"
APPS=SITE/"apps"
COLLECTIONS=SITE/"collections"
DATA=SITE/"data"
REPORT=ROOT/"PUBLISHING-REVIEW.md"
EXCLUDE={".git",".github","site","tools","__pycache__"}
MATURE=re.compile(r"(adult|18\+|taboo|sensual|transgressive|dark-ink|manhwa300)",re.I)
SECRET_PATTERNS=[
 ("private key",re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
 ("AWS access key",re.compile(rb"\bAKIA[0-9A-Z]{16}\b")),
 ("GitHub token",re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
 ("generic API token",re.compile(rb"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{20,}")),
 ("bearer credential",re.compile(rb"(?i)authorization\s*[:=]\s*bearer\s+[A-Za-z0-9._~+/=-]{20,}")),
 ("email address",re.compile(rb"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",re.I)),
 ("phone-like number",re.compile(rb"(?<!\d)(?:\+?\d[\s().-]?){9,14}(?!\d)")),
]
def slug(s):
    out=re.sub(r"[^a-z0-9]+","-",Path(s).stem.lower()).strip("-")
    return out or hashlib.sha1(s.encode()).hexdigest()[:10]
def category(name):
    n=name.lower()
    if any(x in n for x in ("generator","diary","tracker","typewriter","journal")): return "Interactive tools"
    if any(x in n for x in ("film","cinema","movie")): return "Cinema"
    if any(x in n for x in ("manga","manhwa","anime","comic")): return "Manga & Comics"
    if any(x in n for x in ("art","watercolour","collage","bob_ross","poetry")): return "Art"
    if any(x in n for x in ("kid","child","three_year","world_stories","reading_guide")): return "Family"
    if any(x in n for x in ("security","cyber","crypto","pine","ath")): return "Security"
    if any(x in n for x in ("curriculum","course","development","prompt","thinker","inspiration")): return "Learning"
    if any(x in n for x in ("book","reading","poem","kavit","fiction","literature")): return "Reading & Literature"
    return "Other"
def searchable_text(raw):
    raw=re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>"," ",raw)
    raw=re.sub(r"(?s)<[^>]+>"," ",raw)
    return html.unescape(re.sub(r"\s+"," ",raw)).strip()[:250000]
def title_from_html(raw, filename):
    m=re.search(r"<title[^>]*>(.*?)</title>",raw,re.I|re.S)
    if m:
        t=re.sub(r"<[^>]+>"," ",m.group(1))
        t=html.unescape(re.sub(r"\s+"," ",t)).strip()
        if t: return t
    return Path(filename).stem.replace("_"," ").replace("-"," ").strip().title()
def extract_document_text(path, raw):
    """Extract searchable text; OCR image-only PDF pages and DOCX images when possible."""
    ext=path.suffix.lower()
    chunks=[]
    try:
        if ext==".pdf":
            import fitz
            import pytesseract
            from PIL import Image
            import io
            doc=fitz.open(stream=raw,filetype="pdf")
            for page in doc:
                txt=page.get_text("text") or ""
                if len(txt.strip())<40:
                    pix=page.get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False)
                    img=Image.open(io.BytesIO(pix.tobytes("png")))
                    try: txt += "\n"+pytesseract.image_to_string(img,lang="eng+hin")
                    except Exception: txt += "\n"+pytesseract.image_to_string(img,lang="eng")
                chunks.append(txt)
        elif ext==".docx":
            from docx import Document
            import io, zipfile
            from PIL import Image
            import pytesseract
            doc=Document(io.BytesIO(raw))
            chunks.extend(p.text for p in doc.paragraphs)
            for table in doc.tables:
                for row in table.rows:
                    chunks.append(" | ".join(cell.text for cell in row.cells))
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                for name in z.namelist():
                    if name.startswith("word/media/"):
                        try:
                            img=Image.open(io.BytesIO(z.read(name)))
                            chunks.append(pytesseract.image_to_string(img,lang="eng+hin"))
                        except Exception:
                            continue
    except Exception as exc:
        raise RuntimeError(type(exc).__name__) from None
    return "\n".join(chunks)
def scan_bytes(data):
    return [label for label,rx in SECRET_PATTERNS if rx.search(data)]
def write_wrapper(slug_name,title,app_rel,mature):
    dest=COLLECTIONS/slug_name/"index.html"; dest.parent.mkdir(parents=True,exist_ok=True)
    robots='<meta name="robots" content="noindex,nofollow">' if mature else '<meta name="robots" content="index,follow">'
    gate=""
    if mature:
        gate="""<section id="age-gate" class="age-gate" role="dialog" aria-modal="true" aria-labelledby="age-title"><div><p class="kicker">Mature collection</p><h1 id="age-title">Adults only</h1><p>This collection may contain mature themes and is intended for readers aged 18 or over.</p><button id="age-confirm" type="button">I am 18 or older — continue</button><a href="../../index.html">Return to the library</a></div></section><script>try{if(localStorage.getItem('rr-age-confirmed')==='yes')document.getElementById('age-gate').hidden=true}catch(e){}document.getElementById('age-confirm').addEventListener('click',()=>{try{localStorage.setItem('rr-age-confirmed','yes')}catch(e){}document.getElementById('age-gate').hidden=true})</script>"""
    doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{robots}<meta name="description" content="Original interactive collection: {html.escape(title)}"><title>{html.escape(title)} — The Reading Room</title><link rel="stylesheet" href="../../assets/reading-room.css"><style>.app-frame{{display:block;width:100%;height:calc(100vh - 8rem);min-height:650px;border:0;background:white}}.app-head{{max-width:1200px;margin:auto;padding:1rem 1.25rem;display:flex;justify-content:space-between;gap:1rem;align-items:center}}.age-gate{{position:fixed;inset:0;z-index:10000;background:var(--canvas);display:grid;place-items:center;padding:1.5rem}}.age-gate[hidden]{{display:none}}.age-gate>div{{max-width:34rem;background:var(--surface);border:1px solid var(--line);padding:2rem}}.age-gate button{{display:block;margin:1rem 0;padding:.7rem 1rem;background:var(--accent);color:white;border:0;cursor:pointer}}</style></head><body><header class="app-head"><a href="../../index.html">← The Reading Room</a><strong>{html.escape(title)}</strong><a href="../../apps/{app_rel}" target="_blank" rel="noopener">Open original view ↗</a></header><main><iframe class="app-frame" title="{html.escape(title)}" src="../../apps/{app_rel}"></iframe></main>{gate}</body></html>'''
    dest.write_text(doc,encoding="utf-8")
    return dest.relative_to(SITE).as_posix()
def main():
    for p in (SITE,APPS,COLLECTIONS,DATA): p.mkdir(parents=True,exist_ok=True)
    items=[]; withheld=[]; issues=[]; seen=set()
    source_files=sorted(p for p in ROOT.iterdir() if p.is_file() and p.suffix.lower() in {".html",".pdf",".docx",".txt",".pine"})
    for p in source_files:
        raw=p.read_bytes()
        ext=p.suffix.lower()
        scan_data=raw
        if ext in {".pdf",".docx"}:
            try:
                extracted=extract_document_text(p,raw)
                scan_data += b"\n"+extracted.encode("utf-8",errors="ignore")
                if not extracted.strip():
                    withheld.append({"file":p.name,"reason":"no extractable text; OCR/content review required"})
                    continue
            except Exception as exc:
                withheld.append({"file":p.name,"reason":"document extraction failed ("+str(exc)+"); held for manual review"})
                continue
        hits=scan_bytes(scan_data)
        if hits:
            withheld.append({"file":p.name,"reason":"sensitive-data scan: "+", ".join(hits)})
            continue
        if ext==".html":
            source=raw.decode("utf-8",errors="replace")
            name=slug(p.name)
            if name in seen: name += "-"+hashlib.sha1(p.name.encode()).hexdigest()[:6]
            seen.add(name)
            mature=bool(MATURE.search(p.name) or re.search(r"(?i)adult|18\+|mature",source[:12000]))
            app_name=name+".html"
            app_dest=APPS/app_name
            # Preserve app source byte-for-byte for ordinary apps. Mature copies gain only noindex metadata.
            app_dest.write_bytes(raw)
            if mature:
                try:
                    text=app_dest.read_text(encoding="utf-8")
                    if re.search(r"<head[^>]*>",text,re.I):
                        text=re.sub(r"(<head[^>]*>)",r'\1<meta name="robots" content="noindex,nofollow">',text,count=1,flags=re.I)
                    app_dest.write_text(text,encoding="utf-8")
                except UnicodeDecodeError:
                    withheld.append({"file":p.name,"reason":"mature HTML could not be safely tagged noindex"}); app_dest.unlink(missing_ok=True); continue
            title=title_from_html(source,p.name)
            href=write_wrapper(name,title,app_name,mature)
            items.append({"title":title,"description":"Open the preserved original interactive collection.","category":category(p.name),"kind":"Interactive HTML","href":href,"mature":mature,"searchText":searchable_text(source)})
        elif ext in {".pdf",".docx"}:
            # Rights and personal-data review cannot be inferred from a filename. No document is published
            # until its exact source path is approved in a human-reviewed policy manifest.
            withheld.append({"file":p.name,"reason":"document held for manual copyright and content review"})
        elif ext in {".txt",".pine"}:
            # Code and text source files are not published as-is until reviewed; keep a clear audit trail.
            withheld.append({"file":p.name,"reason":"text/code held for manual content and sensitive-data review"})
    items.sort(key=lambda x:(x["category"],x["title"].casefold()))
    (DATA/"catalog.json").write_text(json.dumps({"generated":date.today().isoformat(),"items":items},ensure_ascii=False,indent=2),encoding="utf-8")
    report=["# Publishing review","",f"Build date: {date.today().isoformat()}","",f"Published interactive HTML collections: **{len(items)}**","",f"Withheld source files: **{len(withheld)}**",""]
    for x in withheld: report.append(f"- **{x['file']}** — {x['reason']}")
    report += ["","## Notes","- Withheld filenames are reported without reproducing matched values or document contents.","- PDF/DOCX and text/code files require human review before allowlisting.","- Original root-level source files are never modified.",""]
    REPORT.write_text("\n".join(report),encoding="utf-8")
    report_html="<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><meta name='robots' content='noindex,nofollow'><title>Publishing review — The Reading Room</title><link rel='stylesheet' href='assets/reading-room.css'></head><body><main class='intro'><p class='kicker'>Internal publishing record</p><h1>Content review<br><em>and exclusions.</em></h1><p class='intro-copy'>Build date: "+date.today().isoformat()+"</p><p>Published interactive HTML collections: <strong>"+str(len(items))+"</strong></p><p>Withheld source files: <strong>"+str(len(withheld))+"</strong></p><ul>"+''.join("<li><strong>"+html.escape(x['file'])+"</strong> — "+html.escape(x['reason'])+"</li>" for x in withheld)+"</ul><p>Matched sensitive values are never included in this report. Original source files remain unchanged.</p><a href='./'>Return to the library</a></main></body></html>"
    (SITE/"review-report.html").write_text(report_html,encoding="utf-8")
    (SITE/"robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://piyushimself.github.io/files/sitemap.xml\n",encoding="utf-8")
    urls=["https://piyushimself.github.io/files/","https://piyushimself.github.io/files/404.html"]+[f"https://piyushimself.github.io/files/{x['href']}" for x in items if not x["mature"]]
    (SITE/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f"<url><loc>{html.escape(u)}</loc></url>" for u in urls)+"</urlset>",encoding="utf-8")
    print(f"Build complete: {len(items)} HTML collections; {len(withheld)} files withheld.")
if __name__=="__main__": main()
