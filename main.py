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

def update_lesson(lesson_id: int, new_name: str):
    with Session(engine) as session:
        lesson = session.get(Lesson, lesson_id)
        if lesson:
            lesson.name = new_name
            session.commit()
            print("'lesson' ma'lumoti yangilandi!\n")
        else:
            print("'lesson' ma'lumoti topilmadi!\n")

def add_theme(title: str, lesson_id: int):
    with Session(engine) as session:
        theme = Theme(title = title, lesson_id = lesson_id)
        session.add(theme)
        session.commit()
        print("'theme' ma'lumotlari qo'shildi!\n")

def show_themes():
    with Session(engine) as session:
        stmt = select(Theme)
        themes = session.scalars(stmt)
        print("• Themes: \n")
        for theme in themes:
            print("-" * 30)
            print(f"{theme.id}: {theme.title}\nLesson ID: {theme.lesson_id}")
        print()

def update_theme(theme_id: int, new_title: str):
    with Session(engine) as session:
        theme = session.get(Theme, theme_id)    
        if theme:
            theme.title = new_title
            session.commit()
            print("'theme' ma'lumoti yangilandi!\n")
        else:
            print("'theme' ma'lumoti topilmadi!\n")