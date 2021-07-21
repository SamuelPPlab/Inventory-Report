from .simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(lista):
        simple_result = SimpleReport.generate(lista)
        estoque_das_empresas = {}
        for item in lista:
            if item["nome_da_empresa"] in estoque_das_empresas:
                estoque_das_empresas[item["nome_da_empresa"]] += 1
            else:
                estoque_das_empresas[item["nome_da_empresa"]] = 1

        stock_list = list(estoque_das_empresas.items())
        stock_result = "\nProdutos estocados por empresa: \n"

        print(stock_result)

        for empresa in stock_list:
            new_company = f"- {empresa[0]}: {empresa[1]}\n"
            stock_result = (
                stock_result + new_company
            )

        complete_result = simple_result + stock_result

        return complete_result
