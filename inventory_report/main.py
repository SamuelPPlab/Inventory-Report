# def main():
#     pass

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    file = sys.argv[1]
    type_repoter = sys.argv[2]

    if file.endswith(".csv"):
        inventory_data = InventoryRefactor(CsvImporter)
    if file.endswith(".json"):
        inventory_data = InventoryRefactor(JsonImporter)
    if file.endswith(".xml"):
        inventory_data = InventoryRefactor(XmlImporter)

    print(inventory_data.import_data(file, type_repoter), end="")
