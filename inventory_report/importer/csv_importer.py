from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    def import_data(path):
        file_type = path[-3:]
        if file_type != "csv":
            raise ValueError("Arquivo inválido")
        return Inventory.read_csv(path)
