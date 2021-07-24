from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @classmethod
    def reports(self, data, type):
        if type == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def import_data(self, path, type):
        if path.endswith('.csv'):
            data = CsvImporter.import_data(path)
            return self.reports(data, type)