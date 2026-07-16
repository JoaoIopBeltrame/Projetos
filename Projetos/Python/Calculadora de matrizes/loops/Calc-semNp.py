import os, sys, time

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
        
def matriz():
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
        
        m = [[0 for _ in range(c)] for _ in range(l)]
        print("Matriz atual:")
        print(m)
                
        while 1:
            try:
            
                confirmation_auto_fill = input("Deseja preencher inteira com apenas um numero?\n").strip().capitalize()
                if confirmation_auto_fill in RESPONSES_YES:
                    number_fill = int(input("Digite o numero que deseja que a ua matriz seja\n> "))
                    
                    m = [[number_fill for _ in range(c)] for _ in range(l)]
                
                elif confirmation_auto_fill in RESPONSES_NO:
                    ask_expo_num = ("Deseja Que o auto preenchimento tenha um cresmento exponencial?\n>> ")
                    
                    if ask_expo_num in RESPONSES_YES:
                        ...
                    elif ask_expo_num in RESPONSES_NO:
                        ...
                    else:
                        ...
                    
                
                else:
                    print("Digite uma opção valida")
                    Tela.reloading()
                    continue
            
            except ValueError:
                print("Digite apenas numeros")
