import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def import_instance(file):
    if ".csv" in file:
        return InventoryRefactor(CsvImporter)
    elif ".json" in file:
        return InventoryRefactor(JsonImporter)
    elif ".xml" in file:
        return InventoryRefactor(XmlImporter)


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
        # print("Verifique os argumentos", file=sys.stderr)
    else:
        _, export_file, type_report = sys.argv
        instance = import_instance(export_file)
        result = instance.import_data(export_file, type_report)
        print(result, end="")


if __name__ == "__main__":
    sys.exit(main())

# ('Data de fabricação mais antiga: 2019-09-06\n'\n
# 'Data de validade mais próxima: 2022-09-17\n'\n
# 'Empresa com maior quantidade de produtos estocados: Target Corporation\n')
# ('Data de fabricação mais antiga: 2019-09-06\n'\n
# 'Data de validade mais próxima: 2022-09-17\n'\n
# 'Empresa com maior quantidade de produtos estocados:
#  Target Corporation\n'\n '\n')
