from inventory_report.reports.simple_report import SimpleReport
from typing import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report_list):
        print(cls.getCompanyWithMoreProducts(report_list))
