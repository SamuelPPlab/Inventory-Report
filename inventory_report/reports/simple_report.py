from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data: list) -> str:
        date_now = datetime.now().date()

        sorted_by_manufacturing = min(s["data_de_fabricacao"] for s in data)
        sorted_by_expiration = min(
            s["data_de_validade"]
            for s in data
            if datetime.strptime(s["data_de_validade"], "%Y-%m-%d").date()
            > date_now
        )

        companies = [s["nome_da_empresa"] for s in data]
        company_name = max(set(companies), key=companies.count)

        return (
            f"Data de fabricação mais antiga: {sorted_by_manufacturing}\n"
            f"Data de validade mais próxima: {sorted_by_expiration}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{company_name}\n"
        )
