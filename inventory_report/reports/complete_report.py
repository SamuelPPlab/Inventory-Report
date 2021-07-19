from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(lista_empresas):
        simple = SimpleReport.generate(lista_empresas)
        empresas = [empresa["nome_da_empresa"] for empresa in lista_empresas]
        empresas_qtd = ""
        for empresa in empresas:
            empresa_qtd = empresas.count(empresa)
            if empresa not in empresas_qtd:
                empresas_qtd += f"- {empresa}: {empresa_qtd}\n"

        return (
            f"{simple}\n"
            "Produtos estocados por empresa: \n"
            f"{empresas_qtd}"
        )
