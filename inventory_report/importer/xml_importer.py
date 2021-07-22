from inventory_report.importer.importer import Importer
from xml_to_dict import XMLtoDict


class XmlImporter(Importer):

    def import_data(file_name):
        if file_name.count('xml') != 0:
            with open(file_name) as xml_file:
                xml_read = xml_file.read()
                parser = XMLtoDict()
                response = parser.value_from_nest('.*ecord', xml_read)
                return response
        else:
            raise ValueError('Arquivo inválido')
