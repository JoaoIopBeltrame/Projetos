import os, sys, time

class Tela:
    @staticmethod  # usa quando é coisa direta que não precisa ler nem mudar dados daquele objeto específico   
    def animReiniciando(palavra, vezes=5):
        for i in range(vezes):
            os.system("cls" if os.name == "nt" else "clear")
            sys.stdout.write(palavra)
            for k in range(3):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.17)
            print()
    
    @staticmethod    
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

class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz
    
    @staticmethod
    def criarMatriz(nome="Matriz", quadrada=False, comparaMatriz=None):
        while True:
            try:
                l = int(input(f"Digite quantas linhas a {nome} deve ter\n> "))
                j = int(input(f"Digite quantas colunas a {nome} deve ter\n> "))

                if l <= 0 or j <= 0:
                    print("Linhas e colunas precisam ser maiores que 0")
                    continue

                if comparaMatriz is not None and (l != len(comparaMatriz) or j != len(comparaMatriz[0])):
                    print("As matrizes devem ter o mesmo numero de linhas e colunas para fazer operacoes de soma e subtracao")
                    continue

                if quadrada and l != j:
                    print("Para calcular o determinante a matriz deve ser quadrada (linhas = colunas)")
                    continue

            except ValueError:
                print("Digite um numero inteiro")
                continue

            m = [[0 for co in range(j)] for lin in range(l)]

            for lin in range(l):
                for col in range(j):
                    while True:
                        try:
                            m[lin][col] = int(input(
                                f"Digite o numero da matriz (COORDENADA: linha -> {lin + 1} | coluna -> {col + 1})\n> "))
                            break
                        except ValueError:
                            print("Digite numeros")
            return m

    def limparMatriz(self, titulo=None):
        if titulo:
            print(f"\n{titulo}")
            print('     ' + '  '.join(f'{c:^3}' for c in range(len(self.matriz[0]))))
            print('  ╔' + '═' * (len(self.matriz[0]) * 4))
            for nume, linha in enumerate(self.matriz):
                celulas = ''.join(f'{v:^3}' for v in linha)
                print(f'{nume} ║  ' + celulas)

    def determinante(self):
        mC = self.matriz
        passo = 0
        while len(mC) > 1:
            if mC[0][0] == 0:
                print("A sua matriz vai dar erro: o primeiro indice (pivo) nao pode ser 0")
                return None
            mC = [
                [round(mC[li][co] - (mC[li][0] * mC[0][co]) / mC[0][0]) for co in range(1, len(mC[0]))]
                for li in range(1, len(mC))
            ]
            passo += 1
            limparMatriz(mC, titulo=f"{passo}º passo")
        return mC[0][0]

    @staticmethod
    def somaSub(mA, mB, operador):
        return [
            [operador(mA[l][c], mB[l][c]) for c in range(len(mA[0]))]
            for l in range(len(mA))
        ]
    
    @staticmethod
    def matrizMult(mA, mB):
        if len(mA[0]) == len(mB):
            return [
                [
                    sum(mA[linhaA][linhaB] * mB[linhaB][colunaB] for linhaB in range(len(mB)))
                    for colunaB in range(len(mB[0]))
                ] for linhaA in range(len(mA))
            ]
        print("O numero de colunas de A precisa ser igual ao numero de linhas de B")
        return None

def main():
    while True:
        Tela.tabela()
        try:
            opcao = int(input(">> "))
        except ValueError:
            print("Digite um numero")
            continue

        match opcao:
            case 1 | 2:
                mA = matriz("Matriz A")
                limparMatriz(mA, "Matriz A")
                mB = matriz("Matriz B", comparaMatriz=mA)
                limparMatriz(mB, "Matriz B")
                op = (lambda a, b: a + b) if opcao == 1 else (lambda a, b: a - b)
                resultado = somaSub(mA, mB, op)
                limparMatriz(resultado, "Resultado")

            case 3:
                mA = matriz("Matriz A")
                limparMatriz(mA, "Matriz A")
                mB = matriz("Matriz B")
                limparMatriz(mB, "Matriz B")
                resultado = matrizMult(mA, mB)
                if resultado is not None:
                    limparMatriz(resultado, "Resultado")

            case 4:
                mD = matriz("Matriz", quadrada=True)
                limparMatriz(mD, "Matriz original")
                det = detReduzir(mD)
                if det is not None:
                    print(f"\nO determinante e: {det}")

            case 0:
                Tela.animReiniciando("Encerrando sistema")
                sys.exit()

            case _:
                print("Digite apenas uma das opcoes")
                Tela.animReiniciando("Reiniciando")
                continue

        input("\nPressione Enter para voltar ao menu...")

if __name__ == '__main__':
    main()
