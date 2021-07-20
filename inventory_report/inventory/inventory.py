from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# https://docs.python.org/pt-br/3/library/csv.html?highlight=csv
import csv
# https://docs.python.org/pt-br/3/library/json.html?highlight=json
import json
# https://docs.python.org/pt-br/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        if file_path.endswith('.csv'):
            file = cls.read_file_csv(file_path)
        if file_path.endswith('.json'):
            file = cls.read_file_json(file_path)
        if file_path.endswith('.xml'):
            file = cls.read_file_xml(file_path)

        if report_type == "simples":
            report = SimpleReport.generate(file)
        else:
            report = CompleteReport.generate(file)

        return report

    @classmethod
    def read_file_csv(cls, file_path):
        with open(file_path) as file_csv:
            file = csv.DictReader(file_csv)
            return list(file)

    @classmethod
    def read_file_json(cls, file_path):
        with open(file_path) as file_json:
            file = json.load(file_json)
            return file

    @classmethod
    def read_file_xml(cls, file_path):
        root = ET.parse(file_path).getroot()
        file = []
        for child in root:
            file_dict = {}
            for tag in child:
                file_dict[tag.tag] = tag.text
            file.append(file_dict)
        return file
