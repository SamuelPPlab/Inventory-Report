import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        with open(path, "r") as file:
            inventory_data = csv.DictReader(file)
            list_inventory = list(inventory_data)
            if type == "simples":
                return SimpleReport.generate(list_inventory)
            else:
                return CompleteReport.generate(list_inventory)
