from fastapi import APIRouter
from app.db import get_neo4j_session

router = APIRouter(prefix="/nodes", tags=["Nodes"])

@router.get("/grouped")
async def get_grouped_nodes():
    independent_query = """
    MATCH (n)
    WHERE NOT (()-[]->(n))
    RETURN n
    """

    dependent_query = """
    MATCH (n)
    WHERE (()-[]->(n))
    RETURN n
    """

    independent_nodes = []
    dependent_nodes = []

    async with get_neo4j_session() as session:
        independent_result = await session.run(independent_query)
        async for record in independent_result:
            node = record["n"]
            independent_nodes.append(node)

        dependent_result = await session.run(dependent_query)
        async for record in dependent_result:
            node = record["n"]
            dependent_nodes.append(node)

    return {
        "independent_nodes": independent_nodes,
        "dependent_nodes": dependent_nodes
    }
