from typing import Iterable
from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, items: Iterable):
        self.items = items
        self.index = 0

    def __next__(self):
        item = self.items[self.index]
        self.index += 1
        return item
