import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def readCSV(self, caminho):
        with open(caminho) as arquivo:
            arquivoCSV = csv.DictReader(arquivo)
            return list(arquivoCSV)

    @classmethod
    def readJSON(self, caminho):
        with open(caminho) as arquivo:
            arquivoJSON = json.load(arquivo)
            return arquivoJSON

    @classmethod
    def readXML(self, caminho):
        with open(caminho) as arquivo:
            relatorio = []
            elementos = ET.parse(arquivo)
            root = elementos.getroot()
            for elemento in root.iter("record"):
                item = {}
                for filho in elemento.iter("*"):
                    if filho.tag != "record":
                        item[filho.tag] = filho.text
                relatorio.append(item)
            return relatorio

    @classmethod
    def import_data(self, caminho, tipo):
        if caminho.endswith(".csv"):
            conteudo = self.readCSV(caminho)
        if caminho.endswith(".json"):
            conteudo = self.readJSON(caminho)
        if caminho.endswith(".xml"):
            conteudo = self.readXML(caminho)
        if tipo == "simples":
            relatorio = SimpleReport.generate(conteudo)
        else:
            relatorio = CompleteReport.generate(conteudo)
        return relatorio
