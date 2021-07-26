from inventory_report.importer.importer import Importer
import xmltodict
import json


class XmlImporter(Importer):
    def import_data(path):
        if path.split(".")[1] == "xml":
            with open(path, mode="r") as file:
                xml_file = file.read()
                list = json.dumps(xmltodict.parse(xml_file))
                result = json.loads(list)  # loads @vanderson-henrique
                final_list = result["dataset"]["record"]
            return final_list
        else:
            raise ValueError("Arquivo inválido")
