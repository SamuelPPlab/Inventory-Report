import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.split('.')[1] != 'csv':
            raise ValueError('Arquivo inválido')

        report_list = []
        with open(file_name) as file:
            data = csv.DictReader(file)
            for rows in data:
                report_list.append(rows)
        return report_list
