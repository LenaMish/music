from pydantic import BaseModel

class GenreCreate(BaseModel):
    name: str


class Genre(BaseModel):
    name: str