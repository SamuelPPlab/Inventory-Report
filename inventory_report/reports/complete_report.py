from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @staticmethod
    def generate(object_to_report):
        simple_report = SimpleReport.generate(object_to_report)
        products = CompleteReport.return_enterprises_and_their_products_size(
          object_to_report)
        return (f"{simple_report}\n"
                "Produtos estocados por empresa: \n"
                f"{''.join(products)}")

    def return_enterprises_and_their_products_size(object_to_report):
        enterprise_list = list(SimpleReport.return_all_enterprises_names(
          object_to_report))
        enterprise_products = []
        for enterprise in enterprise_list:
            products_size = list(
              filter(lambda x: x["nome_da_empresa"] == enterprise,
                     object_to_report))
            enterprise_products.append(f"- {enterprise}: {len(products_size)}\n")
        return enterprise_products
