from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, datas):
        self.datas = datas
        self.counter = 0

    def __next__(self):
        try:
            data = self.datas[self.counter]
        except IndexError:
            raise StopIteration()
        else:
            self.counter += 1
            return data
