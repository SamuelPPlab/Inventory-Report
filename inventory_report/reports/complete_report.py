from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data: list) -> str:
        companies = [s["nome_da_empresa"] for s in data]

        c = {}
        for i, n in enumerate(companies):
            c[n] = (c.get(n) or 0) + 1

        return (
            f"{super().generate(data)}"
            "\nProdutos estocados por empresa: \n"
            "{}".format("".join(f"- {k}: {v}\n" for k, v in c.items()))
        )