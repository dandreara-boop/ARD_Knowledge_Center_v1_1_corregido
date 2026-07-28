from __future__ import annotations

from pathlib import Path
import os
import re
import markdown
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates

from app.navigation import (
    INDEX_PAGES,
    MODULE_INDEXES,
    PROJECT_INFO,
    PROJECT_PROGRESS,
    iter_navigation_items,
    sorted_navigation,
)

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"

APP_USER = os.getenv("ARD_KC_USER", "admin")
APP_PASSWORD = os.getenv("ARD_KC_PASSWORD", "cambiar123")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")

app = FastAPI(title="ARD Suite Knowledge Center")
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

def is_logged(request: Request) -> bool:
    return bool(request.session.get("user"))

def slug_to_file(slug: str) -> Path:
    safe = re.sub(r"[^a-zA-Z0-9_/\-]", "", slug)
    return CONTENT_DIR / f"{safe}.md"

def expand_includes(raw: str, stack: tuple[str, ...] = ()) -> str:
    def replace(match: re.Match[str]) -> str:
        slug = match.group(1).strip()
        if slug in stack:
            return f"\n> Inclusión omitida por referencia circular: `{slug}`.\n"
        file = slug_to_file(slug)
        if not file.exists():
            return f"\n> Documento incluido no encontrado: `{slug}`.\n"
        included = file.read_text(encoding="utf-8")
        return "\n\n" + expand_includes(included, (*stack, slug)) + "\n\n"

    return re.sub(r"\{\{\s*include:([a-zA-Z0-9_/\-]+)\s*\}\}", replace, raw)

def read_doc(slug: str):
    file = slug_to_file(slug)
    if not file.exists():
        return None
    raw = file.read_text(encoding="utf-8")
    title = file.stem.replace("_", " ").title()
    for line in raw.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    rendered_raw = expand_includes(raw, (slug,))
    html = markdown.markdown(
        rendered_raw,
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"permalink": True}},
    )
    return {"slug": slug, "title": title, "raw": rendered_raw, "html": html}

def all_docs():
    docs = []
    seen = set()
    for item in iter_navigation_items():
        slug = item.get("doc_slug")
        if not slug or slug in seen:
            continue
        data = read_doc(slug)
        if data:
            seen.add(slug)
            docs.append({"slug": slug, "label": item["title"], "title": data["title"], "raw": data["raw"]})
    return docs


def common_context(request: Request, **extra):
    context = {
        "request": request,
        "navigation": sorted_navigation(),
        "project": PROJECT_INFO,
        "current_path": request.url.path,
        "current_user": request.session.get("user"),
    }
    context.update(extra)
    return context

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == APP_USER and password == APP_PASSWORD:
        request.session["user"] = username
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Usuario o contraseña incorrectos.",
    })

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    if not is_logged(request):
        return RedirectResponse("/login")
    return templates.TemplateResponse("home.html", common_context(
        request,
        progress_items=PROJECT_PROGRESS,
    ))


@app.get("/modulos/{module_slug}", response_class=HTMLResponse)
def module_index(request: Request, module_slug: str):
    if not is_logged(request):
        return RedirectResponse("/login")
    page = MODULE_INDEXES.get(module_slug)
    if not page:
        return HTMLResponse("Modulo no encontrado.", status_code=404)
    if page.get("doc_slug"):
        doc = read_doc(page["doc_slug"])
        if doc:
            return templates.TemplateResponse("document.html", common_context(
                request,
                doc=doc,
                current_slug=page["doc_slug"],
            ))
    return templates.TemplateResponse("module_index.html", common_context(
        request,
        page=page,
    ))


@app.get("/modelo-datos", response_class=HTMLResponse)
def data_model_index(request: Request):
    if not is_logged(request):
        return RedirectResponse("/login")
    page = INDEX_PAGES["modelo-datos"]
    doc = read_doc(page["doc_slug"])
    if doc:
        return templates.TemplateResponse("document.html", common_context(
            request,
            doc=doc,
            current_slug=page["doc_slug"],
        ))
    return templates.TemplateResponse("module_index.html", common_context(
        request,
        page=page,
    ))


@app.get("/wireframes", response_class=HTMLResponse)
def wireframes_index(request: Request):
    if not is_logged(request):
        return RedirectResponse("/login")
    page = INDEX_PAGES["wireframes"]
    doc = read_doc(page["doc_slug"])
    if doc:
        return templates.TemplateResponse("document.html", common_context(
            request,
            doc=doc,
            current_slug=page["doc_slug"],
        ))
    return templates.TemplateResponse("module_index.html", common_context(
        request,
        page=page,
    ))

@app.get("/doc/{slug:path}", response_class=HTMLResponse)
def view_doc(request: Request, slug: str):
    if not is_logged(request):
        return RedirectResponse("/login")
    doc = read_doc(slug)
    if not doc:
        return HTMLResponse("Documento no encontrado.", status_code=404)
    return templates.TemplateResponse("document.html", common_context(
        request,
        doc=doc,
        current_slug=slug,
    ))

@app.get("/buscar", response_class=HTMLResponse)
def search(request: Request, q: str = ""):
    if not is_logged(request):
        return RedirectResponse("/login")
    results = []
    if q.strip():
        query = q.lower().strip()
        for doc in all_docs():
            if query in doc["raw"].lower() or query in doc["title"].lower():
                snippet = doc["raw"].replace("#", "").replace("\n", " ")
                pos = snippet.lower().find(query)
                start = max(0, pos - 90) if pos >= 0 else 0
                snippet = snippet[start:start + 260]
                results.append({**doc, "snippet": snippet})
    return templates.TemplateResponse("search.html", common_context(
        request,
        q=q,
        results=results,
    ))
