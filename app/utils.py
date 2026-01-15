import uuid
import os

def generate_filename(original_filename: str) -> str:
    """
    Генерирует уникальное имя файла с сохранением расширения.
    """
    ext = os.path.splitext(original_filename)[1]  # .png, .jpg и т.д.
    unique_name = uuid.uuid4().hex
    return f"{unique_name}{ext}"
