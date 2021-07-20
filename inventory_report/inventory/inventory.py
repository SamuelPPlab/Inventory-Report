from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import reader


class Inventory:
    def __init__(self):
        pass

    def import_data(file_path, report_type):
        with open(file_path, 'r') as csv_file:
            csv_reader = reader(csv_file, delimiter = ',')
            list_of_rows = list(csv_reader)
            inv_report = inv_lst_converter(list_of_rows)

        if report_type == 'simples':
          return SimpleReport.generate(inv_report)
        elif report_type == 'completo':
          return CompleteReport.generate(inv_report)


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
