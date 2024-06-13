from modules.constants import WRONG_ACTION_INFO
from modules.constants import ACTION_PROMPT


class LibraryManager:
    def __init__(self, library_storage):
        self.actions = {}
        self.library = library_storage
        self.books = {}
        self.history = []

    def list_actions(self):
        actions = ""
        for idx, name in enumerate(self.actions, start=1):
            actions += f"{idx}. {name}\n"
        return ACTION_PROMPT.format(actions)

    def execute(self, name):
        if name not in self.actions:
            print(WRONG_ACTION_INFO.format(name))
        else:
            self.actions[name](self)
        self.library.save()

    def assign(self, name):
        def decorate(func):
            self.actions[name] = func
        return decorate
