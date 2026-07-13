# add uma opcao que ja da pra selecionar de x ate y ou l a c pra um numero pra evitar as demoras
# mP = [
#     [1, 5, 2, 3, 8],
#     [6, 7, 1, 4, 3],
#     [2, 5, 9, 3, 1],
#     [4, 1, 3, 2, 6],
#     [3, 8, 2, 7, 5]
# ]
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

            mA = [[10 for co in range(j)] for lin in range(l)]

            while True:
                for j in mA:
                    for i in j:
                        mA[i][j] = input("Digite o numero da matriz\n> ")
                        if type(mA[i][j]) == int:
                            print("Digite o proximo numero")
                        else:
                            print("Digite apenas numeros")
                            #parada la do reinciando
                            continue
                break

            return mA
        except ValueError:
            print("Digite um numero inteiro")

def matrizB():
    while True:
        try:
            l = int(input("Dgite quantas linhas a matriz deve ter\n> "))
            j = int(input("Dgite quantas colunas a matriz deve ter\n> "))

            mB = [[10 for co in range(j)] for lin in range(l)]
           
            while True:
                for lin in range(l):
                    for col in range(j):
                        mB[lin][col] = input("Digite o numero da matriz\n> ")
                        if type(mB[lin][col]) == int:
                            print("Digite o proximo numero")
                        else:
                            print("Digite apenas numeros")
                            #parada la do reinciando
                            continue 
                break

            return mB
        except ValueError:
            print("Digite um numero inteiro")

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

def determinaneMatriz(): # todas as diagonais tem que se deitadas
    while True:
        try:
            l = int(input("Dgite quantas linhas a matriz deve ter\n> "))
            j = int(input("Dgite quantas colunas a matriz deve ter\n> "))

            if not (l == j):
                print("Para calcular os deerminantes a matriz deve ter um mesmo numero de linha e de coluna")
                continue

            mD = [[9 for co in range(j)] for lin in range(l)]
            while True:
                for j in mD:
                    for i in j:
                        mD[i][j] = input("Digite o numero da matriz\n> ")
                        if type(mD[i][j]) == int:
                            print("Digite o proximo numero")
                        else:
                            print("Digite apenas numeros")
                            #parada la do reinciando
                            continue
                break
            return mD
        except ValueError:
            print("Digite um numero inteiro")

# a'{i,j} = a{i,j} - (a{i,1} × a{1,j}) / a{1,1}
def detReduzir(mC): # transformar em list comprehension
    while len(mC) > 3:
        # TODO 2 - CONDIÇÃO DE PARADA ERRADA
        # Pensa: Chió reduz a matriz até sobrar só 1 número (o determinante).
        # Uma matriz 1x1 tem len(mC) == 1. Então em que valor esse "> 3"
        # deveria estar pra ele continuar reduzindo até sobrar só 1 linha?
        # Troca o "3" por esse valor.
        try:
            matrizRE = []
            for li in range(1, len(mC)):
                linhaRE = []
                for co in range(1, len(mC[0])):
                    valor = round(mC[li][co] - (mC[li][0] * mC[0][co]) / mC[0][0])
                    linhaRE.append(valor)
                matrizRE.append(linhaRE)
            mC = matrizRE

            # TODO 3 - RETURN NO LUGAR ERRADO
            # Esse "return mC" abaixo tá DENTRO do while e do try. Isso
            # significa que a função sai (return) assim que roda UMA
            # rodada do loop, mesmo se a matriz ainda não chegou no
            # tamanho final. Testa: numa matriz 5x5, depois de 1 rodada
            # ela vira 4x4 -- e esse return já devolve ela, incompleta.
            # Pra resolver: tira esse "return mC" daqui de dentro, deixa
            # só "mC = matrizRE" rodando dentro do while, e coloca UM
            # return no final da função (fora do while), devolvendo
            # o número final. Depois que o while acabar, mC vai ser uma
            # lista com 1 linha e 1 elemento só -- então o determinante
            # de verdade é mC[0][0], não a matriz inteira.
            return mC
        except ZeroDivisionError:
            print("A sua matriz dara erro EXPLICAÇÃO CHATA")   #pensar no que escrever ainda

            #colocar a expressao la do numpy

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
                ...
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 0:
                ...

if __name__ == '__main__':
    main()
