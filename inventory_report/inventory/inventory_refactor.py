from .inventory_iterator import InventoryIterator


class InventoryRefactor(InventoryIterator):
    def __init__(self, importer):
        self.importer = importer
        self.data = []
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current_value = self.data[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return current_value

    def import_data(self, path, tipo_de_relatorio):
        self.data += self.importer.import_data(path)
