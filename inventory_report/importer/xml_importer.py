from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            xml_to_dict = xmltodict.parse(file.read())
            data = xml_to_dict["dataset"]["record"]
            return data
