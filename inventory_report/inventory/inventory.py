from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xmltodict


class Inventory():
    def xmlToJson(file_path):
        with open(file_path) as file:
            report_list = xmltodict.parse(file.read())
            json_data = json.loads(json.dumps(report_list))

            return json_data['dataset']['record']

    def cvsToJson(file_path):
        report_list = []
        with open(file_path) as file:
            print('aqui!!')
            data = csv.DictReader(file)
            for rows in data:
                report_list.append(rows)
        return report_list

    def readJsonFile(file_path):
        with open(file_path) as file:
            file_read = file.read()
            data = json.loads(file_read)
            return data

    @classmethod
    def import_data(cls, file_path, report_type='simples'):
        report_list = []
        file_extension = file_path.split('.')[1]

        print(file_extension)
        if (file_extension == 'csv'):
            report_list = cls.cvsToJson(file_path)
        elif (file_extension == 'xml'):
            report_list = cls.xmlToJson(file_path)
        else:
            report_list = cls.readJsonFile(file_path)

        if (report_type == 'simples'):
            return SimpleReport.generate(report_list)
        elif (report_type == 'completo'):
            return CompleteReport.generate(report_list)
        else:
            return None


# print(Inventory.import_data('inventory_report/data/inventory.xml', 'completo'))
