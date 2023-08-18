from fastapi import FastAPI, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from app.use_cases import DbLoadMedias, DbGetNasaIds
from app.repository import Repository
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.config import FASTAPI
from app.database import ENGINE
from typing import Annotated
from app import schemas

app = FastAPI(**FASTAPI)

app.mount("/static", StaticFiles(directory="app/web/static"), name="static")
TEMPLATES = Jinja2Templates(directory="app/web/templates")
schemas.BASE.metadata.create_all(bind=ENGINE)


@app.get("/", response_class=RedirectResponse, status_code=307, summary="Redirect", tags=["Panel"])
async def root():
    DbLoadMedias().handle()
    return RedirectResponse("/panel")


@app.get("/panel", response_class=HTMLResponse, status_code=200, summary="Show Panel", tags=["Panel"])
async def panel(request: Request):
    return TEMPLATES.TemplateResponse("index.html", {"request": request})


@app.get("/data")
async def data():
    return {"data": DbGetNasaIds().handle()}


@app.get("/search/{nasa_id}")
async def search(nasa_id: Annotated[str, Path()]):
    return {"data": Repository().get_one(nasa_id)}
