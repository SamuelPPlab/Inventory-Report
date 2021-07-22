from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        extension = path.split(".")
        value = extension[len(extension) - 1]
        if value == "csv":
            with open(path, mode="r") as file:
                reader_file = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                data = []
                for information in reader_file:
                    data.append(information)
                return data
        else:
            raise ValueError("Arquivo inválido")


if __name__ == "__main__":
    csv1 = CsvImporter()
    csv1.import_data("./inventory_report/data/inventory.csv")
