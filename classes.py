from dataclasses import dataclass, field
from typing import Optional, List, Union


@dataclass
class Book:
    title: str
    author: str
    pages: int
    year: int
    price: float
    book_id: Optional[int] = field(default=None, compare=False)

    def __str__(self):
        return (f"Book ID: {self.book_id} | Title: {self.title} | "
                f"Author: {self.author} | Year: {self.year} | Pages: {self.pages} | "
                f"Price: ${self.price:.2f}")


class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1  # Счётчик для уникального book_id

    def add_book(self, book: Book):
        book.book_id = self.next_id
        self.books.append(book)
        self.next_id += 1
        print(f"Книга '{book.title}' добавлена с ID {book.book_id}.")

    def get_book_info(self, book_id: int) -> Optional[str]:
        for book in self.books:
            if book.book_id == book_id:
                return str(book)
        return "Книга с указанным ID не найдена."

    def find_books_by_author(self, author: Union[str, List[str]]) -> List[Book]:
        if isinstance(author, str):
            authors = [author]
        else:
            authors = author

        found_books = [book for book in self.books if book.author in authors]
        return found_books

    def __str__(self):
        return f"Library with {len(self.books)} books"