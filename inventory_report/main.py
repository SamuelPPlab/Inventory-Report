from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    file_path = sys.argv[1]
    type_repoter = sys.argv[2]

    if file_path.endswith(".csv"):
        inventory = InventoryRefactor(CsvImporter)
    if file_path.endswith(".json"):
        inventory = InventoryRefactor(JsonImporter)
    if file_path.endswith(".xml"):
        inventory = InventoryRefactor(XmlImporter)

    print(inventory.import_data(file_path, type_repoter), end="")
