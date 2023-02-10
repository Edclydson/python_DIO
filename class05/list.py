lista_notas = [7.5, 8.0, 9.5, 10.0, 6.0, 5.0, 4.0]

if 7.0 in lista_notas:
    print("A nota 7.0 está na lista")
else:
    print("A nota 7.0 não está na lista")

print("lista ordenada: ",sorted(lista_notas))
print("menor nota é: ",sorted(lista_notas)[0])
print("maior nota é: ",sorted(lista_notas)[len(lista_notas)-1])
print("média das notas é: ",format(sum(lista_notas)/len(lista_notas),'.2f'))
print("quantidade de notas é: ",len(lista_notas),"\n")

for nota in lista_notas:
    if nota >= 7.0:
        print("Aprovado com nota: ",nota)
    else:
        print("Reprovado com nota: ",nota)

for nota in lista_notas:
    if nota < 7.0:
        lista_notas.remove(nota)

print("lista de notas sem reprovação: ",lista_notas)
print("lista ordenada: ",sorted(lista_notas))
print("menor nota é: ",sorted(lista_notas)[0])
print("maior nota é: ",sorted(lista_notas)[len(lista_notas)-1])
print("média das notas é: ",sum(lista_notas)/len(lista_notas))
print("quantidade de notas é: ",len(lista_notas),"\n")

