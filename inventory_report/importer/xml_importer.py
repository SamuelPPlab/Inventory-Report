from inventory_report.importer.importer import Importer
from xml_to_dict import XMLtoDict


class XmlImporter(Importer):
    def import_data(path):
        with open(path, 'r') as xml_file:
            if path.endswith("xml"):
                parser = XMLtoDict()
                xml_list = xml_file.read()
                return parser.value_from_nest("record", xml_list)
            else:
                raise ValueError('Arquivo inválido')
