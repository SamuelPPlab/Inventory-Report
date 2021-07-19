from datetime import datetime
from collections import Counter

class SimpleReport:
  def __init__(self):
    pass
  
  def generate(inv_products):
    fabrication = sorted(inv_products, key=lambda row:row['data_de_fabricacao'])[0]["data_de_fabricacao"]
    valid_date = calculate_min_validation_date(inv_products)
    company = most_inventory_company(inv_products)
    
    final_report = (f"""Data de fabricação mais antiga: {fabrication}
Data de validade mais próxima: {valid_date}
Empresa com maior quantidade de produtos estocados: {company}\n""")
  
    return final_report


def calculate_min_validation_date(stock):
  date_list = []
  min = 1000000
  min_validation_date = ""

  for item in stock:
    validation_date = item['data_de_validade']
    result =  datetime.today() - datetime.strptime(validation_date, "%Y-%m-%d")
    number_of_days = abs(int(str(result).split(" ")[0]))
    
    if number_of_days < min:
      min = number_of_days
      min_validation_date = validation_date

  return min_validation_date

def most_inventory_company(stock):
  lst = [item["nome_da_empresa"] for item in stock]
  c = Counter(lst)
  return c.most_common(1)[0][0]
    


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


# print(SimpleReport.generate(stock()))
# print(calculate_min_validation_date(stock()))
# print(most_invetory_company(stock()))