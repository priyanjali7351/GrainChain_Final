from pydantic import BaseModel

class TestUserCreate(BaseModel):
    name: str