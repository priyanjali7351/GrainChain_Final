from fastapi import FastAPI
from app.database.db import engine, Base
from app.api.auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Backend running"}