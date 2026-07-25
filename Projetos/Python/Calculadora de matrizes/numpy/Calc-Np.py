import math
import os
import sys
import time
import numpy as np
from fractions import Fraction as Fr
from typing import Callable, NamedTuple

AZ, VERD, VERM, CI, AMA, ROSA, NEG, RE = (f"\033[{c}m" for c in (34, 32, 31, 36, 33, 35, 1, 0))

class Tela:
    """Toda entrada e saída de terminal fica aqui. Nenhuma outra classe faz print/input direto."""

    @staticmethod
    def _msg(simbolo: str, cor: str, texto: str, pausa: float = 0.0) -> None:
        print(f"{cor}{simbolo} {texto}{RE}")
        time.sleep(pausa)

    @staticmethod
    def sucesso(texto: str, pausa: float = 0.0) -> None:
        Tela._msg("✓", VERD, texto, pausa)

    @staticmethod
    def erro(texto: str, pausa: float = 0.0) -> None:
        Tela._msg("✗ Erro:", VERM, texto, pausa)

    @staticmethod
    def aviso(texto: str, pausa: float = 0.0) -> None:
        Tela._msg("⚠", AMA, texto, pausa)

    @staticmethod
    def limpar() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def carregando(palavra: str, pontos: int = 3) -> None:
        sys.stdout.write(f"{CI}{palavra}{RE}")
        for _ in range(pontos):
            sys.stdout.write(f"{AMA}.{RE}")
            sys.stdout.flush()
            time.sleep(0.25)
        print()

    @staticmethod
    def titulo(texto: str, cor: str = AZ) -> None:
        linha = "─" * (len(texto) + 4)
        print(f"\n{NEG}{cor}┌{linha}┐\n│  {texto}  │\n└{linha}┘{RE}\n")

    @staticmethod
    def ler_inteiro(msg: str, minimo: int | None = None) -> int:
        while True:
            try:
                valor = int(input(f"{AZ}{msg}{RE}\n>> "))
            except ValueError:
                Tela.erro("Digite um número inteiro")
                continue
            if minimo is not None and valor < minimo:
                Tela.erro(f"Precisa ser ≥ {minimo}")
                continue
            return valor

    @staticmethod
    def ler_numero(msg: str) -> Fr:
        """Aceita inteiro (3), fração (3/4) ou decimal (0.5) e devolve Fraction exata."""
        while True:
            texto = input(f"{AZ}{msg}{RE}\n>> ").strip()
            try:
                return Fr(texto)
            except ZeroDivisionError:
                Tela.erro("Denominador não pode ser 0")
            except ValueError:
                Tela.erro("Use inteiro (3), fração (3/4) ou decimal (0.5)")

    @staticmethod
    def escolher(pergunta: str, opcoes: list, cor: str = AMA) -> str:
        print(f"\n{NEG}{cor}→ {pergunta}{RE}")
        for tecla, descricao in opcoes:
            print(f"  {AZ}[{tecla}]{RE} {descricao}")
        validas = {tecla for tecla, _ in opcoes}
        while True:
            escolha = input(f"{cor}Escolha{RE}: ").strip().upper()
            if escolha in validas:
                return escolha
            Tela.erro(f"Use: {' / '.join(sorted(validas))}", 1.0)

    @staticmethod
    def menu(operacoes: dict, larg: int = 30) -> None:
        titulo = "CALCULADORA DE MATRIZES"
        print(f"\n{NEG}{AZ}╔" + "═" * (larg + 4) + "╗")
        print(f"║{RE}{NEG}{titulo:^{larg + 4}}{AZ}║")
        print("╠═══╦" + "═" * larg + "╣" + RE)
        linhas = [(t, op.rotulo, op.cor) for t, op in operacoes.items()] + [("0", "Sair", VERM)]
        for tecla, rotulo, cor in linhas:
            print(f"{NEG}{AZ}║{RE} {cor}{tecla}{RE} {NEG}{AZ}║{RE} {cor}{rotulo:<{larg - 2}}{RE} {NEG}{AZ}║{RE}")
        print(f"{NEG}{AZ}╚═══╩" + "═" * larg + f"╝{RE}")

    @staticmethod
    def explicar_exponencial() -> None:
        print(f"""{NEG}{AMA}
        Crescimento exponencial:{RE}
        • inicial {AZ}2{RE}, fator {AZ}2{RE} → {AZ}2 → 4 → 8 → 16 → ...{RE}
        • ao passar do {AMA}limite{RE} (em módulo), a sequência para
        """)

