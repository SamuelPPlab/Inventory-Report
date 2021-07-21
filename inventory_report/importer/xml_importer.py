from inventory_report.importer.importer import Importer
import pathlib
import xmltodict
import ast
import json


class XmlImporter(Importer):
    def import_data(file):
        data = []
        with open(file, mode="r") as xml_file:
            if pathlib.Path(xml_file.name).suffix != "xml":
                raise ValueError("Arquivo inválido")
            xml_reader = xmltodict.parse(xml_file.read())
            xml_to_json = json.dumps(xml_reader)
            xml_dict = ast.literal_eval(xml_to_json)["dataset"]["record"]
            data = xml_dict

        return data
