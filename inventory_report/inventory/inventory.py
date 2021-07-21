import csv
import json
from enum import Enum
from typing import OrderedDict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xmltodict


class FileExtension(Enum):
    JSON = "json"
    CSV = "csv"
    XML = "xml"


class ReportType(Enum):
    COMPLETE = "completo"
    SIMPLE = "simples"


class Inventory:
    @staticmethod
    def import_data(file_name: str, report_type: str):

        with open(file_name, "r") as file:
            data = list()
            file_type: str = file_name.split(".")[-1]

            if file_type == FileExtension.CSV.value:
                data: list[dict] = [line for line in csv.DictReader(file)]

            if file_type == FileExtension.JSON.value:
                data: list[dict] = json.load(file)

            if file_type == FileExtension.XML.value:
                data_ordered_dict: list[OrderedDict] = xmltodict.parse(
                    file.read()
                )
                data_json_string: json = json.dumps(data_ordered_dict)
                data: list[dict] = json.loads(data_json_string)["dataset"][
                    "record"
                ]

            return (
                CompleteReport.generate(data)
                if report_type == ReportType.COMPLETE.value
                else SimpleReport.generate(data)
            )
