import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.config import IMAGE_DIR, MUSIC_DIR, ALLOWED_IMAGE_TYPES, ALLOWED_MUSIC_TYPES, MAX_FILE_SIZE
from app.utils import generate_filename

app = FastAPI(title="Media Hosting")

# === CORS для GitHub Pages ===
origins = [
    "https://memtag14.github.io",
    "https://memtag14.github.io/media-host"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Создаем папки для загрузок, если их нет ===
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

# === Монтируем статические папки ===
app.mount("/images", StaticFiles(directory=IMAGE_DIR), name="images")
app.mount("/music", StaticFiles(directory=MUSIC_DIR), name="music")

# === Проверка работы сервера ===
@app.get("/", response_class=HTMLResponse)
def index():
    return "<h1>Media Hosting Backend</h1><p>Работает!</p>"

# === Проверка размера файла ===
async def check_file_size(file: UploadFile):
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")
    await file.seek(0)
    return contents

# === Загрузка изображений ===
@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid image type")

    contents = await check_file_size(file)
    filename = generate_filename(file.filename)
    path = os.path.join(IMAGE_DIR, filename)

    with open(path, "wb") as f:
        f.write(contents)

    return {"url": f"/images/{filename}"}

# === Загрузка музыки ===
@app.post("/upload/music")
async def upload_music(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_MUSIC_TYPES:
        raise HTTPException(status_code=400, detail="Invalid audio type")

    contents = await check_file_size(file)
    filename = generate_filename(file.filename)
    path = os.path.join(MUSIC_DIR, filename)

    with open(path, "wb") as f:
        f.write(contents)

    return {"url": f"/music/{filename}"}
