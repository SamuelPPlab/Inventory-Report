import csv
import json
from xml_to_dict import XMLtoDict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        file_type = path.split(".")[-1]
        file_type_method = {"csv": cls.csv, "json": cls.json, "xml": cls.xml}
        report_method = {"simples": SimpleReport, "completo": CompleteReport}
        data = file_type_method[file_type](path)

        return report_method[report_type].generate(data)

    @staticmethod
    def csv(path):
        with open(path, newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data_csv = list(data for data in reader)

        return data_csv

    @staticmethod
    def json(path):
        with open(path) as json_file:
            data_json = json.load(json_file)

        return data_json

    @staticmethod
    def xml(path):
        parser = XMLtoDict()
        with open(path) as xml_file:
            data = xml_file.read()
            data_xml = parser.value_from_nest("record", data)

        return data_xml
