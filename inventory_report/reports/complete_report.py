from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)

        products_by_company = {}
        for product in products:
            company_name = product["nome_da_empresa"]
            if company_name not in products_by_company:
                products_by_company[company_name] = 1
            else:
                products_by_company[company_name] += 1

        companies_report = ""
        for company in products_by_company.items():
            companies_report += f"- {company[0]}: {company[1]}\n"

        report = (
            f"{simple_report}\n"
            + "Produtos estocados por empresa: \n"
            + companies_report
        )

        return report
