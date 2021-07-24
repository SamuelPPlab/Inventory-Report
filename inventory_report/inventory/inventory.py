from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:

    @classmethod
    def import_data(cls, file_path, report_type):
        if file_path.endswith('.csv'):
            report = cls.open_csv(file_path)
        if file_path.endswith('.json'):
            report = cls.open_json(file_path)
        if report_type == "simples":
            data = SimpleReport.generate(report)
        else:
            data = CompleteReport.generate(report)
        return data

    @classmethod
    def open_csv(cls, file_path):
        with open(file_path) as c_file:
            file = csv.DictReader(c_file)
            return list(file)

    @classmethod
    def open_json(cls, file_path):
        with open(file_path) as j_file:
            file = json.load(j_file)
            return file

    
