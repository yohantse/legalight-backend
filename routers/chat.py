from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    jurisdiction: str = "Ethiopia"

@router.post("/")
def answer_question(request: ChatRequest):
    # Placeholder — replace with OpenAI or Claude API later
    return {
        "answer": f"Simulated answer to: {request.question}",
        "jurisdiction": request.jurisdiction
    }
