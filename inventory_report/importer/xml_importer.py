from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        ending = file_name[-3:]
        if ending == 'xml':
            xml = Inventory.import_xml(file_name)
            return xml
        else:
            raise ValueError("Arquivo inválido")
