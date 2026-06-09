from sqlalchemy import Column, Integer, String
from app.database.db import Base

class TestUser(Base):
    __tablename__ = "test_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)