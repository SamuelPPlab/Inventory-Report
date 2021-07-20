from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        super().__init__(self)

    def generate(inv_products):
        simple_report = SimpleReport.generate(inv_products)
        most_common = inventory_per_company(inv_products)
        first_line = "Produtos estocados por empresa: "
        bottom_report = (f"""{first_line}
{normalize_most_common(most_common)}""")
        return simple_report + "\n" + bottom_report


def inventory_per_company(stock):
    most_common_list = []
    lst = [item["nome_da_empresa"] for item in stock]
    for item in lst:
        tp = (item, lst.count(item))
        if most_common_list.count(tp) == 0:
            most_common_list.append(tp)
    return most_common_list


def normalize_most_common(commons):
    most_common = ""
    for index in range(0, len(commons)):
        most_common += f"- {commons[index][0]}: {commons[index][1]}\n"
    return most_common
