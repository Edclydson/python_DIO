from datetime import date, time, datetime, timedelta


def today():
    hoje = date.today()
    print("Hoje é:", hoje.strftime("%A"))
    print("Estamos no dia:", hoje.strftime("%d"))
    print("Estamos no mês de:", hoje.strftime("%B"))
    print("Estamos no ano:", hoje.strftime("%Y"))
    hour()
    date_and_time()
    tomorrow()


def hour():
    hora = time(17, 00, 00)
    print("Seu compromisso está marcado para as:", hora.hour, "horas e",
          hora.minute, "minutos",
          hora.second, "segundos")


def date_and_time():
    data_hora = datetime.now()
    print("Data e hora atual:", data_hora.strftime("%d/%m/%Y %H:%M:%S"))
    print("Data atual:", data_hora.strftime("%d/%m/%Y"))
    print("Hora atual:", data_hora.strftime("%H:%M:%S"))


def tomorrow():
    amanha = date.today() + timedelta(days = 1)
    print("Amanhã será:", amanha.strftime("%A"))
    print("Será dia:", amanha.strftime("%d"))
    print("Será mês de:", amanha.strftime("%B"))
    print("Será ano de:", amanha.strftime("%Y"))


today()
