import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def read_csv(path):
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            header, *rows = reader

            return [dict(zip(header, row)) for row in rows]

    @staticmethod
    def read_json(path):
        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def read_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        records = list(root)

        data = []
        for record in records:
            new_product = {}
            product = list(record)

            for key in product:
                new_product[key.tag] = key.text
            data.append(new_product)

        return data

    @staticmethod
    def import_data(path, report_type):
        file_type = path.split(".")[-1]

        if file_type == "csv":
            products = Inventory.read_csv(path)
        elif file_type == "json":
            products = Inventory.read_json(path)
        elif file_type == "xml":
            products = Inventory.read_xml(path)

        if report_type == "simples":
            return SimpleReport.generate(products)
        else:
            return CompleteReport.generate(products)
