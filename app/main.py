import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.config import IMAGE_DIR, MUSIC_DIR, ALLOWED_IMAGE_TYPES, ALLOWED_MUSIC_TYPES
from app.utils import generate_filename

app = FastAPI(title="Media Hosting")

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

app.mount("/images", StaticFiles(directory=IMAGE_DIR), name="images")
app.mount("/music", StaticFiles(directory=MUSIC_DIR), name="music")
app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/", response_class=HTMLResponse)
def index():
    with open("public/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid image type")

    filename = generate_filename(file.filename)
    path = os.path.join(IMAGE_DIR, filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    return {
        "url": f"/images/{filename}"
    }


@app.post("/upload/music")
async def upload_music(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_MUSIC_TYPES:
        raise HTTPException(status_code=400, detail="Invalid audio type")

    filename = generate_filename(file.filename)
    path = os.path.join(MUSIC_DIR, filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    return {
        "url": f"/music/{filename}"
    }