import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import pprint


class Inventory:
    def import_data(file_path, report_type):
        file_name, file_type = file_path.split(".")
        print(file_type)

        if file_type == "csv":
            with open(file_path) as file:
                dict_from_file = [
                    {header: row_value for header, row_value in row.items()}
                    for row in csv.DictReader(file, skipinitialspace=True)
                ]
                # https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
        elif file_type == "json":
            with open(file_path) as file:
                dict_from_file = json.load(file)
        else:
            dict_from_file = []

        if report_type == "simples":
            report = SimpleReport.generate(dict_from_file)
        elif report_type == "completo":
            report = CompleteReport.generate(dict_from_file)
        else:
            raise ValueError(
                "O tipo de relatório deve ser 'simples' ou 'completo'"
            )
        return report
        # return dict_from_file


pprint.pprint(
    Inventory.import_data("inventory_report/data/inventory.json", "simples")
)
