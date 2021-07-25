from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET



class XmlImporter(Importer):
    def import_data(arq):
        with open(arq, "r") as content:
            result = xmltodict.parse(content.read())
            result_final = [dict(linha) for linha in result["dataset"]["record"]]
            return result_final
