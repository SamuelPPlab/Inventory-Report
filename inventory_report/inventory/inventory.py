import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def __init__(self, csv):
        pass

    @classmethod
    def import_data(cls, path, report):
        ending = path[-3:]
        if ending == 'xml':
            data = cls.import_xml(path)
        if ending == 'son':
            data = cls.import_json(path)
        if ending == 'csv':
            data = cls.import_csv(path)
        if report == "simples":
            report = SimpleReport.generate(data)
        else:
            report = CompleteReport.generate(data)
        return report

    @classmethod
    def import_json(cls, path):
        with open(path) as json_file:
            file = json.load(json_file)
            return file

    @classmethod
    def import_csv(cls, path):
        with open(path) as csv_file:
            file = csv.DictReader(csv_file)
            return list(file)

    @classmethod
    def import_xml(cls, path):
        root = ET.parse(path).getroot()
        registers = root.findall("record")
        result = []
        for register in registers:
            file_dict = {}
            for tag in register:
                file_dict[tag.tag] = tag.text
            result.append(file_dict)
        return result
