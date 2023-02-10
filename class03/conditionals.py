
# if, elif, else
a = int(input("Primeiro numero\n"))
b = int(input("Segundo numero\n"))

if a > b:
    print("O maior numero é", a)
elif a < b:
    print("O maior numero é", b)
else:
    print("Os numeros são iguais")

if a % 2 == 0:
    print("O primeiro numero é par")
else:
    print("O primeiro numero é impar")

if b % 2 == 0:
    print("O segundo numero é par")
else:
    print("O segundo numero é impar")
