import uuid
from app.db import driver
from app.models.user import UserCreate, User

def create_user(user_data: UserCreate) -> User:
    user_id = str(uuid.uuid4())
    with driver.session() as session:
        session.run(
            """
            CREATE (u:User {id: $id, name: $name, email: $email})
            """,
            id = user_id, name = user_data.name, email = user_data.email
        )
    return User(id = user_id, name = user_data.name, email = user_data.email)

