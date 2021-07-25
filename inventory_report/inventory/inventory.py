import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self, file_path, file_type):
        self.file_path = file_path
        self.file_type = file_type

    @classmethod
    def files_format(cls, file_path):
        with open(file_path, 'r') as content_file:
            if file_path.endswith(".csv"):
                csv_importer = csv.DictReader(content_file)
                return list(csv_importer)
            elif file_path.endswith(".json"):
                return json.load(content_file)
            elif file_path.endswith(".xml"):
                xml2dict = xmltodict.parse(content_file.read())
                return xml2dict["dataset"]["record"]
            # Ref. working with xml: https://bit.ly/2Vc7fuS
            else:
                return None

    @classmethod
    def import_data(cls, file_path, file_type):
        data = cls.files_format(file_path)

        if file_type == 'simples':
            return SimpleReport.generate(data)
        elif file_type == 'completo':
            return CompleteReport.generate(data)
        else:
            return None
