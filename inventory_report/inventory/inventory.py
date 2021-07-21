from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def __init__(self):
        pass

    def import_data(path, modo):

        # logica JSON
        if (path.endswith('.json')):
            with open(path) as file:
                lista = json.load(file)

        # logica XML

        # logica CSV
        else:
            data = []
            with open(path) as file:
                inventory_csv = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = inventory_csv
                lista = list(map(lambda produto: {
                    header[0]: produto[0],
                    header[1]: produto[1],
                    header[2]: produto[2],
                    header[3]: produto[3],
                    header[4]: produto[4],
                    header[5]: produto[5],
                    header[6]: produto[6]},
                    data))
        
        # trabalhando com a lista:
        if modo == "simples":
            retorno = SimpleReport.generate(lista)
            return retorno
        if modo == "completo":
            retorno = CompleteReport.generate(lista)
            return retorno


print(Inventory.import_data("./inventory_report/data/inventory.json", "completo"))
