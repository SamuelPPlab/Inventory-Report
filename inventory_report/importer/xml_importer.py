from inventory_report.importer.importer import FileExtension, Importer
import xmltodict
from typing import OrderedDict
import json


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_name: str):
        file_extension: str = Importer.get_file_extension(file_name)

        if file_extension != FileExtension.XML.value:
            raise ValueError("Arquivo inválido")

        with open(file_name, "r") as file:
            data_ordered_dict: list[OrderedDict] = xmltodict.parse(file.read())
            data_json_string: json = json.dumps(data_ordered_dict)
            data: list[dict] = json.loads(data_json_string)["dataset"][
                "record"
            ]
            return data
