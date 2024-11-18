from sqlalchemy import text
from sqlalchemy.orm import sessionmaker


def add_subject(session, subject_id, subject_title):
    result = session.execute(
        text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title) RETURNING subject_id, subject_title"),
        {"id": subject_id, "title": subject_title}
    )
    session.commit()
    return result.fetchone()


def update_subject(session, old_title, new_title):
    session.execute(text("UPDATE subject SET subject_title = :new_title WHERE subject_title = :old_title"),
                    {"new_title": new_title, "old_title": old_title})
    session.commit()


def delete_subject(session, title):
    session.execute(text("DELETE FROM subject WHERE subject_title = :title"),
                    {"title": title})
    session.commit()


def get_subject(session, title):
    result = session.execute(text("SELECT subject_title FROM subject WHERE subject_title = :title"),
                             {"title": title})
    return result.fetchone()
