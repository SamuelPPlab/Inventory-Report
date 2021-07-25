from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, companies_list):
        simple_report = super().generate(companies_list)
        company_name_list = [
            product["nome_da_empresa"] for product in companies_list
        ]

        not_repeat_names = []
        for name in company_name_list:
            if name not in not_repeat_names:
                not_repeat_names.append(name)

        company_count = [
            {"name": product, "count": company_name_list.count(product)}
            for product in not_repeat_names
        ]
        report = ""
        for company in company_count:
            report += (
                "- " + company["name"] + ": " + str(company["count"]) + "\n"
            )

        complete_report = (
            f"{simple_report}\nProdutos estocados por empresa: \n{report}"
        )

        return complete_report
