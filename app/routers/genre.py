from fastapi import APIRouter, HTTPException
from app.models.genre import GenreCreate, Genre
from app.services.genre_service import create_genre, get_all_genres, delete_genre_by_name

router = APIRouter(prefix="/genres", tags=["genres"])

@router.post("/", response_model=Genre)
def create_genre_route(genre: GenreCreate):
    return create_genre(genre)

@router.get("/", response_model=list[Genre])
async def read_genres():
    return await get_all_genres()

@router.delete("/{name}")
async def delete_genre(name: str):
    success = await delete_genre_by_name(name)
    if not success:
        raise HTTPException(status_code=404, detail="Genre not found")
    return {"message": f"Genre '{name}' deleted"}