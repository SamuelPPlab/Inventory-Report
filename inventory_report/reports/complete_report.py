from inventory_report.reports.simple_report import SimpleReport
from collections import Counter

class CompleteReport(SimpleReport):
  def __init__(self):
    super().__init__(self)
  
  def generate(inv_products):
    simple_report = SimpleReport.generate(inv_products)

    most_common = inventory_per_company(inv_products)

    bottom_report = (f"""Produtos estocados por empresa: 
- {most_common[1][0]}: {most_common[1][1]}
- {most_common[0][0]}: {most_common[0][1]}
- {most_common[2][0]}: {most_common[2][1]}\n""")


    return simple_report + "\n" + bottom_report
    




def inventory_per_company(stock):
  lst = [item["nome_da_empresa"] for item in stock]
  report = Counter(lst)
  return report.most_common()

def stock():
    stock =  [
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
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]

    return stock


print(CompleteReport.generate(stock()))


