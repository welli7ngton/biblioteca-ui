from datetime import datetime
import calendar


def converte_data_p_str(_dia: datetime, _mes: datetime):
    dia = str(_dia)
    mes = str(_mes)

    return f"{int(dia):02d}/{int(mes):02d}"


if __name__ == "__main__":
    a = calendar.month(2023, 7)
    print(a)
