from datetime import datetime


class SimpleReport:
    def generate(lista_empresas):
        datas_de_validade = []
        empresas = [empresa["nome_da_empresa"] for empresa in lista_empresas]
        print(empresas)
        qtd = max(set(empresas), key=empresas.count)
        data_de_fabricacao = min(
            list(
                map(
                    lambda x: str(
                        datetime.strptime(
                            x["data_de_fabricacao"], "%Y-%m-%d"
                        ).date()
                    ),
                    lista_empresas,
                )
            )
        )

        for data in lista_empresas:
            if (
                datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date()
                > datetime.now().date()
            ):
                datas_de_validade.append(data["data_de_validade"])

        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {min(datas_de_validade)}\n"
            f"Empresa com maior quantidade de produtos estocados: {qtd}\n"
        )
