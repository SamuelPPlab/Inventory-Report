from xml_to_dict import XMLtoDict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        parser = XMLtoDict()
        with open(path) as xml_file:
            data_xml = xml_file.read()
            data = parser.value_from_nest("record", data_xml)

        return data
