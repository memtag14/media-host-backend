import os

# Папки для хранения файлов
IMAGE_DIR = "uploads/images"
MUSIC_DIR = "uploads/music"

# Разрешённые типы файлов
ALLOWED_IMAGE_TYPES = ["image/png", "image/jpeg", "image/jpg", "image/gif", "image/webp"]
ALLOWED_MUSIC_TYPES = ["audio/mpeg", "audio/mp3", "audio/wav", "audio/ogg"]

# Максимальный размер файла (10 МБ)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# Создание папок, если их нет
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)
