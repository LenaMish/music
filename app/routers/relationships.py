from fastapi import APIRouter, Depends
from app.db import get_neo4j_session

router = APIRouter(prefix="/relations", tags=["Relationships"])

@router.post("/performed")
async def create_performed_relation(artist_name: str, song_title: str, session=Depends(get_neo4j_session)):
    query = """
    MATCH (a:Artist {name: $artist_name})
    MATCH (s:Song {title: $song_title})
    MERGE (a)-[:PERFORMED]->(s)
    """
    await session.run(query, artist_name=artist_name, song_title=song_title)
    return {"message": f"Relation PERFORMED created: {artist_name} -> {song_title}"}

@router.post("/belongs_to")
async def create_belongs_to_relation(song_title: str, genre_name: str, session=Depends(get_neo4j_session)):
    query = """
    MATCH (s:Song {title: $song_title})
    MATCH (g:Genre {name: $genre_name})
    MERGE (s)-[:BELONGS_TO]->(g)
    """
    await session.run(query, song_title=song_title, genre_name=genre_name)
    return {"message": f"Relation BELONGS_TO created: {song_title} -> {genre_name}"}

@router.get("/artist_songs/{artist_name}")
async def get_songs_by_artist(artist_name: str, session=Depends(get_neo4j_session)):
    query = """
    MATCH (a:Artist {name: $artist_name})-[:PERFORMED]->(s:Song)
    RETURN s.id AS id, s.title AS title, s.year AS year
    """
    result = await session.run(query, artist_name=artist_name)
    songs = []
    async for record in result:
        songs.append(record.data())
    return songs