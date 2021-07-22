import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path_document, type_of_document):
        report = ''
        file_in_dict = []

        with open(path_document) as f:
            file_in_dict = [row for row in csv.DictReader(f)]

        if type_of_document == "simples":
            report = SimpleReport.generate(file_in_dict)
        if type_of_document == "completo":
            report = CompleteReport.generate(file_in_dict)
        return report
