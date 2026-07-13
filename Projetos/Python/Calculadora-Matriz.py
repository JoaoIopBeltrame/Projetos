# add uma opcao que ja da pra selecionar de x ate y ou l a c pra um numero pra evitar as demoras
# mP = [
#     [1, 5, 2, 3, 8],
#     [6, 7, 1, 4, 3],
#     [2, 5, 9, 3, 1],
#     [4, 1, 3, 2, 6],
#     [3, 8, 2, 7, 5]
# ]
# add um parametro la que vaiimprimir quando terina de preeencher uma matriz e um contaor que vai aumentado conforme o linha e coluna de input

# tem muito erro aqui FAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH        

import os, sys, time

def animReiniciando(palavra, vezes=5):
    for i in range(vezes):
        os.system("cls" if os.name == "nt" else "clear")
        sys.stdout.write(palavra)
        for k in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.17)
        print()

def tabela():
    print("""
╔═══╦══════════════════╗
║ 1 ║ Somar matrizes    ║
║ 2 ║ Subtrair matrizes ║
║ 3 ║ Multiplicar       ║
║ 4 ║ Determinante      ║
║ 0 ║ Sair              ║
╚═══╩══════════════════╝
""")

def matrizA():
    while True:
        try:
            l = int(input("Dgite quantas linhas a matriz deve ter\n> "))
            j = int(input("Dgite quantas colunas a matriz deve ter\n> "))

            mA = [[0 for co in range(j)] for lin in range(l)]

    
            for lin in range(l):
                for col in range(j):
                    mA[lin][col] = int(input(f"Digite o numero da matriz (COORDENADA: linha -> {lin + 1} | coluna -> {col + 1})\n> "))
        
            return mA
        except ValueError:
            print("Digite um numero inteiro")

def matrizB():
    while True:
        try:
            l = int(input("Dgite quantas linhas a matriz deve ter\n> "))
            j = int(input("Dgite quantas colunas a matriz deve ter\n> "))

            mB = [[0 for co in range(j)] for lin in range(l)]
           
        
            for lin in range(l):
                for col in range(j):
                    mB[lin][col] = int(input(f"Digite o numero da matriz (COORDENADA: linha -> {lin + 1} | coluna -> {col + 1})\n> "))

            return mB
        except ValueError:
            print("Digite um numero inteiro")

def determinaneMatriz(): # todas as diagonais tem que se deitadas
    while True:
        try:
            l = int(input("Dgite quantas linhas a matriz deve ter\n> "))
            j = int(input("Dgite quantas colunas a matriz deve ter\n> "))

            if not (l == j):
                print("Para calcular os deerminantes a matriz deve ter um mesmo numero de linha e de coluna")
                continue

            mD = [[0 for co in range(j)] for lin in range(l)]
        
            for lin in range(l) :
                for col in range(j):
                    mD[lin][col] = int(input(f"Digite o numero da matriz (COORDENADA: linha -> {lin + 1} | coluna -> {col + 1})\n> "))

            return mD
        except ValueError:
            print("Digite um numero inteiro")

# a'{i,j} = a{i,j} - (a{i,1} × a{1,j}) / a{1,1}
def detReduzir(mC): # transformar em list comprehension
    while len(mC) > 3:
        # terminar a redução
        try:
            matrizRE = []
            for li in range(1, len(mC)):
                linhaRE = []
                for co in range(1, len(mC[0])):
                    valor = round(mC[li][co] - (mC[li][0] * mC[0][co]) / mC[0][0])
                    linhaRE.append(valor)
                matrizRE.append(linhaRE)
            mC = matrizRE

            # retornar cada matriz reduzida 
            #nao sei como fazer paia de mais
            return mC
        except ZeroDivisionError:
            print("A sua matriz dara erro EXPLICAÇÃO CHATA")   #pensar no que escrever ainda

            #colocar a expressao la do numpy


def somaSub(mA, mB, operador):
    return [
        [operador(mA[l][c], mB[l][c]) for c in range(len(mA[0]))
        ] for l in range(len(mA))
    ]

def matrizMult(mA, mB):
    if len(mA[0]) == len(mB):
        return [
            [
            sum(mA[linhaA][linhaB] * mB[linhaB][colunaB] for linhaB in range(len(mB)))
            for colunaB in range(len(mB[0]))
            ] for linhaA in range(len(mA))
        ]
    print("Tem que ter c de a igual a l de b") # fazer função la das anumações e um que mostra as regras



def main(): # colocar as opções la em match case e uma tabela com as operações add tambem que as matrizes de soma menos e mult e talves inversa fiquem uma do lado da outra com aqules desenos la e coisa parecida
    while True:

        tabela()
        try:
            opcao = int(input(">> "))
        except ValueError:
            print("Digite numero")
            continue
        
        match(opcao):
            case 1:
                mA = matrizA()
                mB = matrizB()
                resultado = somaSub(mA, mB, lambda a, b: a + b)
                print(*resultado, sep="\n")
            case 2:
                mA = matrizA()
                mB = matrizB()
                return somaSub(mA, mB, lambda mA, mB: mA - mB)
            case 3:
                mA = matrizA()
                mB = matrizB()
                return matrizMult(mA, mB)
            case 4:
                ... #determinante
            case 0:
                sys.exit()
            case _:
                print("Digite apenas uma das opções")
                animReiniciando()
                continue

if __name__ == '__main__':
    main()
