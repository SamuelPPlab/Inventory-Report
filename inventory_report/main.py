import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():

    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    path = sys.argv[1]
    type = sys.argv[2]

    if path.endswith(".csv"):
        inventory = InventoryRefactor(CsvImporter)
    elif path.endswith(".json"):
        inventory = InventoryRefactor(JsonImporter)
    elif path.endswith(".xml"):
        inventory = InventoryRefactor(XmlImporter)

    print(inventory.import_data(path, type), end="")
