from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_laws():
    return {"message": "Welcome to the laws section!"}
