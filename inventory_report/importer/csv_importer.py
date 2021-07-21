from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @classmethod
    def import_data(self, path):
        if (path.endswith('.csv')):
            self.data = []
            with open(path) as file:
                inventory_csv = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = inventory_csv
                lista = list(map(lambda produto: {
                    header[0]: produto[0],
                    header[1]: produto[1],
                    header[2]: produto[2],
                    header[3]: produto[3],
                    header[4]: produto[4],
                    header[5]: produto[5],
                    header[6]: produto[6]},
                    data))
            return lista
        else:
            raise Exception('Arquivo incorreto')
