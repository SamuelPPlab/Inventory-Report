from datetime import datetime


class SimpleReport:

    def get_firm(list):
        return max(item["nome_da_empresa"] for item in list)

    def older(list):
        return min(item["data_de_fabricacao"] for item in list)

    def newest(list):
        format_date = "%Y-%m-%d"
        dates = []

        for item in list:
            date = datetime.strptime(item["data_de_validade"], format_date)
            dates.append(date)

        now = datetime.now()
        return min(dt for dt in dates if dt > now).strftime(format_date)

    def generate(list):
        return (f"Data de fabricação mais antiga: {SimpleReport.older(list)}\n"
                f"Data de validade mais próxima: {SimpleReport.newest(list)}\n"
                "Empresa com maior quantidade de produtos estocados:"
                f" {SimpleReport.get_firm(list)}\n")
