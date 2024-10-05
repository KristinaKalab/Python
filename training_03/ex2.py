from book import Book

library = [Book("Война и Мир", "Толстой Л.Н."),
           Book("Незнайка на Луне", "Носов Н.Н."),
           Book("Сказка о царе Салтане", "Пушкин А.С.")]


for book in library:
    print(f"{book.title} - {book.autor}")
