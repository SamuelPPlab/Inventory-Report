from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data_importer):
        self.data_importer = data_importer
        self.current_item = 0

    def __next__(self):
        stock_item = self.data_importer[self.current_item]

        if not stock_item:
            raise StopIteration()

        self.current_item += 1

        return stock_item
