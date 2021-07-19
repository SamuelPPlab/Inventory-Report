from statistics import mode


class SimpleReport:
    def generate(data):
        data_fabricacao_mais_antiga = min(
            list(map(lambda x: x["data_de_validade"], data))
        )

        validade_mais_proxima = min(
             list(map(lambda x: x["data_de_validade"], data))
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
