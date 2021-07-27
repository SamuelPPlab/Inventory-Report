from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable

    def __next__(self):
        try:
            currentIterable = self._iterable[0]
        except IndexError:
            raise StopIteration()
        else:
            return currentIterable
