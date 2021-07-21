from abc import abstractmethod
from inventory_report.inventory.inventory import Inventory


class Importer:
    @abstractmethod
    def import_data(file_name, format):
        if not file_name.endswith(format):
            raise TypeError("Invalid format")

        with open(file_name, "r") as report:
            return Inventory.method(file_name, report)
