from string import Template
from datetime import datetime
import operator


class SimpleReport:
    @staticmethod
    def generate(all_products):

        report_template = Template(
            "Data de fabricação mais antiga: $older_manufacturing_date\n"
            + "Data de validade mais próxima: $newer_expiration_date\n"
            + "Empresa com maior quantidade de produtos estocados: "
            + "$company_name\n"
        )

        older_manufacturing_date = datetime.now().strftime("%Y-%m-%d")
        newer_expiration_date = "2050-12-31"

        for product in all_products:
            if datetime.strptime(
                older_manufacturing_date, "%Y-%m-%d"
            ) > datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d"):
                older_manufacturing_date = product["data_de_fabricacao"]

            if (
                (
                    datetime.strptime(newer_expiration_date, "%Y-%m-%d")
                    - datetime.now()
                )
                > (
                    datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                    - datetime.now()
                )
            ) and (
                datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                > datetime.now()
            ):
                newer_expiration_date = product["data_de_validade"]

        company_name = max(
            SimpleReport.calculate_quantity_by_company(all_products).items(),
            key=operator.itemgetter(1),
        )[0]

        return report_template.substitute(
            older_manufacturing_date=older_manufacturing_date,
            newer_expiration_date=newer_expiration_date,
            company_name=company_name,
        )

    @staticmethod
    def calculate_quantity_by_company(all_products):
        quantity_by_company = {}
        for product in all_products:
            if product["nome_da_empresa"] in quantity_by_company:
                quantity_by_company[product["nome_da_empresa"]] += 1
            else:
                quantity_by_company[product["nome_da_empresa"]] = 1
        return quantity_by_company
