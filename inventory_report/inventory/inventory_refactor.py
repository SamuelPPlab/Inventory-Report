from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, data_importer):
        self.data_importer = data_importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path, report_type):
        data_dict = self.data_importer.import_data(file_path)
        self.data.extend(data_dict)
        if report_type == "simples":
            return SimpleReport.generate(data_dict)
        elif report_type == "completo":
            return CompleteReport.generate(data_dict)
