class Inventory:
    def import_data(path, report_type):
        if path.split(".")[1] == "csv":
            with open(path, mode="r") as file:
                file_reader = csv.DictReader(file)
                list = []
                for string in file_reader:
                    list.append(string)
            return Generate_Report.generate(list, report_type)
#Evaluator