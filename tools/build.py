#!/usr/bin/env python3
"""Fail-closed builder for The Reading Room. Source files are never modified."""
from __future__ import annotations
import hashlib, html, json, re, shutil, sys
from datetime import date
from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"site"
APPS=SITE/"apps"
COLLECTIONS=SITE/"collections"
DATA=SITE/"data"
REPORT=ROOT/"PUBLISHING-REVIEW.md"
EXCLUDE={".git",".github","site","tools","__pycache__"}
MATURE=re.compile(r"(?:18\+|18-plus|adult[-_ ](?:manga|manhwa|comics?|romance)|taboo|transgressive|dark[-_ ]ink|manhwa300|manhwa[-_ ]300|top500[-_ ]adult|forbidden[-_ ]pages|sensual[-_ ]mood|hentai|ecchi|nsfw|porn(?:ography)?|erotic|sexually explicit|explicit sexual content)",re.I)
SECRET_PATTERNS=[
 ("private key",re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
 ("AWS access key",re.compile(rb"\bAKIA[0-9A-Z]{16}\b")),
 ("GitHub token",re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
 ("generic API token",re.compile(rb"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{20,}")),
 ("bearer credential",re.compile(rb"(?i)authorization\s*[:=]\s*bearer\s+[A-Za-z0-9._~+/=-]{20,}")),
 ("email address",re.compile(rb"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",re.I)),
 ("phone-like number",re.compile(rb"(?<!\d)(?:(?:\+|00)91[\s-]?|0)?[6-9]\d{9}(?!\d)|(?<!\d)\+[1-9](?:[\s()-]*\d){8,13}(?!\d)|(?<!\d)[6-9]\d{4}[\s-]\d{5}(?!\d)")),
 ("Indian Aadhaar-like identifier",re.compile(rb"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b")),
 ("Indian PAN-like identifier",re.compile(rb"\b[A-Z]{5}\d{4}[A-Z]\b",re.I)),
 ("US SSN-like identifier",re.compile(rb"\b\d{3}-\d{2}-\d{4}\b")),
 ("password assignment",re.compile(rb"(?i)password\s*[:=]\s*['\"][^'\"]{8,}")),
 ("JWT-like token",re.compile(rb"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
 ("Slack token",re.compile(rb"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
 ("GitLab token",re.compile(rb"\bglpat-[A-Za-z0-9_-]{20,}\b")),
 ("private/internal URL",re.compile(rb"(?i)\bhttps?://(?:localhost|127(?:\.\d{1,3}){3}|10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2}|[A-Za-z0-9.-]+\.internal)(?::\d+)?[^\s]*")),
 ("home-address label",re.compile(rb"(?i)(?:home|residential|street)\s+address\s*[:=]")),
]
def slug(s):
    out=re.sub(r"[^a-z0-9]+","-",Path(s).stem.lower()).strip("-")
    return out or hashlib.sha1(s.encode()).hexdigest()[:10]
def category(name):
    # Explicit exceptions keep subject assignment deterministic; keyword fallbacks are conservative.
    n=Path(name).name.lower()
    explicit={
      "global_kids_books_complete_guide.pdf":"Family",
      "global_kids_reading_guide_final (1).pdf":"Family",
      "three_year_old_reading_guide (1).pdf":"Family",
      "world_stories_3yearold_guide.pdf":"Family",
      "1000_greatest_fictional_books.pdf":"Reading & Literature",
      "aag_ki_kavitayen.pdf":"Reading & Literature",
      "a_filmmakers_reading_list.pdf":"Reading & Literature",
      "cybersecurity_stories_for_your_teams.pdf":"Security",
      "ath - pine.txt":"Security",
      "crypto_trend_rider_4h.pine":"Security",
      "meditation_on_death.pdf":"Learning",
      "blackout_poetry_tutorial.html":"Reading & Literature",
      "life-fiction-curriculum.html":"Reading & Literature",
      "asian_books_curriculum.pdf":"Reading & Literature",
      "free_art_resource_library.docx":"Art",
      "watercolour_tasks (1).html":"Art",
      "bob_ross_complete_guide.html":"Art",
      "free-art-resources.html":"Art",
      "political-comics-list.html":"Manga & Comics",
      "qwen_html_20260604_f25nf6z8p.html":"Manga & Comics",
      "anime-manga-values-curriculum.html":"Learning",
      "human-development-curriculum.html":"Learning",
      "living-curriculum-2026.html":"Learning",
      "memento-mori-course.pdf":"Learning",
      "sen-mood-movies.html":"Cinema",
    }
    if n in explicit: return explicit[n]
    if any(x in n for x in ("generator","diary","tracker","typewriter","journal")): return "Interactive tools"
    if any(x in n for x in ("cybersecurity","security","crypto_trend","ath - pine")): return "Security"
    if any(x in n for x in ("kid","child","three_year","world_stories","reading_guide","global_kids")): return "Family"
    if any(x in n for x in ("manga","manhwa","anime","comic")): return "Manga & Comics"
    if any(x in n for x in ("film","cinema","movie")): return "Cinema"
    if any(x in n for x in ("poetry","poem","kavit","fiction","literature","book","reading_list","asian_books")): return "Reading & Literature"
    if any(x in n for x in ("art","watercolour","collage","bob_ross","masters_of_art")): return "Art"
    if any(x in n for x in ("curriculum","course","development","prompt","thinker","inspiration","meditation","memento")): return "Learning"
    return "Cross-disciplinary"
def searchable_text(raw):
    raw=re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>"," ",raw)
    raw=re.sub(r"(?s)<[^>]+>"," ",raw)
    return html.unescape(re.sub(r"\s+"," ",raw)).strip()[:250000]
def title_from_html(raw, filename):
    source_stem=Path(filename).stem.lower().replace("_","-").replace(" ","-")
    if source_stem=="manhwa300": return "300 Adult Het Romance Manhwa — Editorial Atlas"
    if source_stem=="manhwa-300-filter-app": return "300 Adult Het Romance Manhwa — Searchable Index"
    m=re.search(r"<title[^>]*>(.*?)</title>",raw,re.I|re.S)
    if m:
        t=re.sub(r"<[^>]+>"," ",m.group(1))
        t=html.unescape(re.sub(r"\s+"," ",t)).strip()
        if t: return t
    # When an interactive source omits <title>, use its visible H1 before falling
    # back to a filename-derived label. This prevents raw filenames becoming titles.
    h=re.search(r"<h1\b[^>]*>(.*?)</h1>",raw,re.I|re.S)
    if h:
        t=html.unescape(re.sub(r"\s+"," ",h.group(1))).strip()
        t=html.unescape(re.sub(r"\\s+"," ",t)).strip()
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
def shell_header(title):
    return """<header class="rr-shell-header"><a class="rr-shell-brand" href="../../index.html">THE READING ROOM <small>PERSONAL LIBRARY</small></a><nav class="rr-shell-tools" aria-label="Library navigation"><a href="../../index.html">Home</a><details class="rr-nav-menu"><summary>Browse collections</summary><div class="rr-nav-panel"><label class="sr-only" for="rr-nav-search">Search collections</label><input id="rr-nav-search" type="search" placeholder="Find a collection…"><nav id="rr-nav-links" class="rr-nav-links" aria-label="All collections"></nav></div></details><a id="rr-prev" href="#" hidden>← Previous</a><a id="rr-next" href="#" hidden>Next →</a><button id="rr-theme-toggle" type="button">Dark mode</button><label class="rr-font-label" for="rr-font-family">Font</label><select id="rr-font-family" aria-label="Reader font"><option value="system">System</option><option value="serif">Serif</option><option value="mono">Mono</option></select><button id="rr-text-smaller" type="button" aria-label="Decrease text size">A−</button><button id="rr-text-larger" type="button" aria-label="Increase text size">A+</button></nav></header>"""
def enhance_app(path, category_name):
    text=path.read_text(encoding="utf-8")
    # Repair one malformed author string in the imported Qwen manga data, only in the generated copy.
    text=text.replace('author: Ryousuke Takeuchi & Takeshi Obata",', 'author: "Ryousuke Takeuchi & Takeshi Obata",')
    # Repair the known unquoted author value in the generated copy only.
    text=text.replace("author: Ryousuke Takeuchi & Takeshi Obata, year: 2014", "author: \"Ryousuke Takeuchi & Takeshi Obata\", year: 2014")
    # Repair a malformed legacy style terminator in the generated copy only.
    # Qwen's source has one opening <style> and a typo "</ thead>" immediately
    # before <body>; browsers then treat the entire app as CSS and render blank.
    style_opens=len(re.findall(r"<style\b",text,re.I))
    style_closes=len(re.findall(r"</style\s*>",text,re.I))
    if style_opens==style_closes+1:
        malformed=re.search(r"</\s*thead\s*>\s*(?=<body\b)",text,re.I)
        if malformed:
            text=text[:malformed.start()]+"</style>"+text[malformed.end():]
    # Correct verified catalogue-count mismatches only in generated copies.
    # Keep the original root-level HTML uploads byte-for-byte unchanged.
    if path.name == "big-library.html":
        corrections = (
            ('{key:"essential_100",label:"Essential 100",type:"film",part:"PART I · SEC 01",title:"100 Essential Films",desc:"100 films that demand to be seen - 30 genres, 28 countries, nearly a century of image-making.",filterType:"film"},', '{key:"essential_100",label:"Essential 98",type:"film",part:"PART I · SEC 01",title:"98 Essential Films",desc:"98 films that demand to be seen - 30 genres, 28 countries, nearly a century of image-making.",filterType:"film"},'),
            ('{key:"biographical",label:"Biog. Films",type:"film",part:"PART I · SEC 02",title:"200 Biographical Films",desc:"Lives vividly told - artists, musicians, scientists, rebels. Organised by subject category.",filterType:"film_bio"},', '{key:"biographical",label:"Biog. Films",type:"film",part:"PART I · SEC 02",title:"190 Biographical Films",desc:"Lives vividly told - artists, musicians, scientists, rebels. Organised by subject category.",filterType:"film_bio"},'),
            ('{key:"world_cinema",label:"Open Worlds",type:"film",part:"PART I · SEC 03",title:"A Life Worth Living - 500 Films",desc:"Cinema as philosophy made visible - 500 films from every inhabited continent and seven decades.",filterType:"film_world"},', '{key:"world_cinema",label:"World Cinema 563",type:"film",part:"PART I · SEC 03",title:"A Life Worth Living - 563 Films",desc:"Cinema as philosophy made visible - 563 films from every inhabited continent and seven decades.",filterType:"film_world"},'),
            ('{key:"curated_900",label:"900 Films",type:"film",part:"PART I · SEC 05",title:"900 Curated World Cinema",desc:"World Cinema Masterpieces, Sensual and Mood Cinema, Explicit Erotic Art Cinema - with IMDb scores.",filterType:"film_900"},', '{key:"curated_900",label:"Curated 835",type:"film",part:"PART I · SEC 05",title:"835 Curated World Cinema",desc:"World Cinema Masterpieces, Sensual and Mood Cinema, Explicit Erotic Art Cinema - with IMDb scores.",filterType:"film_900"},'),
            ('{key:"movie_enc",label:"Encyclopedia",type:"film",part:"PART I · SEC 07",title:"Complete Movie Encyclopedia",desc:"647 films with IMDb, Rotten Tomatoes, streaming availability, and editorial rating.",filterType:"film_enc"},', '{key:"movie_enc",label:"Encyclopedia 649",type:"film",part:"PART I · SEC 07",title:"Complete Movie Encyclopedia",desc:"649 films with IMDb, Rotten Tomatoes, streaming availability, and editorial rating.",filterType:"film_enc"},'),
            ('{key:"books_1000",label:"1000 Books",type:"book",part:"PART III · SEC 12",title:"1000 Greatest Fictional Books",desc:"From Ancient Greek to contemporary global fiction, organised by literary tradition.",filterType:"book"},', '{key:"books_1000",label:"Books 484",type:"book",part:"PART III · SEC 12",title:"484 Greatest Fictional Books",desc:"From Ancient Greek to contemporary global fiction, organised by literary tradition.",filterType:"book"},'),
            ('{key:"music",label:"500 Music",type:"music",part:"PART IV · SEC 16",title:"A Life Worth Living - 500 Albums",desc:"Essential albums spanning jazz, classical, world music, folk, and beyond.",filterType:"music"},', '{key:"music",label:"Music 266",type:"music",part:"PART IV · SEC 16",title:"A Life Worth Living - 266 Albums",desc:"Essential albums spanning jazz, classical, world music, folk, and beyond.",filterType:"music"},')
        )
        for old, new in corrections:
            if old not in text:
                raise RuntimeError("Expected Big Library count line was not found in generated source copy")
            text = text.replace(old, new, 1)
    elif path.name == "film-collection-v8.html":
        text = text.replace("<title>The Complete Film Collection — 1,619 Films</title>", "<title>The Complete Film Collection — 1,629 Films</title>", 1)
        text = text.replace('<span class="result-count" id="resultCount">1,619 films</span>', '<span class="result-count" id="resultCount">1,629 films</span>', 1)
    # Remove remote font dependencies; the reader controls typography locally.
    text=re.sub(r'<link[^>]+(?:fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*>', '', text, flags=re.I)
    text=re.sub(r'@import\s+url\([\'"]?https?://fonts\.googleapis\.com[^)]*\)\s*;?', '', text, flags=re.I)
    additions='<link rel="stylesheet" href="../assets/unified-app.css"><script src="../assets/unified-app.js" defer></script>'
    body_match=re.search(r"<body([^>]*)>",text,re.I)
    if body_match and "data-rr-category" not in body_match.group(1):
        replacement='<body'+body_match.group(1)+' data-rr-category="'+html.escape(category_name,quote=True)+'">'
        text=text[:body_match.start()]+replacement+text[body_match.end():]
    # Resolve head boundaries independently of whether body metadata was already present.
    head_open=re.search(r"<head\b[^>]*>",text,re.I)
    head_close=re.search(r"</head\s*>",text,re.I)
    if head_close:
        if not head_open:
            # Repair a stray closing head by creating a matching opening tag.
            text=text[:head_close.start()]+"<head>"+text[head_close.start():]
            head_open=re.search(r"<head\b[^>]*>",text,re.I)
            head_close=re.search(r"</head\s*>",text,re.I)
        if "unified-app.css" not in text and head_close:
            text=text[:head_close.start()]+additions+text[head_close.start():]
    elif head_open:
        # Some imported files have an opening <head> but omit </head>.
        # Add the shared assets inside that head, then close it before <body>.
        if "unified-app.css" not in text:
            text=text[:head_open.end()]+additions+text[head_open.end():]
        body_match=re.search(r"<body\b[^>]*>",text,re.I)
        if body_match:
            text=text[:body_match.start()]+"</head>"+text[body_match.start():]
        else:
            html_close=re.search(r"</html\s*>",text,re.I)
            if html_close: text=text[:html_close.start()]+"</head>"+text[html_close.start():]
    else:
        match=re.search(r"<html[^>]*>",text,re.I)
        if match:
            text=text[:match.end()]+"<head>"+additions+"</head>"+text[match.end():]
        else:
            text="<!doctype html><html><head>"+additions+"</head><body>"+text+"</body></html>"
    # Inject the shared filter disclosure independently of the theme layer, including
    # imported apps that already reference unified-app.css.
    if "filter-disclosure.js" not in text:
        head_close=re.search(r"</head\s*>",text,re.I)
        if head_close:
            text=text[:head_close.start()]+'<script src="../assets/filter-disclosure.js" defer></script>'+text[head_close.start():]
    # Add responsive metadata after normalizing even non-standard documents without a <head>.
    if not re.search(r'<meta\b[^>]*name=["\']viewport["\']', text, re.I):
        text=re.sub(r'<head\b[^>]*>', lambda m: m.group(0)+'<meta name="viewport" content="width=device-width, initial-scale=1.0">', text, count=1, flags=re.I)
    if "<title" not in text.lower():
        app_title=html.escape(title_from_html(text, path.name))
        head_start=text.lower().find("<head")
        head_open_end=text.find(">",head_start) if head_start >= 0 else -1
        if head_open_end < 0: raise RuntimeError("Generated app has no opening head tag for title fallback")
        text=text[:head_open_end+1]+"<title>"+app_title+"</title>"+text[head_open_end+1:]
    # Qwen's imported palette uses low-contrast muted colours and dark chips.
    # Repair the generated copy only, retaining its original layout and gradient identity.
    if "100 Manga That Will Change How You Think" in text and 'id="rr-qwen-contrast"' not in text:
        qwen_css="""<style id="rr-qwen-contrast">
header h1{background-image:linear-gradient(90deg,#9f3344,#176e70)!important;-webkit-text-fill-color:transparent!important;color:var(--rr-ink)!important}
header p,.status-bar,.rank,.meta,.excerpt,.modal .subtitle,.empty{color:var(--rr-muted)!important}
.status-bar{width:100%!important;gap:1rem!important}
.chip{background:var(--rr-raised)!important;color:var(--rr-ink)!important;border-color:var(--rr-line)!important}
.chip.active{background:var(--rr-accent)!important;color:#fff!important;border-color:var(--rr-accent)!important}
.tag{background:var(--rr-raised)!important;color:var(--rr-accent)!important;border-color:var(--rr-line)!important}
.rating{color:#805500!important}
:root[data-theme=dark] header h1{background-image:linear-gradient(90deg,#ff9a9e,#72d8d0)!important}
:root[data-theme=dark] .chip.active{color:#0b1627!important}
:root[data-theme=dark] .rating{color:#ffd166!important}
.chip:focus-visible,.page-btn:focus-visible,.card:focus-visible{outline:3px solid var(--rr-focus)!important;outline-offset:2px!important}
</style>"""
        head_end=text.lower().find("</head>")
        if head_end < 0:
            raise RuntimeError("Qwen generated app has no closing head tag for contrast repair")
        text=text[:head_end]+qwen_css+text[head_end:]
    path.write_text(text,encoding="utf-8")
def inject_app_age_gate(path):
    """Add a same-origin 18+ self-declaration gate and noindex metadata to the app itself."""
    text=path.read_text(encoding="utf-8")
    # Direct app URLs must be noindex too; wrapper metadata does not apply inside an iframe.
    robots=re.search(r"""<meta\b[^>]*\bname=["']robots["'][^>]*>""",text,re.I)
    if robots:
        tag=robots.group(0)
        if re.search(r"""\bcontent\s*=""",tag,re.I):
            tag=re.sub(r"""\bcontent\s*=\s*(["']).*?\1""",'content="noindex,nofollow"',tag,count=1,flags=re.I)
        else:
            tag=tag[:-1]+' content="noindex,nofollow">'
        text=text[:robots.start()]+tag+text[robots.end():]
    else:
        head_open=re.search(r"""<head\b[^>]*>""",text,re.I)
        if head_open:
            meta='<meta name="robots" content="noindex,nofollow">'
            text=text[:head_open.end()]+meta+text[head_open.end():]
    if "rr-app-age-gate" in text:
        path.write_text(text,encoding="utf-8")
        return
    css="""<style id="rr-app-age-style">
#rr-app-age-gate{position:fixed!important;inset:0!important;z-index:2147483647!important;display:grid!important;place-items:center!important;padding:1.25rem!important;background:var(--rr-canvas,#f3f6fb)!important;color:var(--rr-ink,#172b45)!important;font:inherit!important}
#rr-app-age-gate[hidden]{display:none!important}
#rr-app-age-gate .rr-app-age-card{box-sizing:border-box!important;width:min(100%,34rem)!important;max-width:34rem!important;padding:clamp(1.4rem,4vw,2.2rem)!important;background:var(--rr-surface,#fff)!important;color:var(--rr-ink,#172b45)!important;border:1px solid var(--rr-line,#d7e0ec)!important;border-radius:14px!important;box-shadow:0 24px 70px rgba(0,0,0,.18)!important}
#rr-app-age-gate .rr-age-kicker{margin:0 0 .6rem!important;color:var(--rr-accent,#2868b2)!important;font-size:.72rem!important;font-weight:700!important;letter-spacing:.12em!important;text-transform:uppercase!important}
#rr-app-age-gate h1{margin:0 0 .75rem!important;color:var(--rr-ink,#172b45)!important;font-size:clamp(1.6rem,4vw,2.2rem)!important;line-height:1.15!important}
#rr-app-age-gate p{margin:0 0 1rem!important;color:var(--rr-muted,#526984)!important;line-height:1.65!important}
#rr-app-age-gate button{display:inline-flex!important;align-items:center!important;justify-content:center!important;min-height:44px!important;padding:.7rem 1rem!important;border:0!important;border-radius:8px!important;background:var(--rr-accent,#2868b2)!important;color:#fff!important;font:inherit!important;font-weight:700!important;cursor:pointer!important}
#rr-app-age-gate a{display:inline-block!important;margin-left:1rem!important;color:var(--rr-accent,#2868b2)!important;text-decoration:underline!important}
</style>"""
    gate="""<section id="rr-app-age-gate" role="dialog" aria-modal="true" aria-labelledby="rr-app-age-title">
<div class="rr-app-age-card"><p class="rr-age-kicker">Mature collection · 18+</p><h1 id="rr-app-age-title">Adults only</h1><p>This collection may contain mature themes and is intended for readers aged 18 or over. This is a self-declaration prompt, not identity or age verification.</p><button id="rr-app-age-confirm" type="button" autofocus>I am 18 or older — continue</button><a href="../index.html">Return to The Reading Room</a></div></section>
<script>(function(){const gate=document.getElementById('rr-app-age-gate');const hide=()=>{gate.hidden=true;};try{if(localStorage.getItem('rr-age-confirmed')==='yes')hide();}catch(e){}document.getElementById('rr-app-age-confirm').addEventListener('click',()=>{try{localStorage.setItem('rr-age-confirmed','yes');}catch(e){}hide();});window.addEventListener('storage',e=>{if(e.key==='rr-age-confirmed'&&e.newValue==='yes')hide();});window.addEventListener('message',e=>{if(e.data&&e.data.type==='rr-age-confirmed')hide();});})();</script>"""
    head=re.search(r"</head\s*>",text,re.I)
    if head: text=text[:head.start()]+css+text[head.start():]
    body=re.search(r"</body\s*>",text,re.I)
    if body: text=text[:body.start()]+gate+text[body.start():]
    else: text+=gate
    path.write_text(text,encoding="utf-8")

def write_article(slug_name,title,source,mature,category_name):
    soup=BeautifulSoup(source,"html.parser")
    body=soup.body or soup
    for node in body.find_all(["script","style","noscript","iframe","svg"]):
        node.decompose()
    allowed={"main","article","section","header","footer","nav","h1","h2","h3","h4","p","ul","ol","li","blockquote","table","thead","tbody","tr","th","td","figure","figcaption","img","a","strong","em","b","i","code","pre","hr","br"}
    for tag in list(body.find_all(True)):
        if tag.name=="div":
            block={"h1","h2","h3","h4","p","ul","ol","table","blockquote","section","article","figure"}
            if any(getattr(child,"name",None) in block for child in tag.find_all(recursive=False)):
                tag.unwrap()
            else:
                tag.name="p"
        elif tag.name in {"span","font","center"}:
            tag.unwrap()
        elif tag.name not in allowed:
            tag.unwrap()
        if getattr(tag,"attrs",None) is not None:
            keep={"href","src","alt","colspan","rowspan","scope"}
            tag.attrs={k:v for k,v in tag.attrs.items() if k in keep}
            if tag.name=="a" and tag.get("href","").lower().startswith("javascript:"):
                tag.unwrap()
            if tag.name=="img":
                src=tag.get("src","")
                if src.startswith(("http://","https://")):
                    alt=tag.get("alt","")
                    tag.replace_with(alt if alt else "")
                elif not src:
                    tag.decompose()
    for h in body.find_all("h1"):
        h.name="h2"
    headings=[]
    for h in body.find_all(["h2","h3"]):
        label=" ".join(h.get_text(" ",strip=True).split())
        if not label: continue
        ident=re.sub(r"[^a-z0-9]+","-",label.lower()).strip("-") or "section"
        base=ident; suffix=2
        while any(x.get("id")==ident for x in body.find_all(["h2","h3"])):
            ident=base+"-"+str(suffix); suffix+=1
        h["id"]=ident
        headings.append((ident,label,h.name))
    body_html="".join(str(x) for x in body.contents)
    plain=BeautifulSoup(body_html,"html.parser").get_text(" ",strip=True)
    words=len(re.findall(r"\w+",plain))
    minutes=max(1,round(words/220))
    toc="".join("<li class='"+level+"'><a href='#"+html.escape(i)+"'>"+html.escape(label)+"</a></li>" for i,label,level in headings)
    robots='<meta name="robots" content="noindex,nofollow">' if mature else '<meta name="robots" content="index,follow">'
    gate=""
    if mature:
        gate="""<section id="age-gate" class="age-gate" role="dialog" aria-modal="true" aria-labelledby="age-title"><div><p class="kicker">Mature collection</p><h2 id="age-title">Adults only</h2><p>This collection may contain mature themes and is intended for readers aged 18 or over.</p><button id="age-confirm" type="button">I am 18 or older — continue</button><a href="../../index.html">Return to the library</a></div></section><script>try{if(localStorage.getItem('rr-age-confirmed')==='yes')document.getElementById('age-gate').hidden=true}catch(e){}document.getElementById('age-confirm').addEventListener('click',()=>{try{localStorage.setItem('rr-age-confirmed','yes')}catch(e){}document.getElementById('age-gate').hidden=true;document.querySelector('iframe.app-frame')?.contentWindow.postMessage({type:'rr-age-confirmed'},'*')})</script>"""
    toc_html="<details class='article-toc'><summary>On this page · "+str(len(headings))+" sections</summary><ol>"+toc+"</ol></details>" if headings else ""
    dest=COLLECTIONS/slug_name/"index.html"; dest.parent.mkdir(parents=True,exist_ok=True)
    doc="<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"+robots+"<title>"+html.escape(title)+" — The Reading Room</title><link rel='stylesheet' href='../../assets/reading-room.css'><link rel='stylesheet' href='../../assets/article.css'><link rel='stylesheet' href='../../assets/collection-shell.css'></head><body data-current='collections/"+slug_name+"/index.html' data-category='"+html.escape(category_name,quote=True)+"'>"+shell_header(title)+"<div class='rr-reading-meta'>Reading time · "+str(minutes)+" min</div><main class='article-layout'><article class='reading-article'><p class='kicker'>From the collection</p><h1>"+html.escape(title)+"</h1><div class='article-find'><label for='article-find-input'>Find in this page</label><input id='article-find-input' type='search' placeholder='Find a word or phrase'><button id='article-find-prev' type='button'>Previous</button><button id='article-find-next' type='button'>Next</button><span id='article-find-count' aria-live='polite'></span></div>"+toc_html+"<div class='article-content'>"+body_html+"</div></article></main>"+gate+"<script src=\"../../assets/article-search.js\" defer></script><script src=\"../../assets/collection-shell.js\" defer></script><footer class='site-footer'><a href='../../index.html'>THE READING ROOM</a><p>A personal atlas of stories, images, ideas and useful knowledge.</p><p>Last updated: "+date.today().isoformat()+"</p></footer></body></html>"
    dest.write_text(doc,encoding="utf-8")
    return dest.relative_to(SITE).as_posix(),plain
def write_wrapper(slug_name,title,app_rel,mature,category_name):
    dest=COLLECTIONS/slug_name/"index.html"; dest.parent.mkdir(parents=True,exist_ok=True)
    robots='<meta name="robots" content="noindex,nofollow">' if mature else '<meta name="robots" content="index,follow">'
    gate=""
    if mature:
        gate="""<section id="age-gate" class="age-gate" role="dialog" aria-modal="true" aria-labelledby="age-title"><div><p class="kicker">Mature collection</p><h1 id="age-title">Adults only</h1><p>This collection may contain mature themes and is intended for readers aged 18 or over.</p><button id="age-confirm" type="button">I am 18 or older — continue</button><a href="../../index.html">Return to the library</a></div></section><script>const gate=document.getElementById('age-gate');const hide=()=>{gate.hidden=true;document.querySelector('iframe.app-frame')?.contentWindow.postMessage({type:'rr-age-confirmed'},'*')};try{if(localStorage.getItem('rr-age-confirmed')==='yes')hide()}catch(e){}document.getElementById('age-confirm').addEventListener('click',()=>{try{localStorage.setItem('rr-age-confirmed','yes')}catch(e){}hide()})</script>"""
    doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{robots}<meta name="description" content="Original interactive collection: {html.escape(title)}"><title>{html.escape(title)} — The Reading Room</title><link rel="stylesheet" href="../../assets/reading-room.css"><link rel="stylesheet" href="../../assets/collection-shell.css"><style>.app-frame{{display:block;width:100%;height:calc(100vh - 11rem);min-height:680px;border:0;background:var(--canvas)}}.app-main{{max-width:1600px;margin:0 auto;padding:0 clamp(.5rem,2vw,1.5rem)}}.rr-app-title{{max-width:1500px;margin:.75rem auto;padding:0 clamp(1rem,2vw,1.5rem);font-size:.85rem;color:var(--muted)}}.age-gate{{position:fixed;inset:0;z-index:10000;background:var(--canvas);display:grid;place-items:center;padding:1.5rem}}.age-gate[hidden]{{display:none}}.age-gate>div{{max-width:34rem;background:var(--surface);border:1px solid var(--line);padding:2rem}}.age-gate button{{display:block;margin:1rem 0;padding:.7rem 1rem;background:var(--accent);color:white;border:0;cursor:pointer}}@media(max-width:700px){{.app-frame{{height:78vh;min-height:620px}}}}</style></head><body data-current="collections/{slug_name}/index.html" data-category="{html.escape(category_name,quote=True)}">{shell_header(title)}<p class="rr-app-title"><span>{html.escape(category_name)}</span> · {html.escape(title)} <a href="../../apps/{app_rel}" target="_blank" rel="noopener">Open original view ↗</a></p><main class="app-main"><iframe class="app-frame" title="{html.escape(title)}" src="../../apps/{app_rel}"></iframe></main>{gate}<script src="../../assets/collection-shell.js" defer></script><footer class='site-footer'><a class='wordmark' href='../../index.html'>THE READING ROOM</a><p>A personal atlas of stories, images, ideas and useful knowledge.</p><p>Last updated: {date.today().isoformat()}</p></footer></body></html>'''
    dest.write_text(doc,encoding="utf-8")
    return dest.relative_to(SITE).as_posix()
def main():
    for p in (SITE,APPS,COLLECTIONS,DATA): p.mkdir(parents=True,exist_ok=True)
    items=[]; withheld=[]; issues=[]; seen=set(); seen_content={}; seen_doc_content={}
    source_files=sorted(p for p in ROOT.iterdir() if p.is_file() and p.name!="requirements-build.txt" and p.suffix.lower() in {".html",".pdf",".docx",".txt",".pine"})
    for p in source_files:
        raw=p.read_bytes()
        ext=p.suffix.lower()
        extracted=""
        if ext in {".pdf",".docx"}:
            digest=hashlib.sha256(raw).hexdigest()
            if digest in seen_doc_content:
                withheld.append({"file":p.name,"reason":"exact duplicate document; identical to "+seen_doc_content[digest]+"; review the original once"})
                continue
            seen_doc_content[digest]=p.name
            try:
                extracted=extract_document_text(p,raw)
                if not extracted.strip():
                    withheld.append({"file":p.name,"reason":"no extractable text; OCR/content review required"})
                    continue
            except Exception as exc:
                withheld.append({"file":p.name,"reason":"document extraction failed ("+str(exc)+"); held for manual review"})
                continue
            # Scan extracted document text, not compressed PDF/DOCX bytes.
            scan_data=extracted.encode("utf-8",errors="ignore")
        elif ext==".html":
            # Ignore scripts, styles, SVG path coordinates and markup.
            visible=searchable_text(raw.decode("utf-8",errors="replace"))
            scan_data=visible.encode("utf-8",errors="ignore")
        else:
            scan_data=raw
        hits=scan_bytes(scan_data)
        if ext in {".pdf",".docx"}:
            # Documents stay unpublished until explicit rights/content review.
            reason="document held for manual copyright and content review"
            if hits: reason += "; potential sensitive-data indicators requiring context: "+", ".join(hits)
            withheld.append({"file":p.name,"reason":reason})
            continue
        if hits:
            withheld.append({"file":p.name,"reason":"potential sensitive-data indicators in readable text: "+", ".join(hits)})
            continue
        if ext==".html":
            digest=hashlib.sha256(raw).hexdigest()
            if digest in seen_content:
                withheld.append({"file":p.name,"reason":"duplicate HTML source; identical to "+seen_content[digest]})
                continue
            seen_content[digest]=p.name
            source=raw.decode("utf-8",errors="replace")
            name=slug(p.name)
            if name in seen: name += "-"+hashlib.sha1(p.name.encode()).hexdigest()[:6]
            seen.add(name)
            title=title_from_html(source,p.name)
            # Classify from the collection identity, never incidental words in a large dataset.
            mature=bool(MATURE.search(p.name) or MATURE.search(title))
            interactive=bool(re.search(r"<script\b|<(?:button|input|select|textarea|canvas)\b|\son(?:click|change|submit)\s*=",source,re.I))
            if interactive:
                app_name=name+".html"
                app_dest=APPS/app_name
                app_dest.write_bytes(raw)
                if mature:
                    try:
                        text=app_dest.read_text(encoding="utf-8")
                        if re.search(r"<head[^>]*>",text,re.I):
                            text=re.sub(r"(<head[^>]*>)",r'\1<meta name="robots" content="noindex,nofollow">',text,count=1,flags=re.I)
                        app_dest.write_text(text,encoding="utf-8")
                    except UnicodeDecodeError:
                        withheld.append({"file":p.name,"reason":"mature HTML could not be safely tagged noindex"}); app_dest.unlink(missing_ok=True); continue
                enhance_app(app_dest,category(p.name))
                if mature: inject_app_age_gate(app_dest)
                href=write_wrapper(name,title,app_name,mature,category(p.name))
                kind="Interactive HTML"
                search_text=searchable_text(source)
                description="Open the preserved original interactive collection."
            else:
                href,search_text=write_article(name,title,source,mature,category(p.name))
                kind="Editorial article"
                description="A cleaned, accessible reading edition with a contents guide."
            items.append({"title":title,"description":description,"category":category(p.name),"kind":kind,"href":href,"mature":mature,"searchText":search_text})
        elif ext in {".pdf",".docx"}:
            # Rights and personal-data review cannot be inferred from a filename. No document is published
            # until its exact source path is approved in a human-reviewed policy manifest.
            withheld.append({"file":p.name,"reason":"document held for manual copyright and content review"})
        elif ext in {".txt",".pine"}:
            # Code and text source files are not published as-is until reviewed; keep a clear audit trail.
            withheld.append({"file":p.name,"reason":"text/code held for manual content and sensitive-data review"})
    items.sort(key=lambda x:(x["category"],x["title"].casefold()))
    (DATA/"catalog.json").write_text(json.dumps({"generated":date.today().isoformat(),"items":items},ensure_ascii=False,indent=2),encoding="utf-8")
    report=["# Publishing review","",f"Build date: {date.today().isoformat()}","",f"Published HTML collections: **{len(items)}**","",f"Withheld source files: **{len(withheld)}**",""]
    for x in withheld: report.append(f"- **{x['file']}** — {x['reason']}")
    report += [
        "",
        "## Notes",
        "- Withheld filenames are reported without reproducing matched values or document contents.",
        "- PDF/DOCX and text/code files require human review before allowlisting.",
        "- Exact duplicate documents are identified; review each unique source once.",
        "- Build dependency files are excluded from content review.",
        "- Mature HTML content is scanned across the complete source; both wrapper and direct app URLs show an 18+ self-declaration gate. This is not identity or age verification.",
        "- Original root-level source files are never modified.",
        ""
    ]
    REPORT.write_text("\n".join(report),encoding="utf-8")
    report_html="<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><meta name='robots' content='noindex,nofollow'><title>Publishing review — The Reading Room</title><link rel='stylesheet' href='assets/reading-room.css'></head><body><main class='intro'><p class='kicker'>Internal publishing record</p><h1>Content review<br><em>and exclusions.</em></h1><p class='intro-copy'>Build date: "+date.today().isoformat()+"</p><p>Published HTML collections: <strong>"+str(len(items))+"</strong></p><p>Withheld source files: <strong>"+str(len(withheld))+"</strong></p><ul>"+''.join("<li><strong>"+html.escape(x['file'])+"</strong> — "+html.escape(x['reason'])+"</li>" for x in withheld)+"</ul><p>Matched sensitive values are never included in this report. Original source files remain unchanged.</p><a href='./'>Return to the library</a></main></body></html>"
    (SITE/"review-report.html").write_text(report_html,encoding="utf-8")
    (SITE/"robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://piyushimself.github.io/files/sitemap.xml\n",encoding="utf-8")
    urls=["https://piyushimself.github.io/files/","https://piyushimself.github.io/files/404.html"]+[f"https://piyushimself.github.io/files/{x['href']}" for x in items if not x["mature"]]
    (SITE/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f"<url><loc>{html.escape(u)}</loc></url>" for u in urls)+"</urlset>",encoding="utf-8")
    print(f"Build complete: {len(items)} HTML collections; {len(withheld)} files withheld.")
if __name__=="__main__": main()
