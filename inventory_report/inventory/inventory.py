import json
import pathlib
import xmltodict
import ast
from csv import DictReader
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self, receive_file, report_type):
        self.file = receive_file
        self.report_type = report_type

    @classmethod
    def read_extension_file(cls, file_to_read):
        data = []
        with open(file_to_read, 'r') as file:
            if pathlib.Path(file.name).suffix == '.json':
                data = json.load(file)
            elif pathlib.Path(file.name).suffix == '.csv':
                csvReader = DictReader(file)
                for rows in csvReader:
                    data.append(rows)
            elif pathlib.Path(file.name).suffix == '.xml':
                xmlReader = xmltodict.parse(file.read())
                xmlToJSON = json.dumps(xmlReader)
                xmlDict = ast.literal_eval(xmlToJSON)['dataset']['record']
                data = xmlDict
        return data

    @classmethod
    def import_data(cls, receive_file, report_type):
        data = cls.read_extension_file(receive_file)

        if report_type == 'simples':
            return SimpleReport.generate(data)
        elif report_type == 'completo':
            return CompleteReport.generate(data)
