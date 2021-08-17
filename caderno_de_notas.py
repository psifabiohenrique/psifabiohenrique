x = 0

'''while (x <= 10):
    print (x)
    x += 1
print('else')'''

for c in range(10): # for só pode ser utilizado com uma lista
    print(c)
 # break encerra o laço
 # continue encerra a execução atual e volta para o início do laço
lista = [1, 2, 3, 4] # listas utiliza os cochetes
lista2 = [[], [], []] # Para acessar ou criar sublistas: lista2 [0] [1]
tupla = (1, 2, 3, 4) # tuplas utiliza os parenteses
# tuplas são imutáveis
# python trata todas as strings como listas imutáveis
dicionario = {'index': 'valor',} # dicionários são marcados por chaves
dicionario.keys() # retorna a lista de chaves do dicionário
dicionario.values() # Retorna os valores contindos no dicionário
dicionario.popitem() # Retorna o primeiro elemento do dicionário e já remove ele
dicionario1 = dicionario2 = {}
dicionario1.update(dicionario2) # Passa os dados do dicionário 2 para o dicionário 1
chr(100) # retorna o caractere correspondente na tabela ASC II
ord('d') # retorna o código correspondente na tabela ASC II

# Métodos

# len(), retorna o número de elementos da lista
# lista.append(), acrescenta um item à lista
# del(lista[-1]), apaga um item da lista
# lista.insert(0, 'primeiro item'), inserir item em posição específica
# lista.clear(), apaga todos os items da lista
# lista.pop(), exclui um item específico da lsita
# lista.count('esse item'), conta quantos desse elementos tem na lista
# lista.index(), retorna qual a posição do item na lista
# enumerate('dicionário'), vincula uma lista de objetos a números inteiros
    #for index, valor in enumerate('dicionário')

# Ordenação:

# lista.reverse(), inverte todos os itens da lista
# lista.sort(), ordena a lista de forma acendente
# lista.sorte(reverse=True), ordena a lista de forma descendente

# Propriedades das Strings

# string.split('Onde quer quebrar'), divide a string em lista
# string.replace('', ''), troca o primeiro caractere pelo segundo

# Funções

def minha_funcao(): # Assim se define uma função 
    print('Olá mundo!')
minha_funcao() # Assim nós chamamos a função

def soma(x, y):
    total = x + y
    print(f'O total da soma de X + Y é {total} !')
    print('testando o \n para ver se funciona')
soma(10, 50)

# Utilizar um asterisco (*) antes do parâmetro, indica que a função vai receber uma lista
# Utilizar dois asteriscos (**) antes do parâmetro, indica que a função vai receber um discionário

def func ():
    var = 0
    def func2 ():
        nonlocal var # Dá permissão para utilizar uma variável que está no escopo de uma função a cima da atual

outravar = 0

def func3 ():
    global outravar # Dá permissão para utilizar uma variável que está no escopo global
    # Caso não utilizar esse comando você terá acesso à variável mas não alterará ela em nível global
    # Você também pode utilizar para criar uma variável em escopo local que vale para o escopo global

pass # Indica que o bloco atual está vazio e não deverá ser utilizado