class Matriz:
    """Criação, preenchimento e exibição. Cada matriz é um np.ndarray dtype=object
    guardando Fraction em cada célula, pra aritmética exata."""

    @staticmethod
    def criar(quadrada: bool = False) -> np.ndarray:
        print(f"\n{NEG}{CI}→ Criando matriz{RE}")
        if quadrada:
            linhas = colunas = Tela.ler_inteiro("  Ordem (n de n×n)", minimo=1)
        else:
            linhas = Tela.ler_inteiro("  Linhas", minimo=1)
            colunas = Tela.ler_inteiro("  Colunas", minimo=1)

        Tela.sucesso(f"Matriz {linhas}x{colunas} criada")
        return Matriz.preencher(np.full((linhas, colunas), Fr(0), dtype=object))

    @staticmethod
    def preencher(matriz: np.ndarray) -> np.ndarray:
        modo = Tela.escolher("Como preencher?", [
            ("1", "Um número igual em toda a matriz"),
            ("2", "Manual (digitar cada número)"),
            ("3", "Exponencial — mesma regra na matriz toda"),
            ("4", "Exponencial — uma regra por linha"),
        ])
        linhas, colunas = matriz.shape

        if modo == "1":
            numero = Tela.ler_numero("Número para toda a matriz")
            Tela.sucesso(f"Preenchido com {numero}")
            return np.full((linhas, colunas), numero, dtype=object)

        if modo == "2":
            for lin in range(linhas):
                for col in range(colunas):
                    matriz[lin, col] = Tela.ler_numero(f"[{lin + 1},{col + 1}]")
            Tela.sucesso("Preenchimento manual concluído")
            return matriz

        return Matriz._exponencial(matriz, por_linha=(modo == "4"))

    @staticmethod
    def _ler_regra(indent: str = "  ") -> tuple:
        while True:
            inicial = Tela.ler_numero(f"{indent}Número inicial")
            limite = Tela.ler_numero(f"{indent}Limite (parar em)")
            fator = Tela.ler_numero(f"{indent}Fator de crescimento (ex: 2)")
            if fator == 0:
                Tela.erro("Fator de crescimento não pode ser 0", 1.3)
                continue
            if abs(inicial) > abs(limite):
                Tela.erro(f"Inicial {inicial} já passa do limite {limite}: a matriz sairia toda zerada", 1.3)
                continue
            if fator == 1:
                Tela.aviso("Fator 1 não cresce: os valores ficam todos iguais")
            return inicial, limite, fator

    @staticmethod
    def _preencher_linha(matriz: np.ndarray, lin: int, atual: Fr, limite: Fr, fator: Fr) -> Fr:
        for col in range(matriz.shape[1]):
            if abs(atual) > abs(limite):
                matriz[lin, col] = Fr(0)
                continue
            matriz[lin, col] = atual
            atual *= fator
        return atual

    @staticmethod
    def _exponencial(matriz: np.ndarray, por_linha: bool) -> np.ndarray:
        Tela.explicar_exponencial()
        linhas = matriz.shape[0]

        if por_linha:
            for lin in range(linhas):
                print(f"\n{NEG}{CI}Linha {lin + 1}/{linhas}{RE}")
                Matriz._preencher_linha(matriz, lin, *Matriz._ler_regra())
        else:
            inicial, limite, fator = Matriz._ler_regra()
            reiniciar = Tela.escolher("Ao passar do limite", [
                ("1", "Preencher o resto com 0"),
                ("2", "Reiniciar a sequência a cada linha"),
            ]) == "2"
            atual = inicial
            for lin in range(linhas):
                atual = Matriz._preencher_linha(matriz, lin, inicial if reiniciar else atual, limite, fator)

        Tela.sucesso("Preenchimento exponencial concluído")
        return Matriz._tratar_zeros(matriz)

    @staticmethod
    def _tratar_zeros(matriz: np.ndarray) -> np.ndarray:
        zeros = list(zip(*np.where(matriz == 0)))
        if not zeros:
            return matriz

        Matriz.exibir(matriz, "Matriz atual (zeros vieram do limite)")
        if Tela.escolher("Alguns valores ficaram 0", [
            ("S", "Preencher os zeros manualmente"),
            ("N", "Deixar como 0"),
        ]) == "N":
            return matriz

        for lin, col in zeros:
            matriz[lin, col] = Tela.ler_numero(f"[{lin + 1},{col + 1}] (era 0)")
        Tela.sucesso("Zeros preenchidos")
        return matriz

    @staticmethod
    def exibir(matriz: np.ndarray, titulo: str | None = None) -> None:
        if matriz is None:
            return
        matriz = np.asarray(matriz, dtype=object)
        if matriz.size == 0 or matriz.ndim != 2:
            return

        if titulo:
            print(f"\n{NEG}{ROSA}{titulo}{RE}")

        textos = [[str(valor) for valor in linha] for linha in matriz]
        linhas, colunas = matriz.shape
        largura = max(max(len(v) for linha in textos for v in linha) + 2, 3)
        margem = " " * (len(str(linhas)) + 1)
        borda = "─" * (colunas * largura)

        print(f"{CI}{margem} " + "".join(f"{c:^{largura}}" for c in range(1, colunas + 1)) + RE)
        print(f"{AZ}{margem}┌{borda}┐{RE}")
        for i, linha in enumerate(textos, start=1):
            celulas = "".join(f"{v:^{largura}}" for v in linha)
            print(f"{CI}{i:>{len(margem) - 1}} {AZ}│{VERD}{celulas}{AZ}│{RE}")
        print(f"{AZ}{margem}└{borda}┘{RE}")

