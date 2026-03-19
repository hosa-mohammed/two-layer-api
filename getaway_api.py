from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    phone: str
    city: str

@app.post("/users")
async def create_user(user: User):

    response = requests.post(
        "http://127.0.0.1:8001/internal/users",
        json=user.model_dump()
    )

    return response.json()
