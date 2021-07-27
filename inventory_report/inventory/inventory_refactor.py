from collections.abc import Iterable
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer=CsvImporter()):
        self.importer = importer
        self.data = []

    def import_data(self, export_file, type_report="simples"):
        self.data += self.importer.import_data(export_file, type_report)
        if type_report == "completo":
            return CompleteReport.generate(self.data)
        return SimpleReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
