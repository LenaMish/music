from neo4j import AsyncGraphDatabase
from contextlib import asynccontextmanager

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "test1234"

driver = AsyncGraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

@asynccontextmanager
async def get_neo4j_session():
    session = driver.session()
    try:
        yield session
    finally:
        await session.close()

async def close_driver():
    await driver.close()
