import uuid
from app.db import driver, get_neo4j_session
from app.models.song import SongCreate, Song

def create_song(data: SongCreate) -> Song:
    song_id = str(uuid.uuid4())
    with driver.session() as session:
        session.run(
            """
            CREATE (s: Song {id: $id, title: $title, year: $year})
            """,
            id=song_id, title=data.title, year=data.year
        )
    return Song(id=song_id, title=data.title, year=data.year)

async def delete_song_by_id(song_id: str) -> bool:
    query = "MATCH (s: Song{id: $id}) DETACH DELETE s RETURN count(s) as deleted_count"
    async with get_neo4j_session() as session:
        result = await session.run(query, id=song_id)
        record = await result.single()
        return record ["deleted_count"] > 0

async def get_all_songs():
    query = "MATCH (s:Song) RETURN s.title AS title, s.year AS year, s.id AS id"
    async with get_neo4j_session() as session:
        result = await session.run(query)
        songs = []
        async for record in result:
            songs.append(record.data())
        return songs