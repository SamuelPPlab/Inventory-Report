from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
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
      