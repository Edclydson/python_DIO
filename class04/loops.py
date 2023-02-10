num = int(input("Digite um numero\n"))
pares = 0
for i in range(num):
    if i % 2 == 0 and i != 0:
        print(i, "é par")
        pares += 1

print("Foram encontrados ", pares, " numeros pares")


quantidade_cafe = int(input("Digite a quantidade de cafe que deseja "
                            "colocar\n"))
capacidade_xicara = 0
while capacidade_xicara < quantidade_cafe:
    print("Colocando café na xícara...")
    capacidade_xicara += 5

print("Xícara cheia com", capacidade_xicara, "ml de café(s)! ;D")
