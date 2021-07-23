from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    # @classmethod
    def import_data(self, path, report_type):
        self.data.extend(self.importer.import_data(path))
        report_method = {"simples": SimpleReport, "completo": CompleteReport}
        return report_method[report_type].generate(self.data)
