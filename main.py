from fastapi import FastAPI
from routers import chat, upload, laws

app = FastAPI(title="Legalight AI Backend")

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(laws.router, prefix="/laws", tags=["Laws"])

@app.get("/")
def root():
    return {"msg": "Legalight AI backend is running."}
