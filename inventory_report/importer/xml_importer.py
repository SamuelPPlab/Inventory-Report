from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):

    @classmethod
    def import_data(path):
        if (path.endswith('.xml')):
            tree = ET.parse(path)
            root = tree.getroot()
            lista = list(map(lambda produto: {
                produto[0].tag: produto[0].text,
                produto[1].tag: produto[1].text,
                produto[2].tag: produto[2].text,
                produto[3].tag: produto[3].text,
                produto[4].tag: produto[4].text,
                produto[5].tag: produto[5].text,
                produto[6].tag: produto[6].text},
                root))
            return lista
        else:
            raise Exception('Arquivo incorreto')
