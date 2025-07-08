from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
class Base(DeclarativeBase):
    pass

class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50))

class Themes(Base):
    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(50))