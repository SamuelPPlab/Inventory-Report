import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(file_inventory, type):
        with open(file_inventory) as file:
            if file_inventory.endswith(".csv"):
                inventory = csv.DictReader(file)
                result = list(inventory)
            elif file_inventory.endswith(".json"):
                inventory = json.load(file)
                result = inventory
            else:
                # https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
                inventory = xmltodict.parse(file.read())
                result = inventory["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(result)
        else:
            return CompleteReport.generate(result)
