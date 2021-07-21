from datetime import datetime
import json


class SimpleReport:
    def generate(content):
        data_list = content

        oldest_date = min(
            data["data_de_fabricacao"] for data in data_list
        )
        print(oldest_date)

        current_time = datetime.today().strftime('%Y-%m-%d')
        nearest_expiration_date = min(
            data["data_de_validade"]
            for data in data_list
            if data["data_de_validade"] > current_time
        )
        print(nearest_expiration_date)


with open("./inventory_report/data/inventory.json") as file:
    result = file.read()
    content = json.loads(result)


SimpleReport.generate(content)
