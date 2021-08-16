from datetime import datetime
from statistics import mode


class SimpleReport:

    def verifyDate(stringDate):
        date = datetime.strptime(stringDate, '%Y-%m-%d')
        now = datetime.now()
        if date < now:
            return False
        return True

    def generate(data):
        earliestDate = min(
            item["data_de_fabricacao"] for item in data
        )

        closestDate = min(
            item["data_de_validade"] for item in data
            if SimpleReport.verifyDate(item["data_de_validade"])
        )

        modeCompany = mode(
            item["nome_da_empresa"] for item in data
        )

        report = (
          f"Data de fabricação mais antiga: {earliestDate}\n"
          f"Data de validade mais próxima: {closestDate}\n"
          "Empresa com maior quantidade de produtos estocados: "
          f"{modeCompany}"
          "\n"
        )
        return report
