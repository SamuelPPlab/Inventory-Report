from inventory_report.reports.simple_report import SimpleReport

# Referencias: instrutores do plantão Ajudou em algumas partes do req


class CompleteReport(SimpleReport):
    def generate(lista_empresas):
        simple_report = SimpleReport.generate(lista_empresas)
        empresas = [empresa["nome_da_empresa"] for empresa in lista_empresas]
        empresas_qtd = ""
        for empresa in empresas:
            # http://excript.com/python/quantidade-de-itens-lista-python.html
            empresa_qtd = empresas.count(empresa)
            # http://excript.com/python/operadores-in-not-in-python.html
            if empresa not in empresas_qtd:
                empresas_qtd += f"- {empresa}: {empresa_qtd}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{empresas_qtd}"
        )


if __name__ == "__main__":
    lista = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]
    print(CompleteReport.generate(lista))
