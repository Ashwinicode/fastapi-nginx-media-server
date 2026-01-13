# 
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse
import os
import uuid
import shutil

app = FastAPI()

UPLOAD_DIR = r"E:\upload"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

@app.post("/upload-image")
async def upload_image(
    user_id: str = Form(...),
    file: UploadFile = File(...)
):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    user_folder = os.path.join(UPLOAD_DIR, user_id)
    os.makedirs(user_folder, exist_ok=True)

    filename = f"{uuid.uuid4()}{ext}"
    file_path = os.path.join(user_folder, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Image uploaded successfully",
            "filename": filename,
            "url": f"http://localhost/uploads/{user_id}/{filename}"
        }
    )