from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    format = ".csv"

    def import_data(file_name, format):
        return super().import_data(file_name, format)
