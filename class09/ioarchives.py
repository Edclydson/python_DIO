arquivo = open('leiame.txt', 'w')
arquivo.write('Este é o arquivo de texto criado pelo Python.')
arquivo.close()

arquivo = open('leiame.txt', 'a')
arquivo.write('\n Autor: Edclydson Sousa')
arquivo.close()

arquivo = open('leiame.txt', 'r')
texto = arquivo.read()
print(texto)
arquivo.close()
