from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database import BASE


class Media(BASE):
    __tablename__ = "medias"

    id: Mapped[int] = mapped_column(primary_key=True)
    center: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(String(100))
    nasa_id: Mapped[str] = mapped_column(String(10))
    date_created: Mapped[str] = mapped_column(String(30))
    href: Mapped[str] = mapped_column(String(150))

    def __repr__(self) -> str:
        representation = f"Media(id={self.id!r},"
        representation += f" center={self.center!r},"
        representation += f" title={self.title!r},"
        representation += f" nasa_id={self.nasa_id!r},"
        representation += f" date_created={self.date_created!r},"
        representation += f" href={self.href!r})"
        return representation
