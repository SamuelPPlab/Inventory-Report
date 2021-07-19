import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    path, report_type = sys.argv[1:]
    file_type = path.split(".")[-1]

    inventory = InventoryRefactor()
    if file_type == "csv":
        inventory.importer = CsvImporter
        report = inventory.import_data(path, report_type)
        print(report[:-1])
    elif file_type == "json":
        inventory.importer = JsonImporter
        report = inventory.import_data(path, report_type)
        print(report[:-1])
    elif file_type == "xml":
        inventory.importer = XmlImporter
        report = inventory.import_data(path, report_type)
        print(report[:-1])
