from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, path, relatoryType):
        dictionaryList = cls.define_and_import(path)
        if relatoryType == "simples":
            return SimpleReport.generate(dictionaryList)
        else:
            return CompleteReport.generate(dictionaryList)

    @staticmethod
    def import_csv(path):
        with open(path, "r") as file:
            dictionaty = csv.DictReader(file)
            return [row for row in dictionaty]

    @staticmethod
    def import_json(path):
        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def import_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        result = []
        for record in root.findall("record"):
            dictionary = {}
            for tag in record:
                dictionary[tag.tag] = tag.text
            result.append(dictionary)
        return result

    @classmethod
    def define_and_import(cls, path):
        if (path.endswith('.xml')):
            return cls.import_xml(path)
        elif (path.endswith('.json')):
            return cls.import_json(path)
        elif (path.endswith('.csv')):
            return cls.import_csv(path)
