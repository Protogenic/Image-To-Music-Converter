from fastapi import Request
from fastapi.templating import Jinja2Templates

from app import app, templates


@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})