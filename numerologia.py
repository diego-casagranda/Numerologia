# -*- coding: UTF-8 -*-

from re import compile, match

tabela = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 1, 'á': 3, 'â': 8, 'ã': 4, 'à': 2, 'ä': 2, 'e': 5, 'é': 7, 'ê': 3,
    'è': 1, 'ë': 1, 'i': 1, 'í': 3, 'ì': 2, 'î': 8, 'ï': 2, 'o': 7, 'ó': 9,
    'ô': 5, 'õ': 1, 'ò': 5, 'ö': 5, 'u': 6, 'ú': 8, 'ü': 3, 'ù': 3, 'y': 1,
    'b': 2, 'c': 3, 'ç': 6, 'd': 4, 'f': 8, 'g': 3, 'h': 5, 'j': 1,	'k': 2,
    'l': 3, 'm': 4, 'n': 5, 'ñ': 8, 'p': 8, 'q': 1, 'r': 2, 's': 3, 't': 4,
    'v': 6, 'x': 6, 'w': 6, 'z': 7, ' ': 0
}


def soma_numeros_nome(nome):
    c = 0
    for letra in nome:
        c += tabela[letra]
    return c


def com_mestre(numero_base):
    while True:
        if numero_base in [11, 22, 33]:
            return numero_base
        numero_base = sum([int(x) for x in str(numero_base)])
        if numero_base <= 9:
            return numero_base


def sem_mestre(numero_base):
    while True:
        numero_base = sum([int(x) for x in str(numero_base)])
        if numero_base <= 9:
            return numero_base


def soma_com_mestre(nome):
    return com_mestre(soma_numeros_nome(nome))


def soma_sem_mestre(nome):
    return sem_mestre(soma_numeros_nome(nome))


def soma_numeros_data(data):
    nums_exp = compile(r'(\d+)[/\- ](\d+)[/\- ](\d+)')
    return sum([int(x) for x in nums_exp.findall(data)[0]])


def numero_da_data(data):
    return com_mestre(soma_numeros_data(data))


def somar_digitos(n):
    s = 0
    while n:
        s += n % 10  # Soma `s` ao ultimo numeral de `n`
        n //= 10  # Remove o ultimo numero de `n`
    return s

def verificar_sequencias_repetidas(lista):
    if not lista:  # Garantir que a lista não está vazia
        return []

    sequencia_atual = lista[0]
    contagem = 1
    sequencias_encontradas = []

    for i in range(1, len(lista)):
        if lista[i] == sequencia_atual:
            contagem += 1
        else:
            if contagem >= 3:
                sequencias_encontradas.append((sequencia_atual, min(contagem, 3)))
            sequencia_atual = lista[i]
            contagem = 1

    if contagem >= 3:
        sequencias_encontradas.append((sequencia_atual, min(contagem, 3)))

    return sequencias_encontradas

# ANSI escape codes for coloring
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def piramide(nome):

    nome = nome.replace(' ', '')

    piramide_nome_num = []

    for caracter in nome.lower():
        if caracter in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                        'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'):

            piramide_nome_num.append(tabela[caracter])
        else:
            if caracter != " ":
                piramide_nome_num.append(tabela[caracter])

    print(' '.join(map(str, list(nome.upper()))))
    print(' '.join(map(str, piramide_nome_num)))

    cont_primeira_linha = piramide_nome_num
    cont_linha_anterior = []
    contador = 0

    size = len(piramide_nome_num)
    max_width = size * 2 - 1

    for linha in range(size-1, -1, -1):
        # Calcular o número de espaços à esquerda
        espacos = ' ' * (size - linha - 1)
        print(espacos, end="")  # Imprimir os espaços à esquerda

        linha_atual = []

        for coluna in range(linha + 1):
            if coluna != linha:
                soma = somar_digitos(
                    cont_primeira_linha[contador] + cont_primeira_linha[contador + 1])
                linha_atual.append(soma)
                cont_linha_anterior.append(soma)
            contador += 1

        # Verificar sequências repetidas
        sequencias = verificar_sequencias_repetidas(linha_atual) if linha_atual else []

        # Imprimir a linha com sequências destacadas
        i = 0
        while i < len(linha_atual):
            highlighted = False
            for seq in sequencias:
                if linha_atual[i] == seq[0] and linha_atual[i:i + seq[1]] == [seq[0]] * seq[1]:
                    for _ in range(seq[1]):
                        print(f"{GREEN}{linha_atual[i]}{RESET}", end=" ")
                        i += 1
                    highlighted = True
                    break
            if not highlighted:
                print(linha_atual[i], end=" ")
                i += 1

        cont_primeira_linha = cont_linha_anterior
        cont_linha_anterior = []
        print("\r")
        contador = 0

if __name__ == '__main__':

    Nome = 'Diego Casagranda'
    Data = '01/12/1985'

    vogais = []
    consoantes = []

    nome_num = []
    vogais_num = []
    consoantes_num = []

    for caracter in Nome.lower():
        if caracter in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'):
            consoantes.append(caracter)
            consoantes_num.append(tabela[caracter])
            vogais_num.append(0)
            nome_num.append(tabela[caracter])
        else:
            vogais.append(caracter)
            vogais_num.append(tabela[caracter])
            consoantes_num.append(0)
            nome_num.append(tabela[caracter])
    print()

    print(''.join(map(str, consoantes_num)).replace('0', ' '))
    print(''.join(map(str, list(Nome.upper()))))
    print(''.join(map(str, vogais_num)).replace('0', ' '))

    print()

    piramide(Nome)

    print()

    print("Motivação:", soma_sem_mestre(''.join(map(str, vogais))))
    print("Impressão:", soma_sem_mestre(''.join(map(str, consoantes))))
    print("Expressão:", soma_com_mestre(Nome.lower()))

    print()

    lista_nome = []

    for letra in Nome.lower():
        lista_nome.append(tabela[letra])

    carmica = []
    carmica.append(lista_nome.count(1))
    carmica.append(lista_nome.count(2))
    carmica.append(lista_nome.count(3))
    carmica.append(lista_nome.count(4))
    carmica.append(lista_nome.count(5))
    carmica.append(lista_nome.count(6))
    carmica.append(lista_nome.count(7))
    carmica.append(lista_nome.count(8))
    carmica.append(lista_nome.count(9))

    print('Numeros Repetidos/Em Falta:')
    print('1 2 3 4 5 6 7 8 9 ')
    print(' '.join(map(str, carmica)))

    print("")

    contador = 1
    divida_carmica = []
    tendencia_oculta = []

    for x in carmica:
        if x == 0:
            divida_carmica.append(contador)
        contador = contador + 1

    contador = 1

    for x in carmica:
        if x > 3:
            tendencia_oculta.append(contador)
        contador = contador + 1

    print("Lições Cármicas:", ','.join(map(str, divida_carmica)))
    print("Tendências Ocultas:", ','.join(map(str, tendencia_oculta)))

    print("")

    print("Dia Nascimento:", Data[0:2])
    print("Número Psíquico:", somar_digitos(int(Data[0:2])))
    print("Número de Destino:", numero_da_data(Data))
    print("")
