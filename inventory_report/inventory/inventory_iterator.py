from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, object):
        self.index = -1
        self.object = object

    def __next__(self):
        self.index += 1
        try:
            return self.object[self.index]
        except IndexError:
            raise StopIteration()
