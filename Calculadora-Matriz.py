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

def matrizMenosMais(mA, mB, operador):
    return [
        [operador(mA[l][c], mB[l][c]) for c in range(len(mA[0]))
        ] for l in range(len(mA))  
    ]



def matrizMult(mA, mB, operador): #num de coluna tem que ser igual a de linha linha de A multiplica cada coluna de B e soma  os coisas de coluna diferentes na mesma linha
        if (mA[len(l)] == mB[len(c)]) and ((mA[c] == mB[l]) or (mA[c] != mB[l])):
            return[
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
    print(f"=====D=====")
    res2 = matrizMult(mA, mB, lambda mA, mB: mA * mB)
    print(*res2, sep="\n")



if __name__ == '__main__':
    main()





# matriz = []
# for l in range(10):
#     linha = []
#     for c in range(10):
#         linha.append(0)
#     matriz.append(linha)

# int x,y,m1[x][y],m2[x][y];
# for (x=0;x<10;x++){
#     for (y=0;y<10;y++){
#         printf("digite o valor da matriz;\n" &m1[x][y]);
#         scanf("%d", m1[x][y]);
#     }
# for (x=0;x<10;x++){
#     for (y=0;y<10;y++){
#         printf("digite o valor da matriz;\n" &m2[x][y]);
#         scanf("%d", m2[x][y]);
#     }

















