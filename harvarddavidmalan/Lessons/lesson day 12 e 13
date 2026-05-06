'''
loop for
loop -> estrutura de repeticao
for  -> uma dessas estruturas

Em C ou Java:
for(int i = 0; i < 10; i++) {}

Em Python:
for item in iteravel:
    ...

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis.

Exemplos de iteráveis:
- string
    nome = 'receba'
- lista 
    lista = [1, 3, 5, 7]
- range
    numeros = range(1, 10)
'''

# Iterando
nome = 'receba'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo 1 - iterando sobre uma string
for letra in nome:
    print(letra)

# Exemplo 2 - iterando sobre uma lista
for numero in lista:
    print(numero)

# Exemplo 3 - iterando com range
# OBS: o valor final não é incluso (vai até 9 nesse caso)
for numero in range(1, 10):
    print(numero)

# Enumerate -> retorna índice e valor
# (0 = r), (1 = e), (2 = c) ...
for i, v in enumerate(nome):
    print(nome[i])

# Enumerate com underline -> descartando o índice
for _, letra in enumerate(nome):
    print(letra)

# Enumerate exibindo tuplas (indice, valor)
for valor in enumerate(nome):
    print(valor)

'''
Exemplo de saída:
(0, 'r')
(1, 'e')
(2, 'c')
(3, 'e')
(4, 'b')
(5, 'a')
'''

# Utilização real de for
qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f"Informe o ({n}/{qtd}) valor: "))
    soma = soma + num

print(f"A soma é {soma}")

# Pular linha com for (end='')
nome = 'receba'
for letra in nome:
    print(letra, end='')

print()  # apenas para quebrar a linha no final

# Emoji usando repetição
num = 3
for numero in range(1, 11):
    print('\U0001F60D' * num)
