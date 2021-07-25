import datetime as datetime


class SimpleReport:

    def generate(object_to_report):
        data_fabricacao = SimpleReport.generate_oldest_manufacturing_date(
          object_to_report)
        data_validade = SimpleReport.generate_nearest_expiration_date(
          object_to_report)
        empresa_frequente = SimpleReport.return_the_most_frequent_enterprise(
          object_to_report)
        return (
          f"Data de fabricação mais antiga: {data_fabricacao}\n"
          f"Data de validade mais próxima: {data_validade}\n"
          f"Empresa com maior quantidade de produtos estocados: "
          f"{empresa_frequente}\n")

    def generate_oldest_manufacturing_date(object_to_report):
        return min(SimpleReport.generate_date_time_list(
          object_to_report, "data_de_fabricacao")).date()

    def generate_nearest_expiration_date(object_to_report):
        expiration_date_list = SimpleReport.verifyExpiration(
                               SimpleReport.generate_date_time_list(
                                object_to_report, "data_de_validade"))
        return min(expiration_date_list).date()

    def generate_date_time_list(object_to_report, fieldValue):
        date_time_list = list(map(
          lambda x: x[fieldValue], object_to_report))
        return [datetime.
                datetime.strptime(i, '%Y-%m-%d') for i in date_time_list]

    def verifyExpiration(list):
        return filter(lambda x: x > datetime.datetime.now(), list)

    def return_all_enterprises_names(object_to_report):
        return set([i["nome_da_empresa"] for i in object_to_report])

    def return_the_most_frequent_enterprise(object_to_report):
        enterprise_list = [i["nome_da_empresa"] for i in object_to_report]
        return max(set(enterprise_list),
                   key=enterprise_list.count)
