from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(InventoryIterator):
    def __init__(self, importer_class):
        self.importer = importer_class
        self.data = []
        self.row = 0

    def __iter__(self):
        self.row = 0
        return self

    def __next__(self):
        try:
            row = self.data[self.row]
        except IndexError:
            raise StopIteration
        self.row += 1
        return row

    def import_data(self, path, report_type):
        self.data += self.import_data(path)
