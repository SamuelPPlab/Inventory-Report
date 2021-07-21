from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    list_args = sys.argv
    if len(list_args) < 3:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        path_file = list_args[1]
        type_repoter = list_args[2]

        if path_file.endswith("csv"):
            inventory_refactor = InventoryRefactor(CsvImporter)
            show_values = inventory_refactor.import_data(
                path_file, type_repoter
            )
            print(show_values, end="")
        elif path_file.endswith("xml"):
            inventory_refactor = InventoryRefactor(XmlImporter)
            show_values = inventory_refactor.import_data(
                path_file, type_repoter
            )
            print(show_values, end="")
        else:
            inventory_refactor = InventoryRefactor()
            show_values = inventory_refactor.import_data(
                path_file, type_repoter
            )
            print(show_values, end="")
