from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(lista):
        dic_de_empresas = {}
        data_de_fabricacao_mais_antiga = datetime.now().date()
        data_de_validade_mais_proxima = datetime.now().date()
        quantidade_de_dias_para_vencimento = 99999
        for item in lista:
            if item["nome_da_empresa"] in dic_de_empresas:
                dic_de_empresas[item["nome_da_empresa"]] += 1
            else:
                dic_de_empresas[item["nome_da_empresa"]] = 1

            data_de_fabricacao_do_produto = datetime.fromisoformat(
                item["data_de_fabricacao"]
            ).date()
            if data_de_fabricacao_do_produto < data_de_fabricacao_mais_antiga:
                data_de_fabricacao_mais_antiga = data_de_fabricacao_do_produto

            data_de_validade_do_produto = datetime.fromisoformat(
                item["data_de_validade"]
            ).date()
            if (
                data_de_validade_do_produto - datetime.now().date()
            ).days < quantidade_de_dias_para_vencimento and (
                data_de_validade_do_produto - datetime.now().date()
            ).days > 0:
                quantidade_de_dias_para_vencimento = (
                    data_de_validade_do_produto - datetime.now().date()
                ).days
                data_de_validade_mais_proxima = data_de_validade_do_produto

        dic_de_empresas = sorted(
            dic_de_empresas.items(), key=lambda x: x[1], reverse=True
        )
        result = (
            "Data de fabricação mais antiga: "
            + f"{data_de_fabricacao_mais_antiga}\n"
            "Data de validade mais próxima: "
            + f"{data_de_validade_mais_proxima}\n"
            "Empresa com maior quantidade de produtos estocados: "
            + f"{dic_de_empresas[0][0]}\n"
        )

        return result
