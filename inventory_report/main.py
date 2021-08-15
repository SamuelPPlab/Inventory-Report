import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    file_name = sys.argv[1]
    file_type = file_name.split(".")[-1]
    file_extension = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }
    report_type = sys.argv[2]

    instance = InventoryRefactor(file_extension[file_type])
    print(instance.import_data(file_name, report_type).rstrip("\n"))
