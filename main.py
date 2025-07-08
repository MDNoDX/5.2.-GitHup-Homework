import os
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