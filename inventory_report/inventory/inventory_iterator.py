from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iteration):
        self.iteration = iteration
        self.index = 0

    def __next__(self):
        self.index += 1

        if self.index > len(self.iteration):
            raise StopIteration()

        return self.iteration[self.index - 1]
