import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, report):
        oldest_data_list = sorted(
            report, key=lambda item: item["data_de_fabricacao"], reverse=False
        )
        oldest_data = oldest_data_list[0]["data_de_fabricacao"]

        now_valid_list = sorted(
            report, key=lambda item: item["data_de_validade"], reverse=False
        )
        now_data = []
        date_time = str(datetime.datetime.now())
        for item in now_valid_list:
            if item["data_de_validade"] > date_time:
                now_data.append(item["data_de_validade"])

        company = []
        for comp in report:
            company.append(comp["nome_da_empresa"])

        company_count = Counter(company)
        max_show_company = list(company_count.keys())[1]

        result1 = "Data de fabricação mais antiga: {oldest_data}\n".format(
            oldest_data=oldest_data
        )
        result2 = "Data de validade mais próxima: {data}\n".format(
            data=now_data[0]
        )
        r = "Empresa com maior quantidade de produtos estocados: {m}\n".format(
            m=max_show_company
        )
        resultfinal = result1 + result2 + r
        return resultfinal
