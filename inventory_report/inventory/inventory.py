import csv
import json

from xml_to_dict import XMLtoDict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def read_csv(cls, _file_name):
        with open(_file_name) as item:
            reader = csv.DictReader(item, delimiter=",")
            products = [row for row in reader]
        return products

    @classmethod
    def read_json(cls, file_name):
        with open(file_name) as item:
            products = json.load(item)
        return products

    @classmethod
    def read_xml(cls, file_name):
        with open(file_name) as item:
            parser = XMLtoDict()
            reader = item.read()
            container_tag = "record"
            products = parser.value_from_nest(container_tag, reader)
        return products

    @classmethod
    def getProducts(cls, file_name):
        if file_name.endswith(".csv"):
            return cls.read_csv(file_name)
        elif file_name.endswith(".json"):
            return cls.read_json(file_name)
        elif file_name.endswith(".xml"):
            return cls.read_xml(file_name)

    @classmethod
    def import_data(cls, file_name, report_type):
        products = cls.getProducts(file_name)
        if report_type == "simples":
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)
