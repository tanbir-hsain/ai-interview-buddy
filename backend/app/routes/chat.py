from datetime import datetime

from fastapi import APIRouter
from pymongo.errors import DuplicateKeyError

from app.models.chat import ChatRequest
from app.ai.gemini import ask_ai
from app.db.mongodb import collection

router = APIRouter()


@router.post("/")
def chat(request: ChatRequest):

    question = request.question.strip().lower()

    data = collection.find_one({"question": question})

    if data:
        return {"answer": data["answer"]}

    answer = ask_ai(question)

    try:
        collection.insert_one({
            "question": question,
            "answer": answer,
            "created_at": datetime.utcnow()
        })
    except DuplicateKeyError:
        data = collection.find_one({"question": question})
        return {"answer": data["answer"]}

    return {"answer": answer}