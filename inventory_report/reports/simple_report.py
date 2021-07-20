from statistics import mode
from datetime import date


class SimpleReport:
    def generate(data):

        earliest_manufacturing_date = min(
          [item["data_de_fabricacao"] for item in data])

        # https://stackoverflow.com/questions/3922644/find-oldest-youngest-datetime-object-in-a-list
        now = str(date.today())
        expiration_date = min(
          [
            item["data_de_validade"]
            for item in data if item["data_de_validade"] > now]
        )

        # https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
        company_more_products = mode(
          company["nome_da_empresa"] for company in data)

        return (
          f"Data de fabricação mais antiga: {earliest_manufacturing_date}\n"
          f"Data de validade mais próxima: {expiration_date}\n"
          f"Empresa com maior quantidade de produtos estocados: "
          f"{company_more_products}\n"
        )
