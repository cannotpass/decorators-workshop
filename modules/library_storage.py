import json
import os


class LibraryStorage:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.books = {}
        self.history = []

    def add_history_entry(self, text):
        self.history.append(text)

    def save(self):
        if not os.path.exists(os.path.dirname(self.storage_path)):
            os.makedirs(os.path.dirname(self.storage_path))
        with open(self.storage_path, 'w') as f:
            json.dump({"books": self.books, "history": self.history}, f, indent=2)

    def load(self):
        if not os.path.exists(self.storage_path):
            self.books, self.history = {}, []
        else:
            with open(self.storage_path) as f:
                data = json.load(f)
            self.books = data['books']
            self.history = data['history']

    def items(self):
        for title, copies in self.books.items():
            yield title, copies

    def __iter__(self):
        return iter(self.history)

    def __bool__(self):
        return bool(self.books)
