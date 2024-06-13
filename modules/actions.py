from modules.manager import LibraryManager
from modules.constants import DISPLAY_BOOK_TPL
from modules.constants import NO_BOOKS_AVAILABLE_INFO
from modules.constants import LIST_BOOKS_TITLE
from modules.library_storage import LibraryStorage


lib_storage = LibraryStorage(storage_path="data/lib.json")
lib_storage.load()
lib_manager = LibraryManager(lib_storage)


@lib_manager.assign("add")
def add_book(manager):
    title = input("Title: ")
    copies = int(input("Copies: "))
    if copies < 0:
        raise ValueError("Copies must be greater than or equal to 0.")
    if title not in manager.library.books:
        manager.library.books[title] = 0
    manager.library.books[title] += copies
    manager.library.add_history_entry(f"Kupiono {title}, sztuk {copies}")


@lib_manager.assign("list")
def list_books(manager):
    if not manager.library:
        print(NO_BOOKS_AVAILABLE_INFO)
        return
    print(LIST_BOOKS_TITLE)
    for idx, (title, copies) in enumerate(manager.library.items(), start=1):
        print(DISPLAY_BOOK_TPL.format(idx, title, copies))


@lib_manager.assign("borrow")
def lend_book(manager):
    title = input("Which book would you like to get: ")
    copies = int(input("How many copies (number): "))
    if manager.library.books.get(title, 0) >= copies:
        manager.library.books[title] -= copies
    else:
        print("Not enough copies... Sorry.")


@lib_manager.assign("test")
def test_func(manager):
    print("THIS IS TESTING ONLY")
