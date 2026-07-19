import os, sys, time
from fractions import Fraction as Fr

RESPONSES_YES = ["Sim", "S", "Si", "Y", "Ye", "Yes"]
RESPONSES_NO = ["Não", "Nao", "N", "Na", "No"]

class Tela:
    @staticmethod  # usa quando é coisa direta que não precisa ler nem mudar dados daquele objeto específico   
    def reloading(palavra, vezes=5):
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
    
    @staticmethod
    def regra():
        print(""" 

    digitar o numero 2 
              
    primeiro numero = 2
    segundo numero = 4
    terceiro numero = 8
    
    digitar um numero para ser o limite e reiniar o loop de exponencial
              se nao for digitado nada sera reinciado a cada linha
    """)

def criar_matriz():  # serve para matriz A e B
    while 1:
        try:
            l = int(input("Digite o NUMERO DE LINHAS que a matriz deve ter\n> "))
            c = int(input("Digite o NUMERO DE COLUNAS que a matriz deve ter\n> "))
        except ValueError:
            print("Digite apenas numeros")
            Tela.reloading("Voltando")
            continue
        except Exception as e:
            print("Um erro inesperado ocorreu. Pressione ENTER para voltar ao inicio")
            input(">>")
            Tela.reloading("Voltando")
            continue
        break

    m = [[Fr(0) for _ in range(c)] for _ in range(l)]
    print("Matriz atual:")
    for linha in m:
        print([str(item) for item in linha])

    while 1:
        try:
            confirmation_auto_fill = input("Deseja preencher inteira com apenas um numero?\n").strip().capitalize()
            if confirmation_auto_fill in RESPONSES_YES:
                number_fill = int(input("Digite o numero que deseja que a sua matriz seja\n> "))
                m = [[Fr(number_fill) for _ in range(c)] for _ in range(l)]
                break

            elif confirmation_auto_fill in RESPONSES_NO:
                while 1:
                    ask_expo_num = input("Deseja Que o auto preenchimento tenha um cresmento exponencial?").strip().capitalize()
                    print("Caso contrario sera tera que colocar manualmente cada numero")

                    if ask_expo_num in RESPONSES_YES:
                        limite = input("Deseja que seja digitado o numero inicial e o limite do crescimento exponencial?\n>> ")
                        while 1:
                            numero_expo_linha_diferente = input(
                                "Deseja que o numero de crescimento seja igual para toda a matriz "
                                "ou que va mudando de linha em linha? 1 para matriz inteira, 2 para linha em linha\n>> "
                            )
                            match numero_expo_linha_diferente:
                                case "1":
                                    Tela.regra()
                                    continua_ou_nao = input(
                                        "Voce deseja que os numeros subsequentes do limite sejam 0, ou que reinicie "
                                        "o loop e continue desde o inicio para os restantes 1 (preencher resto com 0) 2 (reiniciar)\n>> "
                                    )
                                    match continua_ou_nao:
                                        case "1":
                                            numero_inicial = Fr(int(input("Digite o numero inicial\n>> ")))
                                            numero_limite = Fr(int(input("Digite o numero limite\n>> ")))
                                            numero_crescimento = Fr(int(input("Digite o numero de exponencial\n>> ")))

                                            for lin in range(len(m)):
                                                for col in range(len(m[0])):
                                                    if numero_inicial <= numero_limite:
                                                        m[lin][col] = numero_inicial
                                                        numero_inicial *= numero_crescimento
                                                    else:
                                                        m[lin][col] = Fr(0)
                                            break

                                        case "2":
                                            numero_inicial = Fr(int(input("Digite o numero inicial\n>> ")))
                                            numero_limite = Fr(int(input("Digite o numero limite\n>> ")))
                                            numero_crescimento = Fr(int(input("Digite o numero de exponencial\n>> ")))
                                            numero_inicial_holder = numero_inicial

                                            for lin in range(len(m)):
                                                for col in range(len(m[0])):
                                                    if numero_inicial <= numero_limite:
                                                        m[lin][col] = numero_inicial
                                                        numero_inicial *= numero_crescimento
                                                    else:
                                                        numero_inicial = numero_inicial_holder
                                                        for lin2 in range(len(m)):
                                                            for col2 in range(len(m[0])):
                                                                if numero_inicial <= numero_limite:
                                                                    m[lin2][col2] = numero_inicial
                                                                    numero_inicial *= numero_crescimento
                                            break

                                        case _:
                                            print("Digite opção valida")
                                            Tela.reloading("Voltando")
                                            continue
                                    break  # fecha Loop B (case "1")

                                case "2":
                                    for lin in range(len(m)):
                                        numero_inicial = Fr(int(input("Digite o numero inicial\n>> ")))
                                        numero_limite = Fr(int(input("Digite o numero limite\n>> ")))
                                        numero_crescimento = Fr(int(input("Digite o numero de exponencial\n>> ")))

                                        for col in range(len(m[0])):
                                            if numero_inicial <= numero_limite:
                                                m[lin][col] = numero_inicial
                                                numero_inicial *= numero_crescimento
                                            else:
                                                m[lin][col] = Fr(0)
                                    break  # fecha Loop B (case "2")

                                case _:
                                    print("Digite uma opção valida")
                                    Tela.reloading("Voltando")
                                    continue
                        break  # fecha Loop A (matriz já preenchida)

                    elif ask_expo_num in RESPONSES_NO:
                        for lin in range(l):
                            for col in range(c):
                                while True:
                                    try:
                                        m[lin][col] = Fr(int(input(
                                            f"Digite o numero da matriz (COORDENADA: linha -> {lin + 1} | coluna -> {col + 1})\n> "
                                        )))
                                        break
                                    except ValueError:
                                        print("Digite numeros")
                        break

                    else:
                        print("Digite uma opção valida")
                        time.sleep(1)
                        Tela.reloading("Voltando")
                        continue

            else:
                print("Digite uma opção valida")
                Tela.reloading("Voltando")
                continue

        except ValueError:
            print("Digite apenas numeros")
            continue
        break

    return m

