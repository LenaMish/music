This project is a REST API built with FastAPI and the Neo4j graph database to manage music data as a graph.

Features :
- Create artists, songs, and genres with unique UUIDs.
- Retrieve all artists, songs, or genres.
- Delete artists, songs, and genres by their IDs.

Create relationships between nodes:
- Artists perform songs (PERFORMED relationship).
- Songs belong to genres (BELONGS_TO relationship).

Query songs by artist or genre, and artists by song.
Retrieve all nodes from the database in a single endpoint.
Uses asynchronous Neo4j sessions for better performance.
Easy to run locally or with Docker (Neo4j + FastAPI).

Requirements:
- Python 3.9 or higher
- Neo4j (version 4.x or newer)
- Docker (optional, for easy setup)

## API Endpoints Overview

- `POST /artists` — create a new artist  
- `GET /artists` — get all artists  
- `DELETE /artists/{id}` — delete an artist by ID  

- `POST /songs` — create a new song  
- `GET /songs` — get all songs  
- `DELETE /songs/{id}` — delete a song by ID  

- `POST /genres` — create a new genre  
- `GET /genres` — get all genres  
- `DELETE /genres/{id}` — delete a genre by ID  

- `POST /relations/performed` — link an artist to a song  
- `POST /relations/belongs_to` — link a song to a genre  

- `GET /nodes` — get all nodes (artists, songs, genres)


