from collections import Iterator

class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current = 0

    def __next__(self):
        if self.current >= len(self.data):
            raise StopIteration

        item = self.data[self.current]
        self.current += 1

        return item
