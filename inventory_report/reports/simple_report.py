from string import Template
from datetime import datetime
from statistics import mode


class SimpleReport:

    simple_report_template = Template(
        "Data de fabricação mais antiga: $oldest_manufacturing_date\n"
        + "Data de validade mais próxima: $nearest_expiration_date\n"
        + "Empresa com maior quantidade de produtos estocados: "
        + "$company_name\n"
    )

    @classmethod
    def generate(cls, product_list):
        oldest_manufacturing_date = min(
            product["data_de_fabricacao"] for product in product_list
        )

        nearest_expiration_date = min(
            product["data_de_validade"]
            for product in product_list
            if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        )

        company_name = mode(
            product["nome_da_empresa"] for product in product_list
        )

        return cls.simple_report_template.substitute(
            oldest_manufacturing_date=oldest_manufacturing_date,
            nearest_expiration_date=nearest_expiration_date,
            company_name=company_name,
        )
