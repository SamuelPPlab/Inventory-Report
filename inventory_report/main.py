import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def Importer(path):
    if ".csv" in path:
        return InventoryRefactor(CsvImporter)
    elif ".json" in path:
        return InventoryRefactor(JsonImporter)
    elif ".xml" in path:
        return InventoryRefactor(XmlImporter)


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    _unknown, path, type = sys.argv

    data = Importer(path).import_data(path, type)

    print(data, end="")
