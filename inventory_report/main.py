import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.index import importer


def main():
    try:
        args = sys.argv
        assert len(args) == 3
        path = args[1]
        type = args[2]
        """ Caminho:
        /home/cezar/trybe-projects/Computer Science/sd-07-inventory-report/
        inventory_report/data/inventory.json """
        file_type = path.split('.')[1]

        inventory = InventoryRefactor(importer[file_type])
        report = inventory.import_data(path, type)

        return print(f"{report}", end="")

    except AssertionError:
        print("Verifique os argumentos", file=sys.stderr)
