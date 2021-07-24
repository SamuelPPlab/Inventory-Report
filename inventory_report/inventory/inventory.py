import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def __init__(self, path, type):
        self.path = path
        self.type = type

    @classmethod
    def load_file(cls, path: str) -> str:
        with open(path, mode="r") as content:
            if path.endswith(".csv"):
                return list(csv.DictReader(content))
            elif path.endswith(".json"):
                return json.load(content)
            elif path.endswith(".xml"):
                xml_content_dict = xmltodict.parse(content.read())
                return [
                    dict(product)
                    for product in xml_content_dict["dataset"]["record"]
                ]

    @classmethod
    def import_data(cls, path: str, type: str) -> str:
        product_list = cls.load_file(path)
        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)
