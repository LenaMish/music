from pydantic import BaseModel
from uuid import uuid4


class ArtistCreate(BaseModel):
    name: str


class Artist(BaseModel):
    id: str
    name: str