from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import sys


def load_data(path, report_type):
    if path.endswith('.csv'):
        inventory = InventoryRefactor(CsvImporter)
    elif path.endswith('.json'):
        inventory = InventoryRefactor(JsonImporter)
    elif path.endswith('.xml'):
        inventory = InventoryRefactor(XmlImporter)
    inventory.import_data(path, report_type)
    return inventory.data


def print_report(data, report_type):
    if report_type == 'simples':
        print(SimpleReport.generate(data))
    elif report_type == 'completo':
        print(CompleteReport.generate(data))


def main():
    try:
        if len(sys.argv) < 3:
            raise Exception('Verifique os argumentos')

        _, path, report_type = sys.argv
        data = load_data(path, report_type)
        print_report(data, report_type)
    except Exception as exc:
        print(exc, file=sys.stderr)
