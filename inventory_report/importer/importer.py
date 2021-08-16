import csv
import json
import xml.etree.ElementTree as ET


class Importer:
    def readCSV(path):
        with open(path) as arquivo:
            arquivoCSV = csv.DictReader(arquivo)
            return list(arquivoCSV)

    def readJSON(path):
        with open(path) as arquivo:
            arquivoJSON = json.load(arquivo)
            return arquivoJSON

    def readXML(path):
        with open(path) as arquivo:
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
