from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self.products = products
        self.index = -1

    def __next__(self):
        try:
            self.index += 1
            return self.products[self.index]
        except IndexError:
            raise StopIteration
