from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.products = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.products)

    def import_data(self, path, report_type):
        self.products.extend(self.importer.import_data(path))
        report = {"simples": SimpleReport, "completo": CompleteReport}
        return report[report_type].generate(self.products)
