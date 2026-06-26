# add uma opcao que ja da pra selecionar de x ate y ou l a c pra um numero pra evitar as demoras
# mP = [
#     [1, 5, 2, 3, 8],
#     [6, 7, 1, 4, 3],
#     [2, 5, 9, 3, 1],
#     [4, 1, 3, 2, 6],
#     [3, 8, 2, 7, 5]
# ]

def definirMatrizA():
    while True:
        try:
            l = int(input("Dgite quantas linhas a matriz deve ter\n> "))
            j = int(input("Dgite quantas colunas a matriz deve ter\n> "))
            
            mA = [[10 for co in range(j)] for lin in range(l)]
            return mA
        except ValueError:
            print("Digite um numero inteiro")

def definirMatrizB():
    while True:
        try:
            l = int(input("Dgite quantas linhas a matriz deve ter\n> "))
            j = int(input("Dgite quantas colunas a matriz deve ter\n> "))
            
            mB = [[10 for co in range(j)] for lin in range(l)]
            return mB
        except ValueError:
            print("Digite um numero inteiro")

def matrizMenosMais(mA, mB, operador):
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
            return mD
        except ValueError:
            print("Digite um numero inteiro")

# a'{i,j} = a{i,j} - (a{i,1} × a{1,j}) / a{1,1}    
def calcularChio(mC): # transformar em list comprehension
    while len(mC) > 3:
        try:
            matrizRE = []
            for li in range(1, len(mC)):
                linhaRE = []
                for co in range(1, len(mC[0])):
                    valor = round(mC[li][co] - (mC[li][0] * mC[0][co]) / mC[0][0])
                    linhaRE.append(valor)
                matrizRE.append(linhaRE)
            mC = matrizRE
            return mC
        except ZeroDivisionError:
            print("A sua matriz dara erro EXPLICAÇÃO CHATA")   #pensar no que escrever ainda
            
            #colocar a expressao la do numpy
        
def main(): # colocar as opções la em match case e uma tabela com as operações add tambem que as matrizes de soma menos e mult e talves inversa fiquem uma do lado da outra com aqules desenos la e coisa parecida
    
    mA = definirMatrizA()  
    print(f"=====A=====")
    print(*mA, sep="\n")
    mB = definirMatrizB()
    print(f"=====B=====")
    print(*mB, sep="\n")
    res = matrizMenosMais(mA, mB, lambda mA, mB: mA + mB)
    print(f"=====C=====")
    print(*res, sep="\n")
    print(f"=====D=====")
    res3 = matrizMult(mA, mB)
    print(*res3, sep="\n")
    det_MA = determinaneMatriz()
    chio = calcularChio(det_MA)
    print(*chio, sep="\n")




if __name__ == '__main__':
    main()









#TUFFEST
