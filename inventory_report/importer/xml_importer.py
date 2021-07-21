from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file_path):
        file_extension = file_path.split(".")[1]
        try:
            if file_extension == 'xml':
                with open(file_path, 'r') as xml_file:
                    content = xml_file.read()
                    d = xmltodict.parse(content)
                    group = [dict(i) for i in d['dataset']['record']]
                return group
            else:
                raise ValueError
        except ValueError:
            return 'Arquivo inválido'
