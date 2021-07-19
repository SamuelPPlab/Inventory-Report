# from datetime import timedelta
import json


class SimpleReport:
    def __init__(self, content):
        self.content = content

    def generate():


with open("./inventory_report/data/inventory.json") as file:
    result = file.read()
    content = json.loads(result)

    print(content[0])
# from datetime import date
# >>> date.fromisoformat('2019-12-04')
# datetime.date(2019, 12, 4)
