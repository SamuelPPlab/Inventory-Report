from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.json_importer import JsonImporter

from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer=JsonImporter):
        self.data = list()
        self.importer = importer

    def import_data(self, path, type_report):
        list_products = self.importer.import_data(path)
        self.data.extend(list_products)

        if type_report == "simples":
            report = SimpleReport.generate(list_products)
            return report
        else:
            report = CompleteReport.generate(list_products)
            return report

    def __iter__(self):
        return InventoryIterator(self.data)


if __name__ == "__main__":
    inventory = InventoryRefactor()
    inventory.import_data("inventory_report/data/inventory.json", "simples")

    for product in inventory:
        print(product)
