from .simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(lista):
        resultado_simples = SimpleReport.generate(lista)
        estoque_das_empresas = {}
        for item in lista:
            if item["nome_da_empresa"] in estoque_das_empresas:
                estoque_das_empresas[item["nome_da_empresa"]] += 1
            else:
                estoque_das_empresas[item["nome_da_empresa"]] = 1

        lista_estoque_das_empresas = list(estoque_das_empresas.items())
        resultado_estoque_das_empresas = "\nProdutos estocados por empresa: \n"

        for empresa in lista_estoque_das_empresas:
            nova_empresa = f"- {empresa[0]}: {empresa[1]}\n"
            resultado_estoque_das_empresas = (
                resultado_estoque_das_empresas + nova_empresa
            )

        resultado_completo = resultado_simples + resultado_estoque_das_empresas

        return resultado_completo
