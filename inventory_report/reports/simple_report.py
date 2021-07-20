from datetime import datetime
from collections import Counter


class SimpleReport:
    def __init__(self):
        pass

    def generate(inv_products):
        inv_products_sorted = sorted(inv_products,
                                     key=lambda row: row['data_de_fabricacao'])
        fabrication = inv_products_sorted[0]["data_de_fabricacao"]
        valid_date = calculate_min_validation_date(inv_products)
        company = most_inventory_company(inv_products)
        final_report = (f"""Data de fabricação mais antiga: {fabrication}
Data de validade mais próxima: {valid_date}
Empresa com maior quantidade de produtos estocados: {company}\n""")
        return final_report


def calculate_min_validation_date(stock):
    min = 1000000
    min_validation_date = ""
    for item in stock:
        validation_dt = item['data_de_validade']
        result = datetime.today()-datetime.strptime(validation_dt, "%Y-%m-%d")
        number_of_days = abs(int(str(result).split(" ")[0]))
        if number_of_days < min:
            min = number_of_days
            min_validation_date = validation_dt

    return min_validation_date


def most_inventory_company(stock):
    lst = [item["nome_da_empresa"] for item in stock]
    c = Counter(lst)
    return c.most_common(1)[0][0]
