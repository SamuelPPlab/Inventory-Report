from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file_name):
        if file_name.endswith('.xml'):
            file_xml = Inventory.read_file_xml(file_name)
            return file_xml

        raise ValueError("Arquivo inválido")
