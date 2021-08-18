from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET
import json
import csv

""" REF:
https://docs.python.org/3/library/xml.etree.elementtree.html
"""


class Inventory:

    @staticmethod
    def archive_xml(file):
        root = ET.parse(file).getroot()
        """ Encontra todas as chaves records dentro do XML """
        all_records = root.findall("record")
        inventory = []
        for records in all_records:
            file_dict = {}
            for tag in records:
                file_dict[tag.tag] = tag.text
            inventory.append(file_dict)
        return inventory

    @staticmethod
    def archive_csv(path):
        with open(path) as file:
            converted_csv_file = csv.DictReader(file, delimiter=",")
            inventory = [row for row in converted_csv_file]
        return inventory

    @staticmethod
    def archive_json(path):
        with open(path) as file:
            inventory = json.load(file)
        return inventory

    @classmethod
    def path_analyze(cls, path):
        if path.endswith(".csv"):
            itens = cls.archive_csv(path)
        elif path.endswith(".json"):
            itens = cls.archive_json(path)
        else:
            itens = cls.archive_xml(path)
        return itens

    @classmethod
    def import_data(cls, path, type):
        inventory = cls.path_analyze(path)
        if type == "simples":
            return SimpleReport.generate(inventory)

        if type == "completo":
            return CompleteReport.generate(inventory)
