from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, create_engine

class Base(DeclarativeBase):
    pass

class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50))
    themes: Mapped[List["Theme"]] = relationship(
        back_populates = "lesson", cascade = "all, delete-orphan")
    
    def __repr__(self):
        return f"Lesson ID: {self.id} - Name: {self.name}"

class Theme(Base):
    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(50))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    lesson: Mapped["Lesson"] = relationship(back_populates = "themes")

    def __repr__(self):
        return f"Theme ID: {self.id} - Title: {self.title} (Lesson ID: {self.lesson_id})"

engine = create_engine("sqlite:///lessons.db")
Base.metadata.create_all(engine)