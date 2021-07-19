from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        new_data = []
        [
            new_data.append(d["nome_da_empresa"])
            for d in data
            if d["nome_da_empresa"] not in new_data
        ]

        products_stocked_by_company = {}
        for company in new_data:
            products_stocked_by_company[company] = 0

        for d in data:
            products_stocked_by_company[d["nome_da_empresa"]] += 1

        products = "Produtos estocados por empresa: \n"

        for company, quantity in products_stocked_by_company.items():
            products += f"- {company}: {quantity}\n"

        return (
            f"{SimpleReport.generate(data)}\n"
            f"{products}"
        )
