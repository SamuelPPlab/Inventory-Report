from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
from xml.etree import cElementTree as ET


class Inventory:
    def import_data(path, type):
        archive = Inventory.factoryReader(path)

        return Inventory.factoryReport(type, archive)

    def factoryReader(path):
        if (path.endswith(".csv")):
            return Inventory.open_csv_archive(path)
        elif(path.endswith(".json")):
            return Inventory.open_json_archive(path)
        elif(path.endswith(".xml")):
            file = open(path)
            return Inventory.open_xml_archive(file)

    def factoryReport(type, archive):
        if(type == "simples"):
            return SimpleReport.generate(archive)
        elif(type == "completo"):
            return CompleteReport.generate(archive)

    def open_csv_archive(path):
        reader = csv.DictReader(open(path, 'r'))
        dict_list = []
        for line in reader:
            dict_list.append(line)
        return dict_list

    def open_json_archive(path):
        reader = open(path)
        return json.load(reader)

    def open_xml_archive(file):
        # Creditos ao Carlos Souza, esse cara é genial, haha o/
        tree = ET.parse(file)
        root = tree.getroot()
        result = []
        for child in root:
            result.append({tag.tag: tag.text for tag in child})
        return result
