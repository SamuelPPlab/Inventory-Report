from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __next__(self):
        self._index += 1
        if self._index > len(self._iterable):
            raise StopIteration()
        return self._iterable[self._index - 1]
