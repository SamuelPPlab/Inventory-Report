from collections.abc import Iterable
from .inventory_iterator import InventoryIterator
from inventory_report.importer.json_importer import JsonImporter

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer=JsonImporter):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path, type):
        iterable_data = self.importer.import_data(file_path)
        self.data.extend(iterable_data)

        if type == "simples":
            return SimpleReport.generate(iterable_data)
        elif type == "completo":
            return CompleteReport.generate(iterable_data)
