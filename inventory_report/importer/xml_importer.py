from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    format = ".xml"

    def import_data(file_name, format):
        return super().import_data(file_name, format)
