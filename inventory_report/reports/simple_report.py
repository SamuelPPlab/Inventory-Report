from datetime import date
from statistics import mode


def get_manufactory_date(list):
    today = date.today()

    for index, product in enumerate(list):
        actual_date = date.fromisoformat(product["data_de_fabricacao"])
        if index < len(list) - 2:
            next_date = date.fromisoformat(
                list[index + 1]["data_de_fabricacao"]
            )
        if today - actual_date > today - next_date:
            oldest_date = actual_date
        else:
            oldest_date = next_date
    return oldest_date.isoformat()


def get_expiration_date(list):
    today = date.today()
    dates_list = [
        product["data_de_validade"]
        for product in list
        if date.fromisoformat(product["data_de_validade"]).year > today.year
    ]
    return min(dates_list)


# Referência: PR Luíse Rios
def get_company_name(list):
    company = mode(product["nome_da_empresa"] for product in list)
    return company


class SimpleReport:
    def generate(product_list):
        manufactoring_date = get_manufactory_date(product_list)
        expiration_date = get_expiration_date(product_list)
        company_name = get_company_name(product_list)
        report = (
            f"Data de fabricação mais antiga: {manufactoring_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{company_name}\n"
        )
        return report
