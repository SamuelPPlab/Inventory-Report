from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(companies_list):
        simple_report = SimpleReport.generate(companies_list)
        companies = [company["nome_da_empresa"] for company in companies_list]
        companies_products_quantity = ""
        for company in companies:
            company_quantity = companies.count(company)
            if company not in companies_products_quantity:
                companies_products_quantity += f"- {company}: {company_quantity}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{companies_products_quantity}"
        )