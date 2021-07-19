from inventory_report.reports.complete_report import (
    SimpleReport,
    CompleteReport,
)
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, report_type):
        file = self.importer.import_data(path)
        self.data.extend(file)
        if report_type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
