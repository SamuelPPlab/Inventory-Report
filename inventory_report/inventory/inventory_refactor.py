from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type):
        inventory = self.importer.import_data(path)
        self.data.extend(inventory)
        if type == 'simples':
            return SimpleReport.generate(inventory)
        elif type == 'completo':
            return CompleteReport.generate(inventory)
        else:
            raise Exception("Invalid type")
