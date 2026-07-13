#add um parametro la que vaiimprimir quando terina de preeencher uma matriz e um contaor que vai aumentado conforme o linha e coluna de input

# tem muito erro aqui FAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH        

# deixar mais bonitinho as coisa dentr da matriz pq se nao fica paia de mais

#colocar a expressao la do numpy

def limparMatriz(matriz):
    print('\n     ' + '  '.join(f'{c:^3}' for c in range(len(matriz[0]))))
    print('  ╔' + '═' * (len(matriz[0]) * 4))
    for nume, linha in enumerate(matriz):
        celulas = ''.join(f'{v:^3}' for v in linha)
        print(f'{nume} ║  ' + celulas)


def malhorarTeste(matriz):
    preenhe_rapido = ("Quer um preencher rapido\n> ").strip().capitalize()
    if preenhe_rapido in ["Sim", "S"]: #teste se funciona ou nao
        print(""" 
        1 = SEMELHANTE
        2- crescente #linha po rlinha, perguntar o ritimo tambem
        3 decresentente""")

        estilo = int(input(">> "))
        numero = int(input("Numero da matriz\n> "))
        match estilo:
            case 1:
                for linha in range(len(matriz)):
                    for item in range(len(matriz[0])):
                        matriz[linha][item] = numero
                editarPass = input("Quer continuar ou editar pelo indice?\n> ").strip().capitalize()
                if editarPass in ["Continua", "Cont", "Continuar", "C"]:
                    return matriz
                elif editarPass in ["Editar", "Edit", "Edita","E"]:
                    ...
                else:
                    print("Opção valida ae paizao")
                    #colocar dentro de  um loop tudo pra voltar pro contiue e etc

    return False # pensar no que fazer nisso s
    



import os, sys, time

# interface
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
#add mais coisa

# criar as matrizes para soma, subtração, multiplicação e possivel divisao(não existe eu acho)
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
        
        except ValueError:
            print("Digite um numero inteiro")
            continue    

        mD = [[0 for co in range(j)] for lin in range(l)]
        
        for lin in range(l) :
            for col in range(j):
                while True:
                    try:
                        mD[lin][col] = int(input(f"Digite o numero da matriz (COORDENADA: linha -> {lin + 1} | coluna -> {col + 1})\n> "))
                        break
                    except ValueError:  
                        print("Digite numeros")
        return mD
            

# Operaçãoes que vao ocorrer entre as matrizes
def detReduzir(mC): # transformar em list comprehension
    i = 0
    # a'{i,j} = a{i,j} - (a{i,1} × a{1,j}) / a{1,1} // regra de Chió usada para redução de matrizes para achar determinantes
    while len(mC) > 1:
        try:
            mC = [[round(mC[li][co] - (mC[li][0] * mC[0][co]) / mC[0][0]) for co in range(1, len(mC[0]))] for li in range(1, len(mC))]
            i += 1
            print(f"{i}º passo")
            print(*mC, sep="\n")
        except ZeroDivisionError:
            print("A sua matriz dara erro o primeiro indice nao pode ser 0")
            return None
    return mC[0][0]

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

def main():    
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
                print(f"Matriz A")
                limparMatriz(mA)
                mB = matrizB()
                print(f"Matriz B")
                limparMatriz(mB)
                resultado = somaSub(mA, mB, lambda a, b: a + b)
                limparMatriz(resultado)
            case 2:
                mA = matrizA()
                print(f"Matriz A")
                limparMatriz(mA)
                mB = matrizB()
                print(f"Matriz B")
                limparMatriz(mB)
                resultado = somaSub(mA, mB, lambda a, b: a - b)
                limparMatriz(resultado)
            case 3:
                mA = matrizA()
                print(f"Matriz A")
                limparMatriz(mA)
                mB = matrizB()
                print(f"Matriz B")
                limparMatriz(mB)
                resultado = matrizMult(mA, mB)
                limparMatriz(resultado)
            case 4:
                mD = determinaneMatriz()
                print("Matriz original:")
                limparMatriz(mD)
                det = detReduzir(mD)
                print(f"O determinante é")
                limparMatriz(det)

            case 0:
                sys.exit()
            case _:
                print("Digite apenas uma das opções")
                animReiniciando()
                continue

if __name__ == '__main__':
    main()
    
