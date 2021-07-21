from collections.abc import Iterator


class InventoryIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value
