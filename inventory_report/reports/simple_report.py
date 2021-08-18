from datetime import datetime


class SimpleReport:
    def oldestDate(data):
        return min([
            datetime.strptime(item["data_de_fabricacao"], "%Y-%m-%d")
            for item in data
        ]).date()

    def nearliestExpireDate(data):
        today = datetime.today()
        nearliest = datetime.max
        for item in data:
            current = datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            if (current > today and current < nearliest):
                nearliest = current

        return nearliest.date()

    def maxItemCount(data):
        return max([item["nome_da_empresa"] for item in data])

    def generate(data):
        return (
            "Data de fabricação mais antiga: %s\n"
            "Data de validade mais próxima: %s\n"
            "Empresa com maior quantidade de produtos estocados: %s\n"
            % (
                SimpleReport.oldestDate(data),
                SimpleReport.nearliestExpireDate(data),
                SimpleReport.maxItemCount(data)
            )
        )
