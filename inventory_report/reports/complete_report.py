from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(data):
        simpleReport = (
            SimpleReport.generate(data) +
            "\nProdutos estocados por empresa: \n"
        )
        report = ""

        companyList = [item["nome_da_empresa"] for item in data]
        for item in companyList:
            if item not in report:
                report += f"- {item}: {companyList.count(item)}\n"

        return (
            simpleReport + report
        )
