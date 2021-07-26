from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = file_path.split('.')[1]
        if extension != 'json':
            raise ValueError('Arquivo inválido')
        else:
            with open(file_path, "r") as file:
                data = json.load(file)
        return data


# x = JsonImporter()
# print(x.import_data(
#     "/home/vanderson/Trybe/projetos_trybe/BLOCO_36_T6/sd-06-inventory-report/inventory_report/data/inventory.json",
# ))
