import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    else:
        if (sys.argv[1].endswith('.xml')):
            instance = InventoryRefactor(XmlImporter)
        elif (sys.argv[1].endswith('.json')):
            instance = InventoryRefactor(JsonImporter)
        elif (sys.argv[1].endswith('.csv')):
            instance = InventoryRefactor(CsvImporter)
        print(instance.import_data(sys.argv[1], sys.argv[2]), end="")


if __name__ == "__main__":
    main()
