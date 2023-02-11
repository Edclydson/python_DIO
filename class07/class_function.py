def numero_par():
    return "O número é par"


def numero_impar():
    return "O número é ímpar"


class Numero:
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        print(numero_par())
    else:
        print(numero_impar())
