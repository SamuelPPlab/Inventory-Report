import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_file(file_path):
        file_type = file_path.split(".")[-1]
        if file_type == "csv":
            return Inventory.import_csv(file_path)
        elif file_type == "json":
            return Inventory.import_json(file_path)
        elif file_type == "xml":
            return Inventory.import_xml(file_path)
        else:
            return []

    @staticmethod
    def import_csv(file_path):
        with open(file_path) as file:
            dict_from_csv = [
                {header: row_value for header, row_value in row.items()}
                for row in csv.DictReader(file, skipinitialspace=True)
            ]
            # https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
        return dict_from_csv

    @staticmethod
    def import_json(file_path):
        with open(file_path) as file:
            return json.load(file)

    @staticmethod
    def import_xml(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        records = list(root)
        elements = [list(record) for record in records]
        dict_from_xml = [
            {item.tag: item.text for item in element} for element in elements
        ]
        return dict_from_xml

    @staticmethod
    def generate_report(data_dict, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data_dict)
        elif report_type == "completo":
            return CompleteReport.generate(data_dict)
        else:
            raise ValueError(
                "O tipo de relatório deve ser 'simples' ou 'completo'"
            )

    @staticmethod
    def import_data(file_path, report_type):
        data_dict = Inventory.import_file(file_path)
        report = Inventory.generate_report(data_dict, report_type)
        return report
