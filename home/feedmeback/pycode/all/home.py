from fastapi import APIRouter, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
home_router = APIRouter()

@home_router.get("/")
async def homepage(request:Request):
    return templates.TemplateResponse("pages/home.html", {"request":request})