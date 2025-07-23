from pydantic import BaseModel, EmailStr
from uuid import uuid4

class UserCreate(BaseModel):
    name: str
    email: EmailStr


class User(BaseModel):
    id: str
    name: str
    email: EmailStr