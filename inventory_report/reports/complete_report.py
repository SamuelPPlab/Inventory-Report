from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @classmethod
    def generate(self, input):
        simple_report = SimpleReport.generate(input)
        company = [item["nome_da_empresa"] for item in input]
        companies = ""
        for item in company:
            counter = company.count(item)
            if item not in companies:
                companies += f"- {item}: {counter}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{companies}"
        )
