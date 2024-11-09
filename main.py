"""Класс Library:
   Хранит книги и автоматически присваивает каждой книге уникальный id.
   Имеет методы add_book и get_book_info.
   Поддерживает метод для поиска книг по автору с перегрузкой: можно искать по одному автору или передавать список авторов.

Переопределить методы str в классах для красивого вывода объектов

Примечание: в рамках задание создать два файла: classes.py и main.py.
В первом будут описаны все классы, во втором классы будут импортированы и
использованы.
"""

from classes import Book, Library

# Создаём экземпляр библиотеки
library = Library()

# Создаём несколько книг
book1 = Book(title="Code", author="Charles Petzold", pages=250, year=1999, price=29.99)
book2 = Book(title="Computer Science Distilled", author="Wladston Ferreira Filho", pages=400, year=2019, price=33.33)
book3 = Book(title="Learning C++", author="John Doe", pages=300, year=2020, price=35.50)

# Добавляем книги в библиотеку
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Получаем информацию о книге по ID
print("\nИнформация о книге с ID 1:")
print(library.get_book_info(1))

# Поиск по автору
print("\nКниги автора John Doe:")
books_by_john_doe = library.find_books_by_author("John Doe")
for book in books_by_john_doe:
    print(book)

# Поиск по списку авторов
print("\nКниги авторов John Doe и Jane Smith:")
books_by_multiple_authors = library.find_books_by_author(["John Doe", "Jane Smith"])
for book in books_by_multiple_authors:
    print(book)

# Выводим общее количество книг в библиотеке
print("\n", library)