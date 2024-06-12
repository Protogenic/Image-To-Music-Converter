from PIL import Image
from io import BytesIO

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from image_to_music.create_midi import create_music_file

app = FastAPI()
templates: Jinja2Templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/api/uploadfile/", response_class=HTMLResponse)
async def create_upload_files(file: UploadFile, request: Request):
    extension = file.filename.split(".")[-1]
    if extension == 'jfif':
        extension = 'jpg'
    if not extension in {"jpg", "jpeg", "png"}:
        return {"message": "Wrong file extension"}

    source_image = Image.open(file.file)
    source_image.save("static/image." + extension)

    create_music_file(source_image)

    return templates.TemplateResponse("post.html", {"request": request,
                                                    "file_name": "static/music.mid",
                                                    "extension": extension})
