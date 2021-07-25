
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    def generate_report_CSV(file_path, report_type):
        with open(file_path, 'r') as csv_file:
            content = csv.DictReader(csv_file)
            converted_content = list(content)
            if report_type == 'simples':
                return SimpleReport.generate(converted_content)
            elif report_type == 'completo':
                return CompleteReport.generate(converted_content)

    def import_data(file_path, report_type):
        if file_path.endswith('csv'):
            return Inventory.generate_report_CSV(file_path, report_type)
