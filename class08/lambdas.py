contador_letras = lambda lista: [len(x) for x in lista]

print(contador_letras(['cachorro', 'gato', 'elefante']))

# criando calculadora com lambda
calculadora_lambda = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}
soma = calculadora_lambda['soma']
subtracao = calculadora_lambda['subtracao']
multiplicacao = calculadora_lambda['multiplicacao']
divisao = calculadora_lambda['divisao']

print(soma(5, 10))
print(subtracao(10, 5))
print(multiplicacao(5, 10))
print(divisao(10, 5))
