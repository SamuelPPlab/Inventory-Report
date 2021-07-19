from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        report_data = []
        [
            report_data.append(company["nome_da_empresa"])
            for company in data
            if company["nome_da_empresa"] not in report_data
        ]

        company_stock = {}
        for product in report_data:
            company_stock[product] = 0

        for item in report_data:
            company_stock[item["nome_da_empresa"]] += 1

        products = "Produtos estocados por empresa: \n"

        for company, quantity in company_stock.items():
            products += f"- {company}: {quantity}\n"

        return (
          f"{SimpleReport.generate(data)}\n"
          f"{products}"
        )
