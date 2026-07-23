import os, sys, time
from fractions import Fraction as Fr

AZ   = "\033[34m"
VERD = "\033[32m"
VERM = "\033[31m"
CI   = "\033[36m"
AMA  = "\033[33m"
ROSA = "\033[35m"
NEG  = "\033[1m"
RE   = "\033[0m"

class Tela:
    @staticmethod
    def reloading(palavra, vezes=5):
        for i in range(vezes):
            os.system("cls" if os.name == "nt" else "clear")
            sys.stdout.write(f"{CI}{palavra}{RE}")
            for k in range(3):
                sys.stdout.write(f"{AMA}.{RE}")
                sys.stdout.flush()
                time.sleep(0.17)
            print()

    @staticmethod
    def pausa_erro():
        time.sleep(1.3)

    @staticmethod
    def tabela():
        opcoes = [
            ("1", "Somar matrizes", VERD),
            ("2", "Subtrair matrizes", VERD),
            ("3", "Multiplicar", ROSA),
            ("4", "Determinante", VERM),
            ("5", "Transposta", CI),
            ("6", "Traço", CI),
            ("7", "Norma", CI),
            ("8", "Rank", AMA),
            ("9", "Inversa", AMA),
            ("0", "Sair", VERM),
        ]
        larg = 30
        titulo = "CALCULADORA DE MATRIZES"
        print()
        print(f"{NEG}{AZ}╔" + "═" * (larg + 4) + f"╗{RE}")
        print(f"{NEG}{AZ}║{RE}{NEG}{titulo:^{larg + 4}}{RE}{NEG}{AZ}║{RE}")
        print(f"{NEG}{AZ}╠═══╦" + "═" * larg + f"╣{RE}")
        for num, texto, cor in opcoes:
            print(f"{NEG}{AZ}║{RE} {cor}{num}{RE} {NEG}{AZ}║{RE} {cor}{texto:<{larg - 2}}{RE} {NEG}{AZ}║{RE}")
        print(f"{NEG}{AZ}╚═══╩" + "═" * larg + f"╝{RE}")

    @staticmethod
    def titulo(msg, cor=AZ):
        linha = "─" * (len(msg) + 4)
        print(f"\n{NEG}{cor}┌{linha}┐{RE}")
        print(f"{NEG}{cor}│  {msg}  │{RE}")
        print(f"{NEG}{cor}└{linha}┘{RE}\n")

    @staticmethod
    def sucesso(msg):
        print(f"{VERD}✓ {msg}{RE}")

    @staticmethod
    def erro(msg):
        print(f"{VERM}✗ Erro: {msg}{RE}")

    @staticmethod
    def aviso(msg):
        print(f"{AMA}⚠ {msg}{RE}")

    @staticmethod
    def info(msg):
        print(f"{CI}i {msg}{RE}")

    @staticmethod
    def regra():
        print(f"""{NEG}{AMA}
        Exemplo de crescimento exponencial:{RE}
        • Digite o número inicial: {AZ}2{RE}
        • Resultado: {AZ}2{RE} → {AZ}4{RE} → {AZ}8{RE} → {AZ}16{RE} → ...

        {AMA}Digite um limite para parar a sequência{RE}
        """)

