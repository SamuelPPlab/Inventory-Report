import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    args = sys.argv

    if len(args) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    _, file_name, report_type = args

    file_type = file_name.split(".")[-1]

    # Vai virar um adapter
    inventory = None
    if file_type == "csv":
        inventory = InventoryRefactor(CsvImporter)
    if file_type == "json":
        inventory = InventoryRefactor(JsonImporter)
    if file_type == "xml":
        inventory = InventoryRefactor(XmlImporter)

    inventory.import_data(file_name, report_type)

    report = inventory.import_report(report_type)

    print(report, end="")
