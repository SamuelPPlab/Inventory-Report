from statistics import mode
from datetime import datetime


class SimpleReport:
    def menor_data(string_date):
        data = datetime.strptime(string_date, "%Y-%m-%d")
        atual = datetime.now()
        if data < atual:
            return False
        return True

    @classmethod
    def generate(data):
        data_fabricacao_mais_antiga = min(
            map(lambda x: x["data_de_fabricacao"], data)
        )

        validade_mais_proxima = min(
            item["data_de_validade"]
            for item in data
            if SimpleReport.menor_data(item["data_de_validade"])
        )

        empresa_com_maior_estoque = mode(
            list(map(lambda x: x["nome_da_empresa"], data))
        )

        dados_formatados = (
            f"Data de fabricação mais antiga: {data_fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{empresa_com_maior_estoque}"
            "\n"
        )
        return dados_formatados
