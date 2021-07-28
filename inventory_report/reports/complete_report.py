from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def output(data):
        new_lista = []
        str_output = ""

        for item in data:
            new_lista.append(item["nome_da_empresa"])

        for company in new_lista:
            if company not in str_output:
                str_output += f"- {company}: {new_lista.count(company)}\n"

        return str_output

    @classmethod
    def generate(cls, data):

        return (
            f"{SimpleReport.generate(data)}\n"
            f"Produtos estocados por empresa: \n"
            f"{cls.output(data)}"
        )
