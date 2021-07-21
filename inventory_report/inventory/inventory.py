from abc import ABC
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory(ABC):
    @classmethod
    def import_data(cls, path, report_type):
        dictionary = cls.csv_reader(path)        
        if (report_type == 'simples'):
            result = SimpleReport.generate(dictionary)
        elif (report_type == 'completo'):
            result = CompleteReport.generate(dictionary)
        return result

    @staticmethod
    def csv_reader(path):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)       
            lista = []
            for row in reader:
                lista.append({
                    'id': row['id'], 
                    'nome_do_produto': row['nome_do_produto'],
                    "nome_da_empresa": row['nome_da_empresa'],
                    "data_de_fabricacao": row['data_de_fabricacao'],
                    "data_de_validade": row['data_de_validade'],
                    "numero_de_serie": row['numero_de_serie'],
                    "instrucoes_de_armazenamento": row[
                        'instrucoes_de_armazenamento'],
                })
            return lista

if __name__ == '__main__':
    teste = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]
    Inventory.import_data('inventory_report/data/inventory.csv', 'simples')
