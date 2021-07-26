from collections.abc import Iterable
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer=CsvImporter()):
        self.importer = importer
        self.data = []

    def import_data(self, export_file, type_report="simples"):
        self.data += self.importer.import_data(export_file, type_report)

    def __iter__(self):
        return InventoryIterator(self.data)
