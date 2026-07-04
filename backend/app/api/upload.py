from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter()


UPLOAD_DIRECTORY = "uploaded_pdfs"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": f"{file.filename} uploaded successfully."
    }