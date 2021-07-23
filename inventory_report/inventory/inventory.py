import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def __init__(self, csv):
        pass

    def import_xml(path):
        root = ET.parse(path).getroot()
        registers = root.findall("record")
        result = []
        for register in registers:
            file_dict = {}
            for tag in register:
                file_dict[tag.tag] = tag.text
            result.append(file_dict)
        return result

    def import_data(path, type):
        with open(path, "r") as file:
            ending = path[-4:]
            result = ''
            if ending == '.csv':
                result = [row for row in csv.DictReader(file)]
            if ending == 'json':
                result = json.load(file)
            if ending == '.xml':
                result = Inventory.import_xml(path)
            if type == "simples":
                return SimpleReport.generate(result)
            return CompleteReport.generate(result)
