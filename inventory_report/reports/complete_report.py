from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def number_of_occurrences(name, stock):
        number_of_occurrences = 1
        for company in stock:
            if company["nome_da_empresa"] == name:
                number_of_occurrences += 1
        return number_of_occurrences

    @classmethod
    def generate(cls, stock):
        simple_report = super().generate(stock)
        companys = "\nProdutos estocados por empresa: \n"
        for index, company in enumerate(stock):
            number_of_occurrences = CompleteReport.number_of_occurrences(
                company["nome_da_empresa"], stock[index + 1:]
            )
            companys += (
                f'- {company["nome_da_empresa"]}: '
                f"{number_of_occurrences}\n"
            )
            for other_company in stock[index + 1:]:
                if (
                    company["nome_da_empresa"]
                    == other_company["nome_da_empresa"]
                ):
                    stock.remove(other_company)
        return simple_report + companys
