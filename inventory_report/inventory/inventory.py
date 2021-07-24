from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:

    @classmethod
    def import_data(cls, file_path, report_type):
        report = cls.open_csv(file_path)
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
