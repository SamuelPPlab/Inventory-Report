import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def csv_importer(path, type):
        with open(path, "r") as file:
            inventory_data = csv.DictReader(file)
            list_inventory = list(inventory_data)
            if type == "simples":
                return SimpleReport.generate(list_inventory)
            else:
                return CompleteReport.generate(list_inventory)

    def json_importer(path, type):
        with open(path) as file:
            content = file.read()
            inventory_data = json.loads(content)
            list_inventory = list(inventory_data)
            if type == "simples":
                return SimpleReport.generate(list_inventory)
            else:
                return CompleteReport.generate(list_inventory)

    def import_data(path, type):
        if path.endswith(".csv"):
            return Inventory.csv_importer(path, type)
        elif path.endswith(".json"):
            return Inventory.json_importer(path, type)
