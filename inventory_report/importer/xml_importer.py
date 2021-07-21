from inventory_report.importer.importer import Importer
import xml.etree.cElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_type = cls.check_file_type_in_path(path)
        if file_type == "xml":
            tree = ET.parse(path)
            root = tree.getroot().findall("record")
            lista = []
            for tag in root:
                dicionario = {}
                for item in tag:
                    dicionario[item.tag] = item.text
                lista.append(dicionario)
        else:
            raise ValueError("Arquivo inválido")
        return lista

    @staticmethod
    def check_file_type_in_path(path):
        return path.split(".")[1]
