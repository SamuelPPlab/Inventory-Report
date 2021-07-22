from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')
        csv_to_dict = csv.DictReader(open(path))
        convert_to_list = list(csv_to_dict)
        return convert_to_list