class OperacoesMat:
    """Matemática pura. Recebe matrizes e devolve resultado ou None
    (já tendo avisado o erro via Tela)."""

    @staticmethod
    def _mesma_forma(A: np.ndarray, B: np.ndarray) -> bool:
        if A.shape == B.shape:
            return True
        Tela.erro(f"Dimensões incompatíveis: {A.shape[0]}x{A.shape[1]} ≠ {B.shape[0]}x{B.shape[1]}")
        Tela.aviso("Soma/subtração exige matrizes EXATAMENTE do mesmo tamanho")
        return False

    @staticmethod
    def _e_quadrada(matriz: np.ndarray, nome: str) -> bool:
        if matriz.size == 0:
            Tela.erro(f"Matriz vazia não tem {nome}")
            return False
        if matriz.shape[0] != matriz.shape[1]:
            Tela.erro(f"Matriz {matriz.shape[0]}x{matriz.shape[1]} não é quadrada")
            Tela.aviso(f"{nome.capitalize()} só existe para matriz quadrada (n×n)")
            return False
        return True

    @staticmethod
    def _escalonar(matriz: np.ndarray) -> tuple:
        """Elimina abaixo dos pivôs. Devolve (matriz escalonada, sinal das trocas, rank)."""
        M = np.asarray(matriz, dtype=object).copy()
        linhas, colunas = M.shape
        sinal, pivo = Fr(1), 0

        for col in range(colunas):
            if pivo >= linhas:
                break
            alvo = next((lin for lin in range(pivo, linhas) if M[lin, col] != 0), None)
            if alvo is None:
                continue
            if alvo != pivo:
                M[[pivo, alvo]] = M[[alvo, pivo]]
                sinal = -sinal
            for lin in range(pivo + 1, linhas):
                if M[lin, col] != 0:
                    M[lin, col:] -= (M[lin, col] / M[pivo, col]) * M[pivo, col:]
            pivo += 1

        return M, sinal, pivo

    @staticmethod
    def soma(A: np.ndarray, B: np.ndarray) -> np.ndarray | None:
        return A + B if OperacoesMat._mesma_forma(A, B) else None

    @staticmethod
    def subtracao(A: np.ndarray, B: np.ndarray) -> np.ndarray | None:
        return A - B if OperacoesMat._mesma_forma(A, B) else None

    @staticmethod
    def multiplicacao(A: np.ndarray, B: np.ndarray) -> np.ndarray | None:
        if A.shape[1] != B.shape[0]:
            Tela.erro(f"Multiplicação impossível: colunas de A({A.shape[1]}) ≠ linhas de B({B.shape[0]})")
            return None
        return A @ B

    @staticmethod
    def transposta(matriz: np.ndarray) -> np.ndarray:
        return matriz.T

    @staticmethod
    def traco(matriz: np.ndarray) -> Fr | None:
        if not OperacoesMat._e_quadrada(matriz, "traço"):
            return None
        return sum((matriz[i, i] for i in range(matriz.shape[0])), Fr(0))

    @staticmethod
    def norma(matriz: np.ndarray) -> Fr:
        """Norma 1: maior soma de módulos entre as colunas."""
        return max(sum((abs(v) for v in matriz[:, col]), Fr(0)) for col in range(matriz.shape[1]))

    @staticmethod
    def rank(matriz: np.ndarray) -> int:
        return OperacoesMat._escalonar(matriz)[2]

    @staticmethod
    def determinante(matriz: np.ndarray) -> Fr | None:
        if not OperacoesMat._e_quadrada(matriz, "determinante"):
            return None
        escalonada, sinal, rank = OperacoesMat._escalonar(matriz)
        ordem = matriz.shape[0]
        if rank < ordem:
            return Fr(0)
        return sinal * math.prod(escalonada[i, i] for i in range(ordem))

    @staticmethod
    def inversa(matriz: np.ndarray) -> np.ndarray | None:
        if not OperacoesMat._e_quadrada(matriz, "inversa"):
            return None

        ordem = matriz.shape[0]
        identidade = np.full((ordem, ordem), Fr(0), dtype=object)
        for i in range(ordem):
            identidade[i, i] = Fr(1)
        aumentada = np.hstack([matriz.copy(), identidade])

        for i in range(ordem):
            if aumentada[i, i] == 0:
                alvo = next((j for j in range(i + 1, ordem) if aumentada[j, i] != 0), None)
                if alvo is None:
                    Tela.erro("Matriz é singular, não tem inversa")
                    Tela.aviso("Determinante é zero")
                    return None
                aumentada[[i, alvo]] = aumentada[[alvo, i]]

            aumentada[i] /= aumentada[i, i]
            for k in range(ordem):
                if k != i and aumentada[k, i] != 0:
                    aumentada[k] -= aumentada[k, i] * aumentada[i]

        return aumentada[:, ordem:]

