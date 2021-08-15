import xmltodict

from .importer import Importer


class XmlImporter(Importer):
    def import_data(file_name):
        if file_name.endswith(".xml"):
            with open(file_name) as file:
                result = xmltodict.parse(file.read())["dataset"]["record"]
                return result
        else:
            raise ValueError("Arquivo inválido")
