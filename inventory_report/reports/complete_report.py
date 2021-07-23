from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, report):
        result = super().generate(report)

        company = []
        for comp in report:
            company.append(comp["nome_da_empresa"])

        company_count = Counter(company)

        r = ""
        for item in company_count:
            r += "- {iten}: {companies}\n".format(
                iten=item, companies=str(company_count[item])
            )

        result_final = result + "\nProdutos estocados por empresa: \n" + r
        print(result_final)
        return result_final
