from datetime import datetime
from statistics import mode


class SimpleReport:
    def date_verification(strDate):
        date = datetime.strptime(strDate, '%Y-%m-%d')
        hour = datetime.now()
        if date < hour:
            return False
        return True

    def generate(data):
        initial_date = min(
            item["data_de_fabricacao"] for item in data
        )

        final_date = min(
            item["data_de_validade"] for item in data
            if SimpleReport.date_verification(item["data_de_validade"])
        )

        company = mode(
            item["nome_da_empresa"] for item in data
        )

        report = (
          f"Data de fabricação mais antiga: {initial_date}\n"
          f"Data de validade mais próxima: {final_date}\n"
          "Empresa com maior quantidade de produtos estocados: "
          f"{company}"
          "\n"
        )

        return report