class Matriz:
    @staticmethod
    def criar(quadrada=False):
        while True:
            try:
                print(f"\n{NEG}{CI}→ Criando matriz{RE}")
                if quadrada:
                    n = int(input(f"{AZ}  Ordem (n de n×n){RE}: "))
                    l = c = n
                else:
                    l = int(input(f"{AZ}  Linhas{RE}: "))
                    c = int(input(f"{AZ}  Colunas{RE}: "))

                if l < 1 or c < 1:
                    Tela.erro("Dimensões devem ser ≥ 1")
                    Tela.pausa_erro()
                    continue

            except ValueError:
                Tela.erro("Digite apenas números inteiros")
                Tela.pausa_erro()
                continue
            except Exception as e:
                Tela.erro(f"Erro inesperado: {str(e)}")
                print("Pressione ENTER para continuar")
                input(">>")
                continue
            break

        m = [[Fr(0) for _ in range(c)] for _ in range(l)]
        print(f"{VERD}Matriz {l}x{c} criada{RE}")
        return Matriz.preencher(m, l, c)

    @staticmethod
    def preencher(m, l, c):
        while True:
            try:
                print(f"\n{NEG}{AMA}→ Como preencher?{RE}")
                print(f"  {AZ}[S]{RE} Número único")
                print(f"  {AZ}[N]{RE} Manual ou exponencial")
                choice = input(f"{AMA}Escolha{RE}: ").strip().upper()

                if choice in ["S", "SIM", "SI", "Y", "YES"]:
                    number_fill = int(input(f"{AZ}Número para toda matriz{RE}: "))
                    m = [[Fr(number_fill) for _ in range(c)] for _ in range(l)]
                    Tela.sucesso(f"Preenchido com {number_fill}")
                    return m

                elif choice in ["N", "NAO", "NO"]:
                    return Matriz._preencher_avancado(m, l, c)
                else:
                    Tela.erro("Digite S ou N")
                    Tela.pausa_erro()

            except ValueError:
                Tela.erro("Entrada inválida")
                Tela.pausa_erro()
                continue

    @staticmethod
    def _preencher_avancado(m, l, c):
        while True:
            print(f"\n{NEG}{ROSA}→ Tipo de preenchimento{RE}")
            print(f"  {AZ}[S]{RE} Exponencial (crescimento automático)")
            print(f"  {AZ}[N]{RE} Manual (digita cada número)")
            ask_expo = input(f"{ROSA}Escolha{RE}: ").strip().upper()

            if ask_expo in ["S", "SIM", "SI", "Y", "YES"]:
                return Matriz._preencher_exponencial(m)
            elif ask_expo in ["N", "NAO", "NO"]:
                return Matriz._preencher_manual(m, l, c)
            else:
                Tela.erro("Digite S ou N")
                time.sleep(1)

    @staticmethod
    def _preencher_exponencial(m):
        Tela.regra()
        while True:
            print(f"{NEG}{CI}→ Modo de crescimento{RE}")
            print(f"  {AZ}[1]{RE} Mesmo crescimento em toda matriz")
            print(f"  {AZ}[2]{RE} Crescimento diferente em cada linha")
            modo = input(f"{CI}Escolha{RE}: ").strip()

            if modo == "1":
                return Matriz._expo_matriz_inteira(m)
            elif modo == "2":
                return Matriz._expo_linha_por_linha(m)
            else:
                Tela.erro("Digite 1 ou 2")
                Tela.pausa_erro()

    @staticmethod
    def _expo_matriz_inteira(m):
        print(f"\n{NEG}{AMA}→ Opção ao atingir limite{RE}")
        print(f"  {AZ}[1]{RE} Preencher resto com 0")
        print(f"  {AZ}[2]{RE} Reiniciar a sequência")
        continua = input(f"{AMA}Escolha{RE}: ").strip()

        numero_inicial = Fr(int(input(f"{AZ}Número inicial{RE}: ")))
        numero_limite = Fr(int(input(f"{AZ}Limite (parar em){RE}: ")))
        numero_crescimento = Fr(int(input(f"{AZ}Fator de crescimento (ex: 2){RE}: ")))

        if continua == "1":
            for lin in range(len(m)):
                for col in range(len(m[0])):
                    if numero_inicial <= numero_limite:
                        m[lin][col] = numero_inicial
                        numero_inicial *= numero_crescimento
                    else:
                        m[lin][col] = Fr(0)
            Tela.sucesso("Matriz preenchida (resto = 0)")
        elif continua == "2":
            numero_inicial_holder = numero_inicial
            for lin in range(len(m)):
                numero_inicial = numero_inicial_holder
                for col in range(len(m[0])):
                    if numero_inicial <= numero_limite:
                        m[lin][col] = numero_inicial
                        numero_inicial *= numero_crescimento
                    else:
                        m[lin][col] = Fr(0)
            Tela.sucesso("Matriz preenchida (reiniciado)")

        return Matriz._tratar_zeros(m)

    @staticmethod
    def _expo_linha_por_linha(m):
        for lin in range(len(m)):
            print(f"\n{NEG}{CI}Linha {lin + 1}/{len(m)}{RE}")
            numero_inicial = Fr(int(input(f"{AZ}  Número inicial{RE}: ")))
            numero_limite = Fr(int(input(f"{AZ}  Limite{RE}: ")))
            numero_crescimento = Fr(int(input(f"{AZ}  Crescimento{RE}: ")))

            for col in range(len(m[0])):
                if numero_inicial <= numero_limite:
                    m[lin][col] = numero_inicial
                    numero_inicial *= numero_crescimento
                else:
                    m[lin][col] = Fr(0)
        Tela.sucesso("Preenchimento linha por linha concluído")
        return Matriz._tratar_zeros(m)

    @staticmethod
    def _preencher_manual(m, l, c):
        for lin in range(l):
            for col in range(c):
                while True:
                    try:
                        valor = Fr(int(input(f"{AZ}[{lin + 1},{col + 1}]{RE}: ")))
                        m[lin][col] = valor
                        break
                    except ValueError:
                        Tela.erro("Digite um número inteiro")
        Tela.sucesso("Preenchimento manual concluído")
        return m

    @staticmethod
    def _tratar_zeros(m):
        tem_zero = any(v == 0 for linha in m for v in linha)
        if not tem_zero:
            return m

        Matriz.exibir(m, "Matriz atual (zeros vieram do limite)")
        print(f"\n{NEG}{AMA}→ Alguns valores ficaram 0{RE}")
        print(f"  {AZ}[S]{RE} Preencher os zeros manualmente")
        print(f"  {AZ}[N]{RE} Deixar como 0")

        while True:
            escolha = input(f"{AMA}Escolha{RE}: ").strip().upper()
            if escolha in ["N", "NAO", "NO"]:
                return m
            if escolha in ["S", "SIM", "SI", "Y", "YES"]:
                break
            Tela.erro("Digite S ou N")

        for i, linha in enumerate(m):          # i = indice da LINHA
            for j, valor in enumerate(linha):  # j = indice da COLUNA
                if valor == 0:
                    while True:
                        try:
                            m[i][j] = Fr(int(input(f"{AZ}[{i + 1},{j + 1}] (era 0){RE}: ")))
                            break
                        except ValueError:
                            Tela.erro("Digite um número inteiro")
        Tela.sucesso("Zeros preenchidos")
        return m

    @staticmethod
    def exibir(mat, titulo=None):
        if not mat or len(mat) == 0 or len(mat[0]) == 0:
            return

        if titulo:
            print(f"\n{NEG}{ROSA}{titulo}{RE}")

        textos = [[str(v) for v in linha] for linha in mat]
        cols = len(mat[0])
        cel = max(len(v) for linha in textos for v in linha) + 2
        if cel < 3:
            cel = 3
        rot = len(str(len(mat) - 1))
        margem = " " * (rot + 1)

        print(f"{CI}{margem} " + "".join(f"{c:^{cel}}" for c in range(cols)) + f"{RE}")
        print(f"{AZ}{margem}┌" + "─" * (cols * cel) + f"┐{RE}")
        for i, linha in enumerate(textos):
            celulas = "".join(f"{v:^{cel}}" for v in linha)
            print(f"{CI}{i:>{rot}} {AZ}│{VERD}{celulas}{AZ}│{RE}")
        print(f"{AZ}{margem}└" + "─" * (cols * cel) + f"┘{RE}")

