from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    path = sys.argv[1]
    file_type = path.split(".")[-1]
    report_type = sys.argv[2]
    file_type_method = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }

    instance = InventoryRefactor(file_type_method[file_type])
    print(instance.import_data(path, report_type), end="")
