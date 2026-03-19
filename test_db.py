from fastapi import FastAPI
import pyodbc

app = FastAPI()

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=.;"
    "Database=challengeDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

@app.get("/users")
async def get_users():

    cursor.execute("SELECT * FROM users")

    users = []

    for row in cursor:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return users