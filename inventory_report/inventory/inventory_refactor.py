from collections import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class InventoryRefactor(Iterable):
    def __init__(self, importer=None):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, report_type):
        importer_data = self.importer.import_data(path)
        self.data.extend(importer_data)

        if report_type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
