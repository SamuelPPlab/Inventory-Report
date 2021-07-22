from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def read_csv(path, type):
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            a = list(reader)
            if (type == 'simples'):
                return SimpleReport.generate(a)
            if (type == 'completo'):
                return CompleteReport.generate(a)

    def read_json(path, type):
        with open(path) as jsonfile:
            reader = json.load(jsonfile)
            if (type == 'simples'):
                return SimpleReport.generate(reader)
            if (type == 'completo'):
                return CompleteReport.generate(reader)

    def read_xml(path, type):
        with open(path) as xmlfile:
            reader = xmltodict.parse(xmlfile.read())
            xml_to_json = json.dumps(reader)
            doc = json.loads(xml_to_json)['dataset']['record']
            if (type == 'simples'):
                return SimpleReport.generate(doc)
            if (type == 'completo'):
                return CompleteReport.generate(doc)

    def import_data(path, type):
        if path.endswith('csv'):
            return Inventory.read_csv(path, type)
        if path.endswith('json'):
            return Inventory.read_json(path, type)
        if path.endswith('xml'):
            return Inventory.read_xml(path, type)