def sum_sub(matrizA, matrizB, operador):
    return[
       
        [operador(matrizA[lin][col], matrizB[lin][col]) for col in range(len(matrizA[0]))] 
        for lin in range(len(matrizA))
    ]

def multiplicacao(matrizA, matrizB):
    if len(matrizA[0]) == len(matrizB):
        
        return[
            [sum(matrizA[l][k] * matrizB[k][c] for k in range(len(matrizB))) for c in range(len(matrizB[0]))]
            for l in range(len(matrizA))
            ]

    else:
        print("ERRO! O numero de colunas da matriz A deve ser igual ao numero de linhas de matrizeB ")
        return None

def matriz(mat, titulo=None):
    if titulo:
        print(f"\n{titulo}")
    textos = [[str(v) for v in linha] for linha in mat]
    largura = max(len(v) for linha in textos for v in linha) + 2

    print('     ' + ''.join(f'{c:^{largura}}' for c in range(len(mat[0]))))
    print('  ╔' + '═' * (len(mat[0]) * largura))
    for nume, linha in enumerate(textos):
        print(f'{nume} ║  ' + ''.join(f'{v:^{largura}}' for v in linha))

def gauss(m):
    t = len(m)

    sinal = 1
    for i in range(t):
        if m[i][i] == 0:
            for k in range(i + 1, t):
                if m[k][i] != 0:
                    m[i], m[k] = m[k], m[i]
                    sinal *= -1
                    break
            else:
                return Fr(0)
            
        for j in range(i + 1, t):
            fator = m[j][i] / m[i][i]
            for k in range(i, t):
                m[j][k] -= fator * m[i][k]

    resultado = sinal
    for i in range(t):
        resultado *= m[i][i]
    return resultado

def main_SomaSubtracao(opcao):
    mA = criar_matriz()
    matriz(mA, "Matriz A")
    mB = criar_matriz()
    matriz(mB, "Matriz B")
    op = (lambda a, b: a + b) if opcao == 1 else (lambda a, b: a - b)
    resultado = sum_sub(mA, mB, op)
    matriz(resultado, "Resultado")

def main_Multiplicacao():
    mA = criar_matriz()
    matriz(mA, "Matriz A")
    mB = criar_matriz()
    matriz(mB, "Matriz B")
    resultado = multiplicacao(mA, mB)
    if resultado is not None:
        matriz(resultado, "Resultado")

def main_Determinante():
    mD = criar_matriz()
    matriz(mD, "Matriz original")
    det = gauss(mD)
    if det is not None:
        print(f"\nO determinante e: {det}")

# exemplo:     
#  linha 2 = linha 2 − 
# (elemento que vai virar 0, que está na linha 2 ÷ elemento pivô, que está na linha pivô) 
# × linha pivô inteira

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
                main_SomaSubtracao(opcao) 
            case 3:
                main_Multiplicacao()
            case 4:
                main_Determinante()
            case 0:
                Tela.reloading("Encerrando sistema")
                sys.exit()
            case _:
                print("Digite apenas uma das opcoes")
                Tela.reloading("Reiniciando")
                continue

        input("\nPressione Enter para voltar ao menu...")

if __name__ == '__main__':
    main()
