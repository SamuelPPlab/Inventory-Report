""" import json """
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport

""" with open(
  "/home/cezar/trybe-projects/
  Computer Science/sd-07-inventory-report/inventory_report/data/inventory.json"
  ) as file:
    inventory = json.load(file) """


class CompleteReport(SimpleReport):
    def __init__(self):
        print("Complete Report created")

    @classmethod
    def products_stocked_by_company(cls, list):
        all_companies = []
        for company in list:
            all_companies.append(company["nome_da_empresa"])

        commom_companies = Counter(all_companies)

        companies_stock = "\nProdutos estocados por empresa: \n"

        for company_name, quantity in commom_companies.items():
            companies_stock += f"- {company_name}: {quantity}\n"
        return companies_stock

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        complete_report = cls.products_stocked_by_company(list)
        return simple_report + complete_report


""" print(CompleteReport.generate(inventory)) """
