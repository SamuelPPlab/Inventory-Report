from inventory_report.importer.importer import Importer
import xmltodict
import json


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = file_path.split('.')[1]
        if extension != 'xml':
            raise ValueError('Arquivo inválido')
        else:
            with open(file_path, 'r') as file:
                read = file.read()
                data_xml = xmltodict.parse(read)
                data_json = json.dumps(data_xml)
                result = json.loads(data_json)
                data = result["dataset"]["record"]
        return data


# x = XmlImporter()
# print(x.import_data(
#     "/home/vanderson/Trybe/projetos_trybe/BLOCO_36_T6/sd-06-inventory-report/inventory_report/data/inventory.xml",
# ))
