from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(companies_list):
        simple_report = SimpleReport.generate(companies_list)
        companies = [company["nome_da_empresa"] for company in companies_list]
        companies_products_qnt = ""
        for company in companies:
            company_qnt = companies.count(company)
            if company not in companies_products_qnt:
                companies_products_qnt += f"- {company}:{company_qnt}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{companies_products_qnt}"
        )
