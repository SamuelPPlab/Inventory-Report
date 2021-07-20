import json
import pathlib
import xmltodict
import ast
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file_to_read):
        data = []
        with open(file_to_read, 'r') as file:
            if pathlib.Path(file.name).suffix != '.xml':
                raise ValueError("Arquivo inválido")
            xmlReader = xmltodict.parse(file.read())
            xmlToJSON = json.dumps(xmlReader)
            xmlDict = ast.literal_eval(xmlToJSON)['dataset']['record']
            data = xmlDict
        return data
