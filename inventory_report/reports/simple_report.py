from datetime import datetime
from statistics import mode


class SimpleReport:

    def is_date_less_now(string_date):
        date = datetime.strptime(string_date, '%Y-%m-%d')
        now = datetime.now()
        if (date < now):
            return False
        return True

    def generate(data):
        earliest_manufacture_date = min(
            item["data_de_fabricacao"] for item in data
        )

        closest_expiration_date = min(
            item["data_de_validade"] for item in data
            if SimpleReport.is_date_less_now(item["data_de_validade"])
        )

        mode_company = mode(
            item["nome_da_empresa"] for item in data
        )

        report = (
          f"Data de fabricação mais antiga: {earliest_manufacture_date}\n"
          f"Data de validade mais próxima: {closest_expiration_date}\n"
          "Empresa com maior quantidade de produtos estocados: "
          f"{mode_company}"
          "\n"
        )
        return report
