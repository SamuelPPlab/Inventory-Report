import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def import_instance(file):
    if ".csv" in file:
        return InventoryRefactor(CsvImporter)
    elif ".json" in file:
        return InventoryRefactor(JsonImporter)
    elif ".xml" in file:
        return InventoryRefactor(XmlImporter)


def main():
    _, export_file, type_report = sys.argv

    if len(sys.argv) < 3:
        raise ValueError("Verifique os argumentos")

    instance = import_instance(export_file)
    instance.import_data(export_file, type_report)
    dictionary = instance.data

    if type_report == "completo":
        return CompleteReport.generate(dictionary)
    return SimpleReport.generate(dictionary)


if __name__ == "__main__":
    sys.exit(main())
