from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file_path):
        if file_path.endswith("xml"):
            with open(file_path, 'r') as xml_file:
                content = xmltodict.parse(xml_file.read())
                converted_content = content["dataset"]["record"]
                return converted_content
        else:
            raise ValueError("Arquivo inválido")
