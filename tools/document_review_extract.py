#!/usr/bin/env python3
"""Extract redacted review copies of withheld source documents for temporary QA."""
from __future__ import annotations
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
from collections import defaultdict
import hashlib, json, re

import fitz
import pytesseract
from PIL import Image
from docx import Document

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"document-review-redacted"
OUT.mkdir(exist_ok=True)
EXTS={".pdf",".docx",".txt",".pine"}
EXCLUDE={"requirements-build.txt"}

REDACTIONS=[
 ("private_key",re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z0-9 ]*PRIVATE KEY-----",re.I)),
 ("email",re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",re.I)),
 ("aws_access_key",re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
 ("github_token",re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
 ("jwt",re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
 ("aadhaar_like",re.compile(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b")),
 ("pan_like",re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b",re.I)),
 ("ssn_like",re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
 ("credential_assignment",re.compile(r"(?i)\b(password|passwd|secret|api[_ -]?key|access[_ -]?token)\b\s*[:=]\s*[^\s,;]{4,}")),
 ("labelled_phone",re.compile(r"(?i)\b(phone|mobile|telephone|tel)\s*[:#-]?\s*\+?[\d\s().-]{8,}\d")),
 ("private_ip",re.compile(r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b")),
]
RIGHTS={
 "copyright_notice":re.compile(r"\b(copyright|©|all rights reserved)\b",re.I),
 "license_reference":re.compile(r"\b(creative commons|cc[- ]by|licensed under|mit license|apache license|gnu general public license|gpl)\b",re.I),
 "public_domain_reference":re.compile(r"\b(public domain|out of copyright|no copyright)\b",re.I),
 "publisher_or_isbn":re.compile(r"\b(published by|publisher|isbn|issn)\b",re.I),
 "author_reference":re.compile(r"\b(author|written by|compiled by|curated by)\b",re.I),
}

def redact(text):
    counts={}
    for label,pattern in REDACTIONS:
        text,n=pattern.subn(f"[REDACTED:{label}]",text)
        if n: counts[label]=n
    return text,counts

def docx_text(raw):
    doc=Document(BytesIO(raw))
    chunks=[]
    for p in doc.paragraphs:
        if p.text.strip(): chunks.append(p.text)
    for ti,table in enumerate(doc.tables,1):
        chunks.append(f"[TABLE {ti}]")
        for row in table.rows:
            chunks.append(" | ".join(cell.text.replace("\n"," / ").strip() for cell in row.cells))
    for si,section in enumerate(doc.sections,1):
        for label,part in (("HEADER",section.header),("FOOTER",section.footer)):
            values=[p.text for p in part.paragraphs if p.text.strip()]
            if values: chunks.append(f"[{label} {si}]"); chunks.extend(values)
    image_count=0
    ocr_errors=[]
    try:
        with ZipFile(BytesIO(raw)) as z:
            for name in z.namelist():
                if name.startswith("word/media/") and not name.endswith("/"):
                    image_count+=1
                    try:
                        im=Image.open(BytesIO(z.read(name))).convert("RGB")
                        value=pytesseract.image_to_string(im,lang="eng+hin")
                        if value.strip(): chunks.append(f"[OCR IMAGE {name}]\n{value}")
                    except Exception as e: ocr_errors.append(f"{name}: {e}")
    except Exception as e: ocr_errors.append(str(e))
    props=doc.core_properties
    metadata={k:bool(getattr(props,k,None)) for k in ("title","subject","author","last_modified_by","keywords","comments")}
    return "\n\n".join(chunks),{"paragraphs":len(doc.paragraphs),"tables":len(doc.tables),"embedded_images":image_count,"ocr_errors":ocr_errors,"metadata_fields_present":metadata}

def pdf_text(raw):
    pdf=fitz.open(stream=raw,filetype="pdf")
    chunks=[]; ocr_pages=[]; errors=[]
    for index,page in enumerate(pdf):
        text=page.get_text("text") or ""
        images=page.get_images(full=True)
        if len(text.strip())<100 or (images and len(text.strip())<500):
            try:
                pix=page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
                im=Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
                ocr=pytesseract.image_to_string(im,lang="eng+hin")
                if len(ocr.strip())>len(text.strip()):
                    text=ocr
                    ocr_pages.append(index+1)
            except Exception as e: errors.append({"page":index+1,"error":str(e)})
        chunks.append(f"===== PAGE {index+1} =====\n{text.strip()}")
    meta=pdf.metadata or {}
    metadata={k:bool(meta.get(k)) for k in ("title","author","subject","keywords","creator","producer")}
    return "\n\n".join(chunks),{"pages":len(pdf),"ocr_pages":ocr_pages,"ocr_errors":errors,"metadata_fields_present":metadata}

def safe_name(name):
    value=re.sub(r"[^a-z0-9]+","-",Path(name).stem.lower()).strip("-")
    return (value[:90] or "document")+".txt"

def main():
    sources=sorted(p for p in ROOT.iterdir() if p.is_file() and p.suffix.lower() in EXTS and p.name not in EXCLUDE)
    seen=defaultdict(list); records=[]; errors=[]
    for path in sources:
        try:
            raw=path.read_bytes()
            digest=hashlib.sha256(raw).hexdigest()
            seen[digest].append(path.name)
            meta={"file":path.name,"extension":path.suffix.lower(),"bytes":len(raw),"sha256":digest}
            if path.suffix.lower()==".pdf":
                content,extra=pdf_text(raw); meta.update(extra)
            elif path.suffix.lower()==".docx":
                content,extra=docx_text(raw); meta.update(extra)
            else:
                content=raw.decode("utf-8-sig",errors="replace")
                meta.update({"lines":len(content.splitlines()),"pages":None})
            content,redactions=redact(content)
            rights={k:len(v.findall(content)) for k,v in RIGHTS.items()}
            meta.update({"characters":len(content),"words":len(re.findall(r"\S+",content)),"redactions":redactions,"rights_markers":{k:v for k,v in rights.items() if v}})
            if not content.strip(): meta["extraction_warning"]="No text extracted; manual visual inspection required"
            outpath=OUT/safe_name(path.name)
            outpath.write_text(f"# Redacted review copy: {path.name}\n\n{content}\n",encoding="utf-8")
            meta["review_text_file"]=outpath.name
            records.append(meta)
        except Exception as e:
            errors.append({"file":path.name,"error":str(e)})
            records.append({"file":path.name,"extension":path.suffix.lower(),"extraction_error":str(e)})
    duplicate_groups=[names for names in seen.values() if len(names)>1]
    manifest={"source_count":len(sources),"records":records,"exact_duplicate_groups":duplicate_groups,"errors":errors,"notice":"Redacted temporary review copies only. Not approved for publication. Rights status remains unverified until evidence is reviewed."}
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf-8")
    lines=["# Temporary redacted document review extract","",f"- Source files processed: {len(sources)}",f"- Exact duplicate groups: {len(duplicate_groups)}",f"- Extraction errors: {len(errors)}","- Publication rights: **not verified**; no file is approved by this extraction.","- Contact-like values and common credentials are redacted in the review copies.","","## Per-file extraction inventory",""]
    for r in records:
        lines.append(f"- **{r['file']}** — {r.get('pages',r.get('lines','n/a'))} pages/lines; {r.get('words',0)} words; OCR pages: {len(r.get('ocr_pages',[]))}; redactions: {sum(r.get('redactions',{}).values())}; rights markers: {', '.join(r.get('rights_markers',{}).keys()) or 'none detected'}; {'ERROR: '+r['extraction_error'] if r.get('extraction_error') else r.get('extraction_warning','')}")
    if duplicate_groups:
        lines+=["","## Exact duplicates",""]+[f"- {', '.join(group)}" for group in duplicate_groups]
    if errors:
        lines+=["","## Extraction errors",""]+[f"- {e['file']}: {e['error']}" for e in errors]
    (OUT/"summary.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    (OUT/"README.txt").write_text("Temporary redacted working copies for internal review only. Do not publish these extracted texts. The source files remain withheld pending content, privacy and publication-rights review.\n",encoding="utf-8")
    print("\n".join(lines))
    return 0
if __name__=="__main__": raise SystemExit(main())
