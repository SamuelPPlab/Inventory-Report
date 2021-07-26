import datetime
from collections import Counter


class SimpleReport:
    EARLIEST = "Data de fabricação mais antiga"
    LATEST = "Data de validade mais próxima"
    COMPANY = "Empresa com maior quantidade de produtos estocados"

    @classmethod
    def generate(cls, products):
        earlist_date = sorted(
            products,
            key=lambda product: product["data_de_fabricacao"],
        )[0]["data_de_fabricacao"]

        latest_date = sorted(
            products,
            key=lambda product: product["data_de_validade"],
        )

        for product in latest_date:
            current_date = datetime.datetime.date(datetime.datetime.now())
            date = datetime.datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()

            if date > current_date:
                latest_date = product["data_de_validade"]
                break

        company = Counter(
            [product["nome_da_empresa"] for product in products]
        ).most_common(1)
        company = company[0][0]

        report = (
            f"{cls.EARLIEST}: {earlist_date}\n"
            + f"{cls.LATEST}: {latest_date}\n"
            + f"{cls.COMPANY}: {company}\n"
        )

        return report
