from book import Book

library = []

library.append(Book("Война и Мир", "Толстой Л.Н."))
library.append(Book("Незнайка на Луне", "Носов Н.Н."))
library.append(Book("Сказка о царе Салтане", "Пушкин А.С."))


for book in library:
    print(book)
