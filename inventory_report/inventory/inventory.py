from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def read_by_extension(path):
        with open(path) as file:
            if path.endswith(".csv"):
                inventory = csv.DictReader(file)
                result = list(inventory)
            elif path.endswith(".json"):
                result = json.load(file)
            elif path.endswith(".xml"):
                inventory = xmltodict.parse(file.read())
                result = inventory["dataset"]["record"]
            else:
                raise Exception("Invalid extension")

            return result

    @classmethod
    def import_data(cls, path, type):
        inventory = cls.read_by_extension(path)

        if type == "simples":
            return SimpleReport.generate(inventory)
        elif type == "completo":
            return CompleteReport.generate(inventory)
        else:
            raise Exception("Invalid type")
