import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        try:
            data = []
            if not path.endswith('.csv'):
                raise ValueError("Arquivo inválido")
            with open(path) as file:
                report = csv.DictReader(file, delimiter=',')
                for item in report:
                    data.append(dict(item))
                return data
        except FileNotFoundError:
            raise ValueError('Arquivo não encontrado')
