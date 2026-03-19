from fastapi import FastAPI
from app.api.routes.users import router as users_router

app = FastAPI(title="Service API")

app.include_router(users_router, prefix="/api/v1")