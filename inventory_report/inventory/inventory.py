from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import csv


class Inventory:
    @classmethod
    def import_data(self, file_path, type):
        iterable_data = self.file_reader(file_path)
        if type == 'simples':
            return SimpleReport.generate(iterable_data)
        elif type == 'completo':
            return CompleteReport.generate(iterable_data)

    @classmethod
    def file_reader(self, file_path):
        with open(file_path) as file:
            if '.csv' in file_path:
                read_file = csv.DictReader(file)
                return [item for item in read_file]
            if '.json' in file_path:
                return json.load(file)
