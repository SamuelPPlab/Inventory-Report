import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class Inventory:

    def csv_report(path_document, type_of_document):
        report = ''
        file_in_dict = []
        with open(path_document) as f:
            file_in_dict = [row for row in csv.DictReader(f)]
        if type_of_document == "simples":
            report = SimpleReport.generate(file_in_dict)
        if type_of_document == "completo":
            report = CompleteReport.generate(file_in_dict)
        return report

    def json_report(path_document, type_of_document):
        report = ''
        file_in_dict = []
        with open(path_document) as f:
            file_in_dict = json.load(f)
        if type_of_document == "simples":
            report = SimpleReport.generate(file_in_dict)
        if type_of_document == "completo":
            report = CompleteReport.generate(file_in_dict)
        return report
    
    def xml_report(path_document, type_of_document):
        report = ''
        file_in_dict = []
        with open(path_document) as f:
            doc = xmltodict.parse(f.read())
            # print("DOCUMENTO:", )
            all_product = doc["dataset"]["record"]
            file_in_dict = [
                {
                    item: product[item]
                    for item in product 
                }
                for product in all_product
            ]
 
        if type_of_document == "simples":
            report = SimpleReport.generate(file_in_dict)
        if type_of_document == "completo":
            report = CompleteReport.generate(file_in_dict)
        return report

    @classmethod
    def import_data(cls, path_document, type_of_document):
        report = ''
        if path_document.endswith(".csv"):
            report = Inventory.csv_report(path_document, type_of_document)
        elif path_document.endswith('.json'):
            report = Inventory.json_report(path_document, type_of_document)
        elif path_document.endswith('.xml'):
            report = Inventory.xml_report(path_document, type_of_document)
        return report

if __name__ == "__main__": 
    inventory_test = Inventory()
    inventory_test.import_data("inventory_report/data/inventory.xml", "simples")
        
