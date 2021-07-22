from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, simple_list):
        simples = super().generate(simple_list)
        company_list = []
        counter = {}

        for item in simple_list:
            company_list.append(item['nome_da_empresa'])

        for company in company_list:
            number = company_list.count(company)
            counter[company] = number

        lista = ['Produtos estocados por empresa: ']
        for company in counter:
            lista.append(f"- {company}: {counter[company]}")

        result = "\n".join(lista)
        return (
            f"{simples}\n{result}\n"
        )
