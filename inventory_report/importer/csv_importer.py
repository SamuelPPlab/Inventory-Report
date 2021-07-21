from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path_name):
        if ".csv" in path_name:
            with open(path_name) as csv_file:
                cvs_reader = csv.DictReader(csv_file)
                return list(cvs_reader)
        raise ValueError("Arquivo inválido")
