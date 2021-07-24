from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        report_tail = "\nProdutos estocados por empresa: \n"
        all_companies = [product["nome_da_empresa"] for product in products]
        companies = []
        for company in all_companies:
            if company not in companies:
                companies.append(company)
        for company in companies:
            report_tail += f"- {company}: {all_companies.count(company)}\n"
        return simple_report + report_tail
