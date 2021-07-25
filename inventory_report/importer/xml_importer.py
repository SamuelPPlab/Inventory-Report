import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file_name):
        with open(file_name, 'r') as content_file:
            if file_name.endswith(".xml"):
                xml2dict = xmltodict.parse(content_file.read())
                result_format = xml2dict["dataset"]["record"]
                return result_format
            else:
                raise ValueError("Arquivo inválido")
