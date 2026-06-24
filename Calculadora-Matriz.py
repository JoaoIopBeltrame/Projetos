def definirMatrizA():
    while True:
        try:
            l = int(input("Diite uantas linhas a matriz deve ter\n> "))
            j = int(input("Diite uantas colunas a matriz deve ter\n> "))
            
            mA = [[60 for co in range(j)] for lin in range(l)]
        except ValueError:
            print("Digite um numero inteiro")
        return mA

def definirMatrizB():
    while True:
        try:
            l = int(input("Diite uantas linhas a matriz deve ter\n> "))
            j = int(input("Diite uantas colunas a matriz deve ter\n> "))
            
            mB = [[7 for co in range(j)] for lin in range(l)]
        except ValueError:
            print("Digite um numero inteiro")
        return mB

def matrizMenosMais(mA, mB, operador): #colocar dentro do main e o inpt de quantoQUANTO vai colocar o valor dentro disso
    return [
        [operador(mA[l][c], mB[l][c]) for c in range(len(mA[0]))
        ] for l in range(len(mA))  
    ]

def main():
    mA = definirMatrizA()
    print(f"=====A=====")
    print(*mA, sep="\n")
    mB = definirMatrizB()
    print(f"=====B=====")
    print(*mB, sep="\n")
    res = matrizMenosMais(mA, mB, lambda mA, mB: mA + mB)
    print(f"=====C=====")
    print(*res, sep="\n")



if __name__ == '__main__':
    main()
