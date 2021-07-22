from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    def import_data(file_name):
        if file_name.count('csv') != 0:
            with open(file_name, newline="") as csvfile:
                doc_reader = csv.DictReader(csvfile)
                data_csv = list((item for item in doc_reader))
                return data_csv
        else:
            raise ValueError('Arquivo inválido')
