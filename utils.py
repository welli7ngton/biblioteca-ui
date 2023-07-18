from datetime import datetime


def converte_data_p_str(_dia: datetime, _mes: datetime):
    dia = str(_dia)
    mes = str(_mes)

    return f"{int(dia):02d}/{int(mes):02d}"


if __name__ == "__main__":
    dia = datetime.now().day
    mes = datetime.now().month

    data = converte_data_p_str(dia, mes)
    print(data)

    print(datetime.now().microsecond)