class Operacao(NamedTuple):
    """Uma linha do menu: rótulo, cor, função e o que ela exige/devolve."""
    rotulo: str
    cor: str
    funcao: Callable
    matrizes: int = 1
    quadrada: bool = False
    escalar: bool = False
    aviso_singular: bool = False

OPERACOES = {
    "1": Operacao("Somar matrizes", VERD, OperacoesMat.soma, matrizes=2),
    "2": Operacao("Subtrair matrizes", VERD, OperacoesMat.subtracao, matrizes=2),
    "3": Operacao("Multiplicar", ROSA, OperacoesMat.multiplicacao, matrizes=2),
    "4": Operacao("Determinante", VERM, OperacoesMat.determinante, quadrada=True, escalar=True, aviso_singular=True),
    "5": Operacao("Transposta", CI, OperacoesMat.transposta),
    "6": Operacao("Traço", CI, OperacoesMat.traco, quadrada=True, escalar=True),
    "7": Operacao("Norma", CI, OperacoesMat.norma, escalar=True),
    "8": Operacao("Rank", AMA, OperacoesMat.rank, escalar=True),
    "9": Operacao("Inversa", AMA, OperacoesMat.inversa, quadrada=True),
}

class Main:
    """Loop principal: mostra o menu, lê a opção, despacha e volta pro menu."""

    def executar(self) -> None:
        while True:
            Tela.limpar()
            Tela.menu(OPERACOES)
            try:
                escolha = input(f"{AMA}Escolha uma opção{RE}\n>> ").strip()
                if escolha == "0":
                    Tela.sucesso("Até logo!")
                    Tela.carregando("Saindo")
                    return
                if escolha not in OPERACOES:
                    Tela.erro("Opção inválida", 1.0)
                    continue
                Main._rodar(OPERACOES[escolha])
                input(f"\n{CI}Pressione ENTER para voltar ao menu\n>> {RE}")
            except KeyboardInterrupt:
                Tela.aviso("\nOperação cancelada", 1.0)
            except EOFError:
                Tela.aviso("\nEntrada encerrada", 1.0)
                return

    @staticmethod
    def _rodar(op: Operacao) -> None:
        Tela.titulo(op.rotulo.upper(), op.cor)

        matrizes: list = []
        for i in range(op.matrizes):
            nome = f"Matriz {'AB'[i]}" if op.matrizes > 1 else "Matriz"
            matrizes.append(Matriz.criar(op.quadrada))
            Matriz.exibir(matrizes[-1], nome)

        resultado = op.funcao(*matrizes)
        if resultado is None:
            return
        if op.escalar:
            Tela.sucesso(f"{op.rotulo} = {resultado}")
            if op.aviso_singular and resultado == 0:
                Tela.aviso("Determinante 0 → matriz singular (não tem inversa)")
        else:
            Matriz.exibir(resultado, f"Resultado — {op.rotulo}")

if __name__ == "__main__":
    try:
        Main().executar()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{VERM}Encerrado pelo usuário{RE}")
    try:
        Main().executar()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{VERM}Encerrado pelo usuário{RE}")
