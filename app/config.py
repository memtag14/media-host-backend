import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
IMAGE_DIR = os.path.join(UPLOAD_DIR, "images")
MUSIC_DIR = os.path.join(UPLOAD_DIR, "music")

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp"]
ALLOWED_MUSIC_TYPES = ["audio/mpeg", "audio/wav", "audio/ogg"]
