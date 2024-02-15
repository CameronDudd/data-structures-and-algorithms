"""A Sorted Tale"""

from __future__ import annotations
import csv
from typing import List
from dataclasses import dataclass
from functools import cached_property
from utils.sorting_algorithms import bubble_sort_custom_comp_func, quick_sort_custom_comp_func


FILE = "src/lib/books_small.csv"


@dataclass
class Book:
    """Book"""

    title: str
    author: str

    def __len__(self) -> int:
        return sum(ord(_) for _ in self.title_lower + self.author_lower)

    @cached_property
    def title_lower(self) -> str:
        """return title lower"""
        return self.title.lower()

    @cached_property
    def author_lower(self) -> str:
        """return author lower"""
        return self.author.lower()

    @staticmethod
    def compare_by_title_lower_ascending(book_a: Book, book_b: Book) -> bool:
        """compare two books by their title in lower case"""
        for a, b in zip(book_a.title_lower, book_b.title_lower):
            if a != b:
                return ord(a) > ord(b)
        return len(book_a.title_lower) > len(book_b.title_lower)

    @staticmethod
    def compare_by_author_lower_ascending(book_a: Book, book_b: Book) -> bool:
        """compare two books by their author in lower case"""
        for a, b in zip(book_a.author_lower, book_b.author_lower):
            if a != b:
                return ord(a) > ord(b)
        return len(book_a.author_lower) > len(book_b.author_lower)

    @staticmethod
    def compare_by_total_length_ascending(book_a: Book, book_b: Book) -> bool:
        """compare two books by the sum of their names and authors"""
        return len(book_a) > len(book_b)


def get_bookshelf() -> List[Book]:
    """get bookshelf"""
    bookshelf = []
    with open(FILE, "r", encoding="UTF-8") as csv_file:
        shelf = csv.reader(csv_file)
        _ = next(shelf)
        for title, author in shelf:
            bookshelf.append(Book(title, author))
    return bookshelf


def main() -> None:
    """main"""
    bookshelf = get_bookshelf()
    for book in bookshelf:
        print("+ ", "Title:", book.title_lower, "\n   Author:", book.author_lower)
    print("")

    print("+----BUBBLE SORT TITLE LOWER-----")
    for book in bubble_sort_custom_comp_func(arr=bookshelf, comp_func=Book.compare_by_title_lower_ascending, inplace=False):
        print("| ", book.title_lower)
    print("")

    print("+----QUICK SORT TITLE LOWER-----")
    for book in quick_sort_custom_comp_func(arr=bookshelf, comp_func=Book.compare_by_title_lower_ascending):
        print("| ", book.title_lower)
    print("")

    print("+----BUBBLE SORT AUTHOR LOWER-----")
    for book in bubble_sort_custom_comp_func(arr=bookshelf, comp_func=Book.compare_by_author_lower_ascending, inplace=False):
        print("| ", book.author_lower)
    print("")

    print("+----QUICK SORT AUTHOR LOWER-----")
    for book in quick_sort_custom_comp_func(arr=bookshelf, comp_func=Book.compare_by_author_lower_ascending):
        print("| ", book.author_lower)
    print("")

    print("+----BUBBLE SORT TOTAL LOWER-----")
    for book in bubble_sort_custom_comp_func(arr=bookshelf, comp_func=Book.compare_by_total_length_ascending, inplace=False):
        print("| ", book.title_lower, book.author_lower)
    print("")

    print("+----QUICK SORT TOTAL LOWER-----")
    for book in quick_sort_custom_comp_func(arr=bookshelf, comp_func=Book.compare_by_total_length_ascending):
        print("| ", book.title_lower, "|", book.author_lower)
    print("")


if __name__ == "__main__":
    main()
