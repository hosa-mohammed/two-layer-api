from fastapi import FastAPI
import pyodbc
from pydantic import BaseModel

app = FastAPI()

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=.;"
    "Database=challengeDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

class User(BaseModel):
    name: str
    email: str
    phone: str
    city: str

@app.post("/internal/users")
async def create_user(user: User):
    print("API 2 RECEIVED:")
    print("name =", user.name)
    print("email =", user.email)
    print("phone =", user.phone)
    print("city =", user.city)

    cursor.execute(
        "INSERT INTO users (name, email, phone, city) VALUES (?, ?, ?, ?)",
        user.name,
        user.email,
        user.phone,
        user.city
    )

    conn.commit()

    return {
        "message": "User created successfully"
    }