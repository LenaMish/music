import uuid
from app.db import driver, get_neo4j_session
from app.models.artist import ArtistCreate, Artist

def create_artist(data: ArtistCreate) -> Artist:
    artist_id = str(uuid.uuid4())
    with driver.session() as session:
        session.run(
            """
            CREATE (a: Artist {id: $id, name: $name})
            """,
            id=artist_id, name=data.name
        )
    return Artist(id=artist_id, name=data.name)

async def get_all_artists():
    query = "MATCH (a: Artist) RETURN a.name as name, a.id as id"
    async with get_neo4j_session() as session:
        result = await session.run(query)
        records = []
        async for record in result:
            records.append(record.data())
        return records

async def delete_artist_by_name(name: str):
    query = "MATCH (a: Artist {name: $name}) DETACH DELETE a RETURN count(a) as deleted_count"
    async with get_neo4j_session() as session:
        result = await session.run(query, name=name)
        record = await result.single()
        return record["deleted_count"] > 0
