from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_name):
        if file_name.endswith('.csv'):
            file_csv = Inventory.read_file_csv(file_name)
            return file_csv

        raise ValueError("Arquivo inválido")
