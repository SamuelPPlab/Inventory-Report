import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


def handle_csv(file_path):
    # https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
    # Simon
    with open(file_path) as cvs_file:
        cvs_reader = csv.DictReader(cvs_file)
        return list(cvs_reader)


def handle_json(file_path):
    with open(file_path) as json_file:
        json_reader = json_file.read()
        return json.loads(json_reader)


def handle_xml(file_path):
    # https://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
    # https://stackoverflow.com/questions/60805355/convert-xml-to-list-of-dictionaries-in-python
    # pradeep
    tree = ET.parse(file_path)
    root = tree.getroot()
    xml_result = []

    for item in root.findall('./record'):
        curr_dict = {}

        for child in item:
            curr_dict[child.tag] = child.text

        xml_result.append(curr_dict)

    return xml_result


class Inventory:
    def import_data(file_path, type_report):
        result = []
        if ".csv" in file_path:
            result = handle_csv(file_path)

        if ".json" in file_path:
            result = handle_json(file_path)

        if ".xml" in file_path:
            result = handle_xml(file_path)

        if type_report == 'simples':
            return SimpleReport.generate(result)
        else:
            return CompleteReport.generate(result)


cvs_path = "./inventory_report/data/inventory.csv"
json_path = "./inventory_report/data/inventory.json"
xml_path = "./inventory_report/data/inventory.xml"

Inventory.import_data(file_path=cvs_path, type_report="simples")
Inventory.import_data(file_path=cvs_path, type_report="completo")
Inventory.import_data(file_path=json_path, type_report="simples")
Inventory.import_data(file_path=json_path, type_report="completo")
Inventory.import_data(file_path=xml_path, type_report="simples")
Inventory.import_data(file_path=xml_path, type_report="completo")
