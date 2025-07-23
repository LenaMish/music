from fastapi import APIRouter, HTTPException
from app.models.artist import ArtistCreate, Artist
from app.services.artist_service import create_artist, get_all_artists, delete_artist_by_name

router = APIRouter(prefix="/artists", tags=["artists"])

@router.post("/", response_model=Artist)
def create_artist_route(artist: ArtistCreate):
    return create_artist(artist)

@router.get("/", response_model=list[Artist])
async def read_artists():
    return await get_all_artists()

@router.delete("/{name}")
async def delete_artist(name: str):
    success = await delete_artist_by_name(name)
    if not success:
        raise HTTPException(status_code=404, detail="Artist not found")
    return {"message": f"Artist '{name}' deleted"}
