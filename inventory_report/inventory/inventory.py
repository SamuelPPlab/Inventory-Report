from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:

    def csv_reader(path):
        with open(path, mode="r") as file:
            content = csv.DictReader(file, delimeter=",", quotechar='"')
            products_list = [row for row in content]
            print("CSV", products_list[0])
            return products_list

    def json_reader(path):
        with open(path, mode="r") as file:
            content = json.load(file)
            print("JSON", content[0])
            return content

    @classmethod
    def import_data(cls, path, type_report):
        products_list = list()
        if path.endswith("csv"):
            products_list = cls.csv_reader(path)
        elif path.endswith("json"):
            products_list = cls.json_reader(path)

        if type_report == "simples":
            report = SimpleReport.generate(products_list)
            return report
        else:
            report = CompleteReport.generate(products_list)
            return report


if __name__ == "__main__":
    inventory = Inventory()
    inventory.import_data("data/inventory.json", "simples")
