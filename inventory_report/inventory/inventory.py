import xmltodict
import json
import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def get_file_xml(file_path):
        with open(file_path) as fd:
            file = xmltodict.parse(fd.read())
            products = file["dataset"]["record"]

            dict_products = [
                {item: product[item] for item in product}
                for product in products
            ]

        return dict_products

    def get_file_json(file_path):
        with open(file_path) as fd:
            dict_products = json.load(fd)
        return dict_products

    def get_file_csv(file_path):
        with open(file_path) as fd:
            dict_products = [row for row in csv.DictReader(fd)]
        return dict_products

    def get_instance(type_report, dict_products):
        if type_report == "simples":
            return SimpleReport.generate(dict_products)
        else:
            return CompleteReport.generate(dict_products)

    def import_data(file_path, type_report):
        dict_products = {}

        if file_path.endswith(".csv"):
            dict_products = Inventory.get_file_csv(file_path)
        elif file_path.endswith(".json"):
            dict_products = Inventory.get_file_json(file_path)
        elif file_path.endswith(".xml"):
            dict_products = Inventory.get_file_xml(file_path)

        return Inventory.get_instance(type_report, dict_products)
