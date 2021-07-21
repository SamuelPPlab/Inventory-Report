from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:

    def reader_csv(path):
        with open(path, mode="r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            list_products = [row for row in content]
            print("CSV", list_products[0])
            return list_products

    def reader_json(path):
        with open(path, mode="r") as file:
            content = json.load(file)
            print("JSON", content[0])
            return content

    def reader_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        list_products = [
            {
                tag.tag: tag.text
                for tag in child
            }
            for child in root
        ]
        print("XML", list_products[0])
        return list_products

    @classmethod
    def import_data(cls, path, type_report):
        list_products = list()
        if path.endswith("csv"):
            list_products = cls.reader_csv(path)
        elif path.endswith("json"):
            list_products = cls.reader_json(path)
        elif path.endswith('xml'):
            list_products = cls.reade_rxml(path)

        if type_report == "simples":
            report = SimpleReport.generate(list_products)
            return report
        else:
            report = CompleteReport.generate(list_products)
            return report


if __name__ == "__main__":
    inventory = Inventory()
    inventory.import_data("data/inventory.json", "simples")
