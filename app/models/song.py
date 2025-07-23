from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

class SongCreate(BaseModel):
    title: str
    year: Optional[int] = None


class Song(BaseModel):
    id: str
    title: str
    year: Optional[int]