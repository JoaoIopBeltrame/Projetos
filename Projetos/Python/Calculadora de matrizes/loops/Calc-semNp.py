import os, sys, time
from fractions import Fraction

RESPONSES_YES = ["Sim", "S", "Si"]
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


def criar_matriz(): # serve para matriz A e B
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
    m = [[Fraction(0) for _ in range(c)] for _ in range(l)]
    print("Matriz atual:")
    print(m)
                
    while 1:
        try:
        
            confirmation_auto_fill = input("Deseja preencher inteira com apenas um numero?\n").strip().capitalize()
            if confirmation_auto_fill in RESPONSES_YES:
                number_fill = int(input("Digite o numero que deseja que a ua matriz seja\n> "))
                
                m = [[Fraction(number_fill) for _ in range(c)] for _ in range(l)]
                break
            
            elif confirmation_auto_fill in RESPONSES_NO: # terminar depois 
                ask_expo_num = input("Deseja Que o auto preenchimento tenha um cresmento exponencial?")
                print("Caso contrario sera tera que colocar manualmente cada numero")
                
                if ask_expo_num in RESPONSES_YES:
                    Tela.regra()
                    number = int(input(">> "))
                    ...
                elif ask_expo_num in RESPONSES_NO:
                    for lin in range(l):
                        for col in range(c):              
                            while True:
                                try:
                                    m[lin][col] = Fraction(int(input( f"Digite o numero da matriz (COORDENADA: linha -> {lin + 1} | coluna -> {col + 1})\n> ")))
                                    break
                                except ValueError:
                                    print("Digite numeros")
                    break 
                
                else:
                    ...
                
            
            else:
                print("Digite uma opção valida")
                Tela.reloading()
                continue
        
        except ValueError:
            print("Digite apenas numeros")
        
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

def matriz(matriz, titulo=None):
    if titulo:
        print(f"\n{titulo}")
    textos = [[str(v) for v in linha] for linha in matriz]
    largura = max(len(v) for linha in textos for v in linha) + 2

    print('     ' + '  '.join(f'{c:^{largura}}' for c in range(len(matriz[0]))))
    print('  ╔' + '═' * (len(matriz[0]) * (largura + 2)))
    for nume, linha in enumerate(textos):
        print(f'{nume} ║  ' + ''.join(f'{v:^{largura}}' for v in linha))



def determinante():

    l = int(input("linha >> "))
    j = int(input("coluna >> "))
    
    m = [[Fraction(0) for _ in range(j)] for _ in range(l)]

    sinal_troca_de_linha = 1    

    while len(m) > 2:

        n_atual = len(m)

        if m[0][0] == 0:
            for i in range(1, n_atual):
                if m[i][0] != 0:
                    m[0], m[i] = m[i], m[0]      # troca com a linha i (não sempre m[1])
                    sinal_troca_de_linha *= -1
                    break
        else:
            return Fraction(0) #coluna inteira de 0
    
    

    nova_matriz = [[Fraction(0) for _ in range(n_atual - 1)] for _ in range(n_atual - 1)]

    pivo = m[0][0]
    fator = m[1][0] / pivo
    
    for l in range(n_atual -1):
        for c in range(n_atual -1):
            nova_matriz[i][j] = m[i][j] - fator * m[0][j]
            print(nova_matriz)
        
    m = nova_matriz

    a, b = m[0]
    c, d = m[1]

    return sinal_troca_de_linha * (a * d - c * b)















