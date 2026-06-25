# add uma opcao que ja da pra selecionar de x ate y ou l a c pra um numero pra evitar as demoras

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

def main(): # colocar as opções la em match case e uma tabela com as operações
    mA = definirMatrizA()  
    print(f"=====A=====")
    print(*mA, sep="\n")
    mB = definirMatrizB()
    print(f"=====B=====")
    print(*mB, sep="\n")
    # res = matrizMenosMais(mA, mB, lambda mA, mB: mA + mB)
    # print(f"=====C=====")
    # print(*res, sep="\n")
    print(f"=====D=====")
    res3 = matrizMult(mA, mB)
    print(*res3, sep="\n")




if __name__ == '__main__':
    main()









#TUFFEST
