from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        ending = file_name[-3:]
        if ending == 'csv':
            csv = Inventory.import_csv(file_name)
            return csv
        else:
            raise ValueError("Arquivo inválido")
