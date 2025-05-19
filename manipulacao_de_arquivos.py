# arquivo = open('test.txt', 'r') 

# arquivo = open('test.txt', 'r') #LEITURA

# print(arquivo.readable())   # Retorna (true or false) no terminal se o arquivo pode ser lido ou não.
# print(arquivo.read())       # Lê tudo que há no arquivo. 
# print(arquivo.readline())   # Lê linha por linha. 
# arquivo.readlines()         # Vai pegar todas as linhas e transformar em uma lista 
# lista = arquivo.readlines() # Todas linhas viram uma lista 
# print(lista)                # Imprimi o conteudo de calinha do arquivo em uma lista 
# print(lista[1])             # imprimi o o valor que está no indice(linha) [1] = java  


# arquivo = open('test.txt', 'a')  #ADICIONAR

# arquivo.write('SQL\n')        # adiciona no final do arquivo 'SQL'
# arquivo.write('Golang\n')     # adiciona no final do arquivo 'Golang' e quebra uma linha com \n
# arquivo.write('visualg\n')    # adiciona no final do arquivo 'visualg' e quebra uma linha com \n 

# arquivo = open('test.txt', 'w') # ESCRITA

# arquivo.write('sql\n')              # Se o arquivo já existir vai limpar o arquivo e começara a escrever do zero um novo arquivo
# arquivo. write('java golang\n')     # arquivo.write('sql') adiciona o texto 'sql' dentro do arquivo 
# arquivo. write('visualg \n')

# arquivo = open('test3.txt' , 'x') # criar outro arquivo test3.txt 

# arquivo.write('SQL\n')            # Adicionando as linguagens no novo arquivo test3.txt 
# arquivo.write('java script\n')
# arquivo.write('visualg\n')
# arquivo.write('JAVA\n')
# arquivo.write('C++\n')
# arquivo.write('golang\n')



# arquivo.close()

# remover arquivo

#import os 
#os.remove('test3.txt')

