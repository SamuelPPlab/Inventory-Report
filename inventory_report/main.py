import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def generate_report(lista, tipo_de_relatorio):
    if tipo_de_relatorio == "simples":
        resultado = SimpleReport.generate(lista)
    else:
        resultado = CompleteReport.generate(lista)
    return resultado


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    _comando, path, tipo_de_relatorio = sys.argv
    lista = []

    if path.split(".")[1] == "csv":
        transforma_arquivo_em_lista = InventoryRefactor(CsvImporter)
        lista = transforma_arquivo_em_lista.import_data(
            path, tipo_de_relatorio
        )

    if path.split(".")[1] == "json":
        transforma_arquivo_em_lista = InventoryRefactor(JsonImporter)
        lista = transforma_arquivo_em_lista.import_data(
            path, tipo_de_relatorio
        )

    if path.split(".")[1] == "xml":
        transforma_arquivo_em_lista = InventoryRefactor(XmlImporter)
        lista = transforma_arquivo_em_lista.import_data(
            path, tipo_de_relatorio
        )

    resultado = generate_report(lista, tipo_de_relatorio)
    print(resultado[:-1])
