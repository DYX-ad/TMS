"""Класс Book:
   Используем dataclass для создания книги.
   Атрибуты: book_id, pages, year, author, price. Book_id по умолчанию None присваивается только при добавлении книги в библиотеку.
   Выполняем валидацию атрибутов при создании книги. Для валидации создаем собственные исключения
   Реализуем метод сравнения книг по цене.
"""
from dataclasses import dataclass, field
from typing import Optional
from functools import total_ordering


# Определяем собственные исключения для валидации
class BookValidationError(Exception):
    pass


class InvalidPagesError(BookValidationError):
    pass


class InvalidYearError(BookValidationError):
    pass


class InvalidPriceError(BookValidationError):
    pass


@total_ordering
@dataclass
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: Optional[int] = field(default=None, compare=False)  # ID по умолчанию None, не участвует в сравнении

    def __post_init__(self):
        """Метод для валидации полей при создании экземпляра книги."""
        if self.pages <= 0:
            raise InvalidPagesError("Количество страниц должно быть положительным числом.")
        if self.year <= 0:
            raise InvalidYearError("Год выпуска должен быть положительным числом.")
        if self.price < 0:
            raise InvalidPriceError("Цена книги не может быть отрицательной.")
        if not self.author:
            raise BookValidationError("Поле author не должно быть пустым.")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price


# Пример использования
try:
    book1 = Book(pages=300, year=2020, author="Author One", price=25.99)
    book2 = Book(pages=150, year=2019, author="Author Two", price=30.50)
    print(f"Book1 дешевле Book2? {'Да' if book1 < book2 else 'Нет'}")  # Сравнение книг по цене
    print(f"Цена Book1 и Book2 одинаковая? {'Да' if book1 == book2 else 'Нет'}")

    # Создаём книгу с неверными данными, чтобы проверить валидацию
    book_invalid = Book(pages=-50, year=2018, author="Author Three", price=20)
except BookValidationError as e:
    print("Ошибка валидации:", e)
