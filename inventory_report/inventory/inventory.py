import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    # https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
    # Simon
    def import_data(file_path, type_report):
        if ".csv" in file_path:
            with open(file_path) as cvs_file:
                cvs_reader = csv.DictReader(cvs_file)
                cvs_result = list(cvs_reader)
                if type_report == 'simples':
                    return SimpleReport.generate(cvs_result)
                else:
                    return CompleteReport.generate(cvs_result)

        if ".json" in file_path:
            with open(file_path) as json_file:
                json_reader = json_file.read()
                json_result = json.loads(json_reader)
                if type_report == 'simples':
                    return SimpleReport.generate(json_result)
                else:
                    return CompleteReport.generate(json_result)

        # https://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
        # https://stackoverflow.com/questions/60805355/convert-xml-to-list-of-dictionaries-in-python
        # pradeep
        if ".xml" in file_path:
            tree = ET.parse(file_path)
            root = tree.getroot()
            xml_result = []

            for item in root.findall('./record'):
                curr_dict = {}

                for child in item:
                    curr_dict[child.tag] = child.text

                xml_result.append(curr_dict)

            if type_report == 'simples':
                return SimpleReport.generate(xml_result)
            else:
                return CompleteReport.generate(xml_result)


cvs_path = "./inventory_report/data/inventory.csv"
json_path = "./inventory_report/data/inventory.json"
xml_path = "./inventory_report/data/inventory.xml"

Inventory.import_data(file_path=cvs_path, type_report="simples")
Inventory.import_data(file_path=cvs_path, type_report="completo")
Inventory.import_data(file_path=json_path, type_report="simples")
Inventory.import_data(file_path=json_path, type_report="completo")
Inventory.import_data(file_path=xml_path, type_report="simples")
Inventory.import_data(file_path=xml_path, type_report="completo")
