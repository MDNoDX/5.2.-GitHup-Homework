import os
from sqlalchemy import select
from modules import Lesson, Theme, engine
from sqlalchemy.orm import Session
os.system("cls" if os.name == "nt" else "clear")

def add_lesson_with_themes(name: str, theme_titles: list[str]):
    with Session(engine) as session:
        lesson = Lesson(name = name)
        themes = [Theme(title = ttitle) for ttitle in theme_titles]

        lesson.themes.extend(themes)
        session.add(lesson)
        session.commit()
        print("'lesson' ma'lumotlari qo'shildi!\n")

def show_lessons():
    with Session(engine) as session:
        stmt = select(Lesson)
        lessons = session.scalars(stmt)
        print("• Lessons: \n")
        for lesson in lessons:
            print("–" * 30)
            print(f"{lesson.id}: {lesson.name}")
            for theme in lesson.themes:
                print(f"  {theme.title}")
        print()

def update_lessons(lesson_id: int, new_name: str):
    with Session(engine) as session:
        lesson = session.get(Lesson, lesson_id)
        if lesson:
            lesson.name = new_name
            session.commit()
            print("'lesson' ma'lumoti yangilandi!\n")
        else:
            print("'lesson' ma'lumoti topilmadi!\n")