from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import csv
import xmldict
import xml.etree.ElementTree as ET


class Inventory:
    def import_data(path, type):
        products = []
        if path.endswith(".json"):
            products = json.load(open(path))
        if path.endswith(".csv"):
            products_obj = csv.DictReader(open(path))
            products = list(products_obj)
        if path.endswith(".xml"):
            tree = ET.parse(open(path))
            root = tree.getroot()
            products = xmldict.xml_to_dict(root)["dataset"]["record"]

        if type == "simples":
            return SimpleReport.generate(products)
        else:
            return CompleteReport.generate(products)
