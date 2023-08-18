
from app.schemas import Media
from app.database import SESSION
from sqlalchemy import select


class Repository:

    def __init__(self) -> None:
        pass

    def count(self) -> int:
        with SESSION() as session:
            return session.query(Media).count()

    def save_many(self, data: list[dict]) -> None:
        with SESSION() as session:
            medias = [Media(**item) for item in data]
            session.add_all(medias)
            session.commit()

    def get_all(self) -> list[str]:
        with SESSION() as session:
            query = select(Media.nasa_id)
            return session.scalars(query).fetchall()

    def get_one(self, nasa_id: str) -> Media:
        with SESSION() as session:
            return session.query(Media).filter(Media.nasa_id == nasa_id).one()
