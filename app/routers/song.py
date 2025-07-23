from fastapi import APIRouter, HTTPException
from app.models.song import SongCreate, Song
from app.services.song_service import create_song, get_all_songs, delete_song_by_id

router = APIRouter(prefix="/songs", tags=["songs"])

@router.post("/", response_model=Song)
def create_song_route(song: SongCreate):
    return create_song(song)

@router.get("/", response_model=list[Song])
async def read_songs():
    return await get_all_songs()

@router.delete("/{song_id}")
async def delete_song(song_id: str):
    success = await delete_song_by_id(song_id)
    if not success:
        raise HTTPException(status_code=404, detail="Song not found")
    return {"message": f"Song {song_id} deleted"}