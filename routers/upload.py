from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
