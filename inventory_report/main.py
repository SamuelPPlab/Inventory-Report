from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    file_type = sys.argv[1][-3:]
    if file_type == "csv":
        inventory_report_maker = InventoryRefactor(CsvImporter)
    elif file_type == "xml":
        inventory_report_maker = InventoryRefactor(XmlImporter)
    else:
        inventory_report_maker = InventoryRefactor(JsonImporter)
    print(inventory_report_maker.import_data(sys.argv[1], sys.argv[2]), end="")


if __name__ == "__main__":
    main()
