import uuid
from app.db import driver, get_neo4j_session
from app.models.genre import GenreCreate, Genre

def create_genre(data: GenreCreate) -> Genre:
    with driver.session() as session:
        session.run(
            """
            MERGE (g: Genre {name: $name})
            """,
            name=data.name
        )
    return Genre(name=data.name)

async def delete_genre_by_name(name: str) -> bool:
    query = "MATCH (g: Genre {name: $name}) DETACH DELETE g RETURN count(g) as deleted_count"
    async with get_neo4j_session() as session:
        result = await session.run(query, name=name)
        record = await result.single()
        return record["deleted_count"] > 0

async def get_all_genres():
    query = "MATCH (g:Genre) RETURN g.name as name"
    async with get_neo4j_session() as session:
        result = await session.run(query)
        records = []
        async for record in result:
            records.append(record.data())
        return records