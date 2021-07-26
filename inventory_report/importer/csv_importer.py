from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = file_path.split('.')[1]
        if extension != 'csv':
            raise ValueError('Arquivo inválido')
        else:
            data = []
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        return data


# x = CsvImporter()
# print(x.import_data(
#     "/home/vanderson/Trybe/projetos_trybe/BLOCO_36_T6/sd-06-inventory-report/inventory_report/data/inventory.csv",
# ))
