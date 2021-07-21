from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.Report import Report
from enum import Enum


class ReportType(Enum):
    COMPLETE = "completo"
    SIMPLE = "simples"


class InventoryRefactor:
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_name: str, _report_type: str):
        self.data.extend(self.importer.import_data(file_name))

    def import_report(self, report_type) -> Report:
        if report_type == ReportType.COMPLETE:
            return CompleteReport.generate(self.data)
        return SimpleReport.generate(self.data)
