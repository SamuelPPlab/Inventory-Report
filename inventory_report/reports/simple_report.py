from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(dataReport: list) -> str:
        min_data_fabrication = min(
            [
                datetime.strptime(
                    report["data_de_fabricacao"], "%Y-%M-%d"
                ).strftime("%Y-%M-%d")
                for report in dataReport
            ]
        )
        now = datetime.now()
        max_data_validity = min(
            [
                datetime.strptime(
                    report["data_de_validade"], "%Y-%M-%d"
                ).strftime("%Y-%M-%d")
                for report in dataReport
                if datetime.strptime(report["data_de_validade"], "%Y-%M-%d")
                > now
            ]
        )
        companies = [report["nome_da_empresa"] for report in dataReport]
        company = max(set(companies), key=companies.count)
        return (
            f"Data de fabricação mais antiga: {min_data_fabrication}\n"
            f"Data de validade mais próxima: {max_data_validity}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{company}\n"
        )