class Operacoes:
    @staticmethod
    def soma_subtracao(matrizA, matrizB, operador):
        if len(matrizA) == len(matrizB) and len(matrizA[0]) == len(matrizB[0]):
            return [
                [operador(matrizA[lin][col], matrizB[lin][col]) for col in range(len(matrizA[0]))]
                for lin in range(len(matrizA))
            ]
        else:
            Tela.erro(f"Dimensões incompatíveis: A({len(matrizA)}x{len(matrizA[0])}) ≠ B({len(matrizB)}x{len(matrizB[0])})")
            Tela.aviso("Matrizes precisam ter EXATAMENTE o mesmo tamanho para soma/subtração")
            return None

    @staticmethod
    def multiplicacao(matrizA, matrizB):
        if len(matrizA[0]) == len(matrizB):
            return [
                [sum(matrizA[l][k] * matrizB[k][c] for k in range(len(matrizB))) for c in range(len(matrizB[0]))]
                for l in range(len(matrizA))
            ]
        else:
            Tela.erro(f"Multiplicação impossível: colunas A({len(matrizA[0])}) ≠ linhas B({len(matrizB)})")
            Tela.aviso("Colunas de A devem ser iguais às linhas de B")
            return None

    @staticmethod
    def determinante(m):
        if len(m) == 0 or len(m[0]) == 0:
            Tela.erro("Matriz vazia não pode ter determinante")
            return None

        if len(m) != len(m[0]):
            Tela.erro(f"Matriz não é quadrada: {len(m)}x{len(m[0])}")
            Tela.aviso("Determinante só existe para matrizes quadradas (nxn)")
            return None

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

    @staticmethod
    def transposta(m):
        return [list(col) for col in zip(*m)]

    @staticmethod
    def traco(m):
        if len(m) != len(m[0]):
            Tela.erro(f"Matriz não é quadrada: {len(m)}x{len(m[0])}")
            Tela.aviso("Traço só existe para matrizes quadradas (nxn)")
            return None
        return sum(m[i][i] for i in range(len(m)))

    @staticmethod
    def norma(m):
        return max(
            sum(abs(m[l][j]) for l in range(len(m)))
            for j in range(len(m[0]))
        )

    @staticmethod
    def rank(m):
        m = [linha[:] for linha in m]
        linhas = len(m)
        colunas = len(m[0])
        rank_count = 0

        for col in range(min(linhas, colunas)):
            encontrou = False
            for lin in range(rank_count, linhas):
                if m[lin][col] != 0:
                    m[rank_count], m[lin] = m[lin], m[rank_count]
                    encontrou = True
                    break

            if not encontrou:
                continue

            for lin in range(rank_count + 1, linhas):
                if m[rank_count][col] != 0:
                    fator = m[lin][col] / m[rank_count][col]
                    for c in range(colunas):
                        m[lin][c] -= fator * m[rank_count][c]

            rank_count += 1

        return rank_count

    @staticmethod
    def inversa(m):
        if len(m) == 0 or len(m[0]) == 0:
            Tela.erro("Matriz vazia não pode ter inversa")
            return None

        if len(m) != len(m[0]):
            Tela.erro(f"Matriz não é quadrada: {len(m)}x{len(m[0])}")
            Tela.aviso("Inversa só existe para matrizes quadradas (nxn)")
            return None

        n = len(m)
        aug = [linha[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
               for i, linha in enumerate(m)]

        for i in range(n):
            if aug[i][i] == 0:
                for j in range(i + 1, n):
                    if aug[j][i] != 0:
                        aug[i], aug[j] = aug[j], aug[i]
                        break
                else:
                    Tela.erro("Matriz é singular, não tem inversa")
                    Tela.aviso("Determinante é zero")
                    return None

            divisor = aug[i][i]
            for c in range(2 * n):
                aug[i][c] /= divisor

            for k in range(n):
                if k == i:
                    continue
                fator = aug[k][i]
                if fator != 0:
                    for l in range(2 * n):
                        aug[k][l] -= fator * aug[i][l]

        return [linha[n:] for linha in aug]

class Main:
    def __init__(self):
        self.ativo = True

    def executar(self):
        while self.ativo:
            Main._exibir_menu()
            self._processar_opcao()

    @staticmethod
    def _exibir_menu():
        os.system("cls" if os.name == "nt" else "clear")
        Tela.tabela()

    def _processar_opcao(self):
        try:
            opcao = int(input(f"{AMA}Escolha uma opção{RE}: "))
        except ValueError:
            Tela.erro("Digite um número")
            time.sleep(1)
            return

        match opcao:
            case 1:
                Main._soma_subtracao("Soma", lambda a, b: a + b)
            case 2:
                Main._soma_subtracao("Subtração", lambda a, b: a - b)
            case 3:
                Main._multiplicacao()
            case 4:
                Main._determinante()
            case 5:
                Main._transposta()
            case 6:
                Main._traco()
            case 7:
                Main._norma()
            case 8:
                Main._rank()
            case 9:
                Main._inversa()
            case 0:
                self._sair()
            case _:
                Tela.erro("Opção inválida")
                time.sleep(1)

        if self.ativo:
            input(f"\n{CI}Pressione ENTER para voltar ao menu\n>>{RE}")

    @staticmethod
    def _soma_subtracao(operacao, operador):
        Tela.titulo(f"{operacao.upper()} DE MATRIZES", VERD)

        mA = Matriz.criar()
        Matriz.exibir(mA, "Matriz A")

        mB = Matriz.criar()
        Matriz.exibir(mB, "Matriz B")

        resultado = Operacoes.soma_subtracao(mA, mB, operador)

        if resultado is not None:
            Matriz.exibir(resultado, f"Resultado ({operacao})")

    @staticmethod
    def _multiplicacao():
        Tela.titulo("MULTIPLICAÇÃO DE MATRIZES", ROSA)

        mA = Matriz.criar()
        Matriz.exibir(mA, "Matriz A")

        mB = Matriz.criar()
        Matriz.exibir(mB, "Matriz B")

        resultado = Operacoes.multiplicacao(mA, mB)
        if resultado is not None:
            Matriz.exibir(resultado, "Resultado (A x B)")

    @staticmethod
    def _determinante():
        Tela.titulo("DETERMINANTE", VERM)

        mD = Matriz.criar(quadrada=True)
        Matriz.exibir(mD, "Matriz")

        det = Operacoes.determinante(mD)
        if det is not None:
            if det == 0:
                Tela.aviso(f"Determinante = {det} (matriz singular/degenerada)")
            else:
                Tela.sucesso(f"Determinante = {det}")

    @staticmethod
    def _transposta():
        Tela.titulo("TRANSPOSTA", CI)

        mT = Matriz.criar()
        Matriz.exibir(mT, "Matriz original")

        resultado = Operacoes.transposta(mT)
        Matriz.exibir(resultado, "Transposta")

    @staticmethod
    def _traco():
        Tela.titulo("TRAÇO", CI)

        mT = Matriz.criar(quadrada=True)
        Matriz.exibir(mT, "Matriz")

        resultado = Operacoes.traco(mT)
        if resultado is not None:
            Tela.sucesso(f"Traço = {resultado}")

    @staticmethod
    def _norma():
        Tela.titulo("NORMA", CI)

        mN = Matriz.criar()
        Matriz.exibir(mN, "Matriz")

        resultado = Operacoes.norma(mN)
        Tela.sucesso(f"Norma = {resultado}")

    @staticmethod
    def _rank():
        Tela.titulo("RANK", AMA)

        mR = Matriz.criar()
        Matriz.exibir(mR, "Matriz")

        resultado = Operacoes.rank(mR)
        Tela.sucesso(f"Rank = {resultado}")

    @staticmethod
    def _inversa():
        Tela.titulo("INVERSA", AMA)

        mI = Matriz.criar(quadrada=True)
        Matriz.exibir(mI, "Matriz")

        resultado = Operacoes.inversa(mI)
        if resultado is not None:
            Matriz.exibir(resultado, "Inversa")

    def _sair(self):
        Tela.sucesso("Até logo!")
        Tela.reloading("Saindo")
        self.ativo = False

if __name__ == '__main__':
    main = Main()
    main.executar()
    
