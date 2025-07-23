from fastapi import FastAPI
from neo4j import GraphDatabase

from app.routers import user, song, artist, genre, relationships

app = FastAPI()

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "test1234"))

app.include_router(user.router)
app.include_router(song.router)
app.include_router(artist.router)
app.include_router(genre.router)
app.include_router(relationships.router)

@app.get("/")
def route():
    return {"message": "Hello from FastAPI + Neo4j"}

@app.get("/ping-db")
def ping_db():
    with driver.session() as session:
        greeting = session.run("RETURN 'Neo4j is working' AS msg").single()["msg"]
        return {"message": greeting}

