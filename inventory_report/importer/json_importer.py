from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    format = ".json"

    def import_data(file_name, format):
        return super().import_data(file_name, format)
