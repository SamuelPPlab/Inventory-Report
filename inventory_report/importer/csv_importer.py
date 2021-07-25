from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(arq):
        Importer.validate_extension(arq, "csv")
        with open(arq, "r") as content:
            result = csv.DictReader(content)
            result_final = [linha for linha in result]
            return result_final
