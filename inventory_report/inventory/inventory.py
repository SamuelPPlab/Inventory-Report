from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
# from xml.dom import minidom
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
        xml = ET.parse(path)
        root = xml.getroot()
        lista = [
            {
                tag_item.tag: tag_item.text
                for tag_item in tag
            }
            for tag in root
        ]
        return(lista)

        # with open(path, mode="r") as file:
        #     content = minidom.parse(file)
        #     # print("XML", content[0])
        #     print(content[1])
        #     return content

    @classmethod
    def import_data(cls, path, type_report):
        list_products = list()
        if path.endswith("csv"):
            list_products = cls.reader_csv(path)
        elif path.endswith("json"):
            list_products = cls.reader_json(path)
        elif path.endswith("xml"):
            list_products = cls.reader_xml(path)

        if type_report == "simples":
            report = SimpleReport.generate(list_products)
            return report
        else:
            report = CompleteReport.generate(list_products)
            return report


if __name__ == "__main__":
    inventory = Inventory()
    inventory.import_data("inventory_report/data/inventory.xml", "simples")
