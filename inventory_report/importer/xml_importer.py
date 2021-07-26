import xmltodict
import json
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.split('.')[1] != 'xml':
            raise ValueError('Arquivo inválido')

        with open(file_name) as file:
            report_list = xmltodict.parse(file.read())
            json_data = json.loads(json.dumps(report_list))

            return json_data['dataset']['record']
