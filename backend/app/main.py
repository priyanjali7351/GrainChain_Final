from fastapi import FastAPI
from app.database.db import engine, Base
from app.database.models import TestUser
from app.api.routes.test import router as test_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(test_router)

@app.get("/")
def root():
    return {"message": "Backend running"}