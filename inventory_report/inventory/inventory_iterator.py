from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iter):
        self.iter = iter
        self.index = 0

    def __next__(self):
        self.index += 1
        if self.index > len(self.iter):
            raise StopIteration()
        return self.iter[self.index - 1]
