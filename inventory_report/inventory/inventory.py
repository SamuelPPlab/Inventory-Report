import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def __init__(self, csv):
        pass

    def import_data(path, type):
        with open(path, "r") as file:
            ending = path[-3:]
            if ending == 'csv':
                result = [row for row in csv.DictReader(file)]
                if type == "simples":
                    return SimpleReport.generate(result)
                return CompleteReport.generate(result)
            if ending == 'son':
                result = json.load(file)
                if type == "simples":
                    return SimpleReport.generate(result)
                return CompleteReport.generate(result)
            if ending == 'xml':
                root = ET.parse(path).getroot()
                registers = root.findall("record")
                result = []
                for register in registers:
                    file_dict = {}
                    for tag in register:
                        file_dict[tag.tag] = tag.text
                    result.append(file_dict)
                if type == "simples":
                    return SimpleReport.generate(result)
                return CompleteReport.generate(result)


# pathTest = 'inventory_report/data/inventory.csv'
# def teste(pathTest):
#     with open(pathTest, "r") as file:
#         result = [row for row in csv.DictReader(file)]
#         return result
# print(Inventory.import_data(pathTest, csv))
# print(teste(pathTest))
