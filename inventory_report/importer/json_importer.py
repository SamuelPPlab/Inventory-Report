from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        extension = path.split(".")
        value = extension[len(extension) - 1]
        if value == "json":
            with open(path, mode="r") as file:
                reader_file = json.load(file)
                data = []
                for information in reader_file:
                    data.append(information)
                return data
        else:
            raise ValueError("Arquivo inválido")


if __name__ == "__main__":
    csv1 = JsonImporter()
    csv1.import_data("./inventory_report/data/inventory.json")
