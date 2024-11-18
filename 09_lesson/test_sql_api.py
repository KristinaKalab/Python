import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_operations import add_subject, update_subject, delete_subject, get_subject

# Строка подключения
DATABASE_URL = 'postgresql://postgres:Rjnbr-;bdjnbr1@localhost:5433/QA'

# Создание движка и сессии
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def test_add_subject():
    session = Session()   # Открытие сессии

    # Значения для subject_id и subject_title
    subject_id = 20
    subject_title = 'Algebra'

    # Добавление нового предмета
    inserted_subject = add_subject(session, subject_id, subject_title)

    # Проверка, что предмет добавлен с правильными значениями
    assert inserted_subject[0] == subject_id
    assert inserted_subject[1] == subject_title

    session.close()  # Закрытие сессии


def test_update_subject():
    session = Session()

    old_title = "Algebra"
    new_title = "Advanced Mathematics"

    # Проверка, что предмет с названием old_title существует перед обновлением
    existing_subject = get_subject(session, old_title)

    if existing_subject is None:
        # Если записи нет, добавляем ее для теста
        add_subject(session, 20, old_title)

    # Обновление названия предмета
    update_subject(session, old_title, new_title)

    # Проверка, что предмет изменён
    updated_subject = get_subject(session, new_title)
    assert updated_subject is not None and updated_subject[0] == new_title

    session.close()


def test_delete_subject():
    session = Session()

    title_to_delete = "Advanced Mathematics"

    # Проверка, что предмет с названием title_to_delete существует перед удалением
    existing_subject = get_subject(session, title_to_delete)

    if existing_subject is None:
        # Если записи нет, добавляем ее для теста
        add_subject(session, 20, title_to_delete)

    # Удаление предмета
    delete_subject(session, title_to_delete)

    # Проверка, что предмет удалён
    deleted_subject = get_subject(session, title_to_delete)
    assert deleted_subject is None

    session.close()
