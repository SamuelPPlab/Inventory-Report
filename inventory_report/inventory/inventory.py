import csv
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Importer(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def format(self):
        raise NotImplementedError


class ImportCSV(Importer):
    def format(self):
        with open(self.path) as data:
            return [fileRow for fileRow in csv.DictReader(data)]


class ImportJSON(Importer):
    def format(self):
        with open(self.path) as data:
            return json.load(data)


class ImportXML(Importer):
    def translate(self, xml):
        products = []

        for item in xml:
            products.append({
                "id": int(item[0].text),
                "nome_do_produto": item[1].text,
                "nome_da_empresa": item[2].text,
                "data_de_fabricacao": item[3].text,
                "data_de_validade": item[4].text,
                "numero_de_serie": item[5].text,
            })

        return products

    def format(self):
        return self.translate(ET.parse(self.path).getroot())


class Inventory:
    @classmethod
    def import_data(cls, path, type="simples"):
        data = ""

        if ".csv" in path:
            data = ImportCSV(path).format()

        elif ".json" in path:
            data = ImportJSON(path).format()

        elif ".xml" in path:
            data = ImportXML(path).format()

        if type == "completo":
            return CompleteReport.generate(data)

        return SimpleReport.generate(data)
