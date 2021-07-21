from inventory_report.importer.importer import Importer
from csv import reader


class CsvImporter(Importer):
    def import_data(file_path):
        file_extension = file_path.split(".")[1]
        try:
            if file_extension == 'csv':
                with open(file_path, 'r') as csv_file:
                    csv_reader = reader(csv_file, delimiter=',')
                    list_of_rows = list(csv_reader)
                    inv_report = inv_lst_converter(list_of_rows)
                return inv_report
            else:
                raise ValueError
        except ValueError:
            return 'Arquivo inválido'


def inv_lst_converter(rows):
    lst = []
    for index in range(1, len(rows)):
        item = {
            "id": rows[index][0],
            "nome_do_produto": rows[index][1],
            "nome_da_empresa": rows[index][2],
            "data_de_fabricacao": rows[index][3],
            "data_de_validade": rows[index][4],
            "numero_de_serie": rows[index][5],
            "instrucoes_de_armazenamento": rows[index][6]
        }

        lst.append(item)
    return lst
