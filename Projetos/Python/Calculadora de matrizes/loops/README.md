<h1 align="center">Calculadora de Matrizes</h1>

<p align="center">
  Álgebra linear em Python puro, direto no terminal.<br>
  <strong>9 operações implementadas do zero</strong> — sem NumPy, sem bibliotecas externas.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Depend%C3%AAncias-0-2ea44f?style=for-the-badge" alt="Zero dependências">
  <img src="https://img.shields.io/badge/Paradigma-OOP-ff69b4?style=for-the-badge" alt="OOP">
  <img src="https://img.shields.io/badge/Aritm%C3%A9tica-Exata-yellow?style=for-the-badge" alt="Aritmética exata">
</p>

<!-- COLE AQUI O PRINT DO MENU PRINCIPAL -->

---

Calculadora de matrizes com interface colorida em códigos ANSI e molduras em caracteres box-drawing. O diferencial está em dois pontos: todos os cálculos usam **aritmética exata com frações** (`1/3` continua sendo `1/3`, nunca vira `0.3333333333333333`), e o código é dividido em **classes com responsabilidade única**.

A matriz é representada como `list[list[Fraction]]` — lista de listas, sem nenhuma estrutura de dados externa. Todo algoritmo de álgebra linear foi escrito à mão.

> **Versão irmã:** existe uma implementação equivalente sobre NumPy, com a mesma interface e os mesmos resultados, no repositório [calculadora-matrizes-numpy](../com-numpy). A comparação entre as duas está resumida em [Por que sem NumPy](#por-que-sem-numpy).

---

## Sumário

- [Execução](#execução)
- [Funcionalidades](#funcionalidades)
- [Demonstração](#demonstração)
- [Por que sem NumPy](#por-que-sem-numpy)
- [Bibliotecas utilizadas](#bibliotecas-utilizadas)
- [Cores e estilização no terminal](#cores-e-estilização-no-terminal)
- [Desenho das tabelas com f-string](#desenho-das-tabelas-com-f-string)
- [Arquitetura em classes](#arquitetura-em-classes)
- [O dicionário de operações](#o-dicionário-de-operações)
- [As operações matemáticas](#as-operações-matemáticas)
- [Modos de preenchimento](#modos-de-preenchimento)
- [Etapas e fluxo do programa](#etapas-e-fluxo-do-programa)
- [Validações de entrada](#validações-de-entrada)
- [Testes](#testes)
- [Problemas enfrentados](#problemas-enfrentados)

---

## Execução

```bash
python3 calculadora_matrizes.py
```

Sem `pip install`, sem ambiente virtual, sem arquivo de configuração. Python 3.10 ou superior é o único requisito — a sintaxe de tipo `int | None` foi introduzida nessa versão.

---

## Funcionalidades

| # | Operação | Requisito | Algoritmo |
|:-:|----------|-----------|-----------|
| 1 | **Soma** | Mesmas dimensões | Elemento a elemento |
| 2 | **Subtração** | Mesmas dimensões | Elemento a elemento |
| 3 | **Multiplicação** | Colunas de A = linhas de B | Produto escalar linha × coluna |
| 4 | **Determinante** | Matriz quadrada | Eliminação de Gauss com pivoteamento e controle de sinal |
| 5 | **Transposta** | Qualquer matriz | `zip(*m)` |
| 6 | **Traço** | Matriz quadrada | Soma da diagonal principal |
| 7 | **Norma** | Qualquer matriz | Norma-1 (maior soma absoluta entre colunas) |
| 8 | **Rank** | Qualquer matriz | Escalonamento por linhas + contagem de pivôs |
| 9 | **Inversa** | Quadrada e não singular | Gauss-Jordan com matriz aumentada `[A \| I]` |

Além das operações:

- Aritmética exata com frações — resultados como `3/2` em vez de `1.4999999999999998`.
- Entrada aceita **inteiro** (`3`), **fração** (`3/4`) ou **decimal** (`0.5`), sempre convertida para `Fraction`.
- Três modos de preenchimento: número único, manual célula a célula e crescimento exponencial automático.
- Exibição com moldura, índices de linha/coluna e alinhamento calculado em tempo de execução.
- Mensagens padronizadas de sucesso, erro e aviso.
- Validação de dimensões antes de cada operação — avisa em vez de quebrar.

---

## Demonstração

**Menu principal:**

```
╔══════════════════════════════════╗
║     CALCULADORA DE MATRIZES      ║
╠═══╦══════════════════════════════╣
║ 1 ║ Somar matrizes               ║
║ 2 ║ Subtrair matrizes            ║
║ 3 ║ Multiplicar                  ║
║ 4 ║ Determinante                 ║
║ 5 ║ Transposta                   ║
║ 6 ║ Traço                        ║
║ 7 ║ Norma                        ║
║ 8 ║ Rank                         ║
║ 9 ║ Inversa                      ║
║ 0 ║ Sair                         ║
╚═══╩══════════════════════════════╝
```

**Soma de duas matrizes:**

```
Matriz A            Matriz B            Resultado — Somar matrizes
    1  2                1   2               1   2
  ┌──────┐           ┌────────┐          ┌────────┐
1 │ 1  2 │          1│ 10  20 │         1│ 11  22 │
2 │ 3  4 │          2│ 30  40 │         2│ 33  44 │
  └──────┘           └────────┘          └────────┘
```

**Entrada fracionária e determinante exato:**

```
Matriz
     1    2
  ┌──────────┐
1 │ 1/2   3  │
2 │  4    5  │
  └──────────┘
✓ Determinante = -19/2
```

**Saída fracionária exata (inversa da mesma matriz):**

```
Resultado — Inversa
      1       2
  ┌────────────────┐
1 │ -10/19   6/19  │
2 │  8/19   -1/19  │
  └────────────────┘
```

Conferindo à mão: o determinante é `-19/2`, então a inversa é `(-2/19) × [[5, -3], [-4, 1/2]]`, que dá exatamente a tabela acima. Nenhum arredondamento em nenhum passo.

<!-- COLE AQUI O PRINT DE UMA INVERSA COM FRAÇÕES -->

---

## Por que sem NumPy

A pergunta natural é: por que não usar NumPy, que existe justamente para matrizes? A versão paralela do projeto foi escrita para responder isso com medição, não com opinião.

**O motivo é que `Fraction` não é um tipo que o NumPy saiba processar.** Para guardar frações, o array precisa ser criado com `dtype=object` — e isso desliga exatamente aquilo que torna o NumPy rápido. O array deixa de ser um bloco contíguo de números de tamanho fixo e vira um vetor de ponteiros para objetos Python. Cada multiplicação passa a chamar `Fraction.__mul__` no interpretador, célula por célula.

Benchmark real, multiplicação de duas matrizes 60×60 de `Fraction`:

```
numpy dtype=object  : 0.1934s
listas puras        : 0.1979s
```

Empate técnico. **O responsável por isso é o `dtype=object`:** sem tipo nativo, não há vetorização em C, e o laço continua sendo Python nos dois casos — o NumPy só adiciona uma camada de indireção por cima.

| Critério | Listas puras | NumPy com `dtype=object` |
|----------|--------------|--------------------------|
| Velocidade | igual | igual |
| Dependências | nenhuma | uma |
| Roda em máquina da faculdade / pendrive | sempre | depende do ambiente |
| Código do escalonamento | laço explícito | uma linha a menos |

A troca só se pagaria se o NumPy acelerasse alguma coisa. Como não acelera, esta é a versão principal do projeto.

---

## Bibliotecas utilizadas

O projeto utiliza apenas bibliotecas nativas do Python, sem instalação externa.

### `os` — Interação com o sistema operacional

Usado para limpar a tela do terminal:

```python
os.system("cls" if os.name == "nt" else "clear")
```

`os.system()` executa um comando do terminal de dentro do Python. `os.name` verifica o sistema operacional: se for `'nt'` (Windows), executa `cls`; caso contrário (Linux/Mac), executa `clear`. Ambos apagam o conteúdo visível da tela.

### `sys` — Escrita direta na saída padrão

Usado na animação de saída do programa:

```python
sys.stdout.write(f"{AMA}.{RE}")
sys.stdout.flush()
time.sleep(0.25)
```

`sys.stdout.write()` escreve texto na tela **sem pular linha** (diferente do `print`). Isso permite que os pontinhos apareçam um ao lado do outro, na mesma linha. O `flush()` força a exibição imediata — sem ele, o Python guardaria os pontos no buffer e mostraria todos de uma vez no final, quebrando a animação.

**Comparação prática:**

```python
# Com flush()                          # Sem flush()
for k in range(3):                     for k in range(3):
    sys.stdout.write(".")                  sys.stdout.write(".")
    sys.stdout.flush()                     time.sleep(0.25)
    time.sleep(0.25)
```

**Resultado com `flush()`:** aparece `.` → espera → `..` → espera → `...`
**Resultado sem `flush()`:** tela vazia por 0,75s → aparece `...` de uma vez

O responsável pela diferença é o **buffer de saída**: o Python acumula texto na memória e só escreve na tela quando o buffer enche ou encontra uma quebra de linha. O `flush()` esvazia esse buffer na força.

### `time` — Controle de pausas

```python
time.sleep(1.3)
```

Pausa a execução pelo número de segundos informado. No projeto tem duas funções: dar tempo do usuário ler as mensagens de erro antes do loop repetir a pergunta, e controlar a velocidade da animação de saída. A pausa é um parâmetro opcional das próprias mensagens:

```python
Tela.erro("Fator de crescimento não pode ser 0", 1.3)
```

### `math` — Produto da diagonal

```python
return sinal * math.prod(escalonada[i][i] for i in range(ordem))
```

`math.prod()` multiplica todos os elementos de um iterável, como o `sum()` faz com adição. É o passo final do determinante, depois que a matriz já está triangularizada.

### `fractions` — Aritmética exata

É a biblioteca mais importante do projeto:

```python
from fractions import Fraction as Fr
```

`Fraction` guarda o número como **numerador e denominador separados**, em vez de convertê-lo para um decimal aproximado. Toda entrada do usuário passa por ela:

```python
return Fr(texto)
```

**Comparação prática:**

```python
# Com float                      # Com Fraction
resultado = 1/3                  resultado = Fr(1, 3)
print(resultado * 3 == 1)        print(resultado * 3 == 1)
```

**Resultado com float:** `False`
**Resultado com Fraction:** `True`

O responsável pela diferença é a **representação binária do float**: `1/3` não tem representação exata em base 2, então o Python guarda `0.333333333333333314829...`. Multiplicando por 3 dá `0.9999999999999998`, que não é igual a 1. O `Fraction` guarda literalmente `1/3` e faz a multiplicação como fração: `(1×3)/3 = 3/3 = 1`.

Isso é decisivo aqui porque a eliminação de Gauss faz dezenas de divisões seguidas. Com float, um determinante que deveria dar `0` sai como `-4.44e-16`, e a checagem `if det == 0` para detectar matriz singular **nunca funcionaria**.

Outro detalhe: `Fraction` lê string direto, e é isso que permite aceitar os três formatos de entrada com uma linha só.

| O usuário digita | `Fr(texto)` guarda |
|------------------|--------------------|
| `3` | `3` |
| `3/4` | `3/4` |
| `0.5` | `1/2` |
| `-2/6` | `-1/3` (simplifica sozinho) |

### `typing` — Contrato do menu

```python
from typing import Callable, NamedTuple
```

`NamedTuple` cria a estrutura `Operacao`, que descreve cada linha do menu. `Callable` é a anotação de tipo para "isto é uma função" — o campo que guarda qual conta será executada.

---

## Cores e estilização no terminal

A interface colorida é feita com **sequências de escape ANSI**, códigos especiais interpretados pelo terminal para alterar cor e estilo do texto. As oito são criadas numa linha só:

```python
AZ, VERD, VERM, CI, AMA, ROSA, NEG, RE = (f"\033[{c}m" for c in (34, 32, 31, 36, 33, 35, 1, 0))
```

Uma expressão geradora produz as oito strings a partir dos números, e o desempacotamento múltiplo distribui cada uma em sua variável. O resultado é idêntico a escrever oito atribuições:

```python
AZ   = "\033[34m"   # Azul
VERD = "\033[32m"   # Verde
VERM = "\033[31m"   # Vermelho
CI   = "\033[36m"   # Ciano
AMA  = "\033[33m"   # Amarelo
ROSA = "\033[35m"   # Rosa/Magenta
NEG  = "\033[1m"    # Negrito
RE   = "\033[0m"    # Reset (volta ao normal)
```

Para usar, basta colocar a variável da cor antes do texto e o `RE` (reset) depois:

```python
print(f"{VERD}✓ Matriz criada{RE}")
```

**Resultado no terminal:** o texto aparece em verde, e o reset garante que o próximo texto volte à cor padrão. Sem o `RE`, **todo** o resto do terminal continuaria verde — inclusive depois do programa fechar.

As mensagens são padronizadas em três métodos da classe `Tela`, todos construídos sobre um método privado comum:

```python
@staticmethod
def _msg(simbolo: str, cor: str, texto: str, pausa: float = 0.0) -> None:
    print(f"{cor}{simbolo} {texto}{RE}")
    time.sleep(pausa)
```

| Método | Cor | Símbolo | Quando usar |
|--------|-----|---------|-------------|
| `Tela.sucesso()` | Verde | `✓` | Operação concluída |
| `Tela.erro()` | Vermelho | `✗` | Entrada inválida ou operação impossível |
| `Tela.aviso()` | Amarelo | `⚠` | Explica *por que* o erro aconteceu |

O padrão de uso é **erro + aviso juntos**: o erro diz o que houve, o aviso ensina a regra.

```python
Tela.erro(f"Matriz {len(matriz)}x{len(matriz[0])} não é quadrada")
Tela.aviso(f"{nome.capitalize()} só existe para matriz quadrada (n×n)")
```

**Resultado no terminal:**

```
✗ Erro: Matriz 2x3 não é quadrada
⚠ Determinante só existe para matriz quadrada (n×n)
```

<!-- COLE AQUI O PRINT DAS MENSAGENS DE ERRO/AVISO -->

> As cores ANSI funcionam nativamente no Linux, no Mac, no Windows Terminal e no PowerShell 7+. No `cmd.exe` antigo os códigos podem aparecer como texto cru.

---

## Desenho das tabelas com f-string

As molduras usam **caracteres box-drawing** do Unicode, que se conectam formando linhas contínuas:

```
Bordas simples:  ┌ ─ ┐ │ └ ┘
Bordas duplas:   ╔ ═ ╗ ║ ╚ ╝
Junções:         ╠ ╣ ╦ ╩
```

O alinhamento dentro da moldura é feito com **especificadores de formato dentro da f-string**:

```python
larg = 30
titulo = "CALCULADORA DE MATRIZES"

print(f"║{titulo:^{larg + 4}}║")
```

**Resultado no terminal:**

```
║     CALCULADORA DE MATRIZES      ║
```

Aqui tem uma f-string **aninhada**: as chaves internas `{larg + 4}` são resolvidas primeiro e viram o número `34`, então o Python lê `{titulo:^34}` — centralizar o título em 34 caracteres. É isso que permite mudar a largura da tabela inteira alterando uma única variável.

| Especificador | O que faz | Exemplo | Saída |
|---------------|-----------|---------|-------|
| `:^10` | Centraliza em 10 espaços | `f"{'oi':^10}"` | `    oi    ` |
| `:<10` | Alinha à esquerda | `f"{'oi':<10}"` | `oi        ` |
| `:>10` | Alinha à direita | `f"{'oi':>10}"` | `        oi` |

No método `Matriz.exibir()`, a largura da célula é **calculada em tempo de execução** a partir do maior número da matriz:

```python
textos = [[str(valor) for valor in linha] for linha in matriz]
largura = max((max(len(v) for linha in textos for v in linha) + 2), 3)
```

Cada valor vira texto, mede-se o mais comprido e soma-se 2 de respiro — com piso de 3, para matrizes de um dígito não ficarem espremidas. Por isso a moldura fica alinhada tanto com números de 1 dígito quanto com frações como `-10/19`:

```
Largura = 3                   Largura = 8
    1  2  3                        1       2
  ┌─────────┐                 ┌────────────────┐
1 │ 1  2  3 │               1 │ -10/19   6/19  │
2 │ 4  5  6 │               2 │  8/19   -1/19  │
3 │ 7  8  9 │                 └────────────────┘
  └─────────┘
```

A margem à esquerda também é calculada, para o número da linha nunca desalinhar a moldura:

```python
margem = " " * (len(str(linhas)) + 1)
```

Uma matriz de 9 linhas usa margem de 2 caracteres; uma de 12 linhas usa 3, porque `"12"` ocupa dois dígitos.

---

## Arquitetura em classes

O código é dividido em **quatro classes e uma estrutura de dados**, cada uma com uma responsabilidade única.

| Classe | Responsabilidade | Não faz | Métodos principais |
|--------|------------------|---------|--------------------|
| `Tela` | Toda a parte visual: menu, molduras, mensagens, animações, leitura do teclado | Não sabe o que é uma matriz | `menu()`, `titulo()`, `sucesso()`, `erro()`, `aviso()`, `ler_numero()`, `escolher()` |
| `Matriz` | Criar, preencher e exibir matrizes | Não faz cálculo matemático | `criar()`, `preencher()`, `exibir()`, `_exponencial()`, `_tratar_zeros()` |
| `OperacoesMat` | Matemática pura: recebe matriz, devolve resultado | Não lê teclado | `soma()`, `multiplicacao()`, `determinante()`, `inversa()`, `rank()`, `_escalonar()` |
| `Operacao` | Estrutura de dados: descreve uma linha do menu | Não executa nada | `NamedTuple` com 7 campos |
| `Main` | Controle de fluxo e despacho do menu | Não implementa algoritmo | `executar()`, `_rodar()` |

Fora das classes existem duas funções auxiliares, porque são construtoras de dado e não pertencem a nenhuma responsabilidade específica:

```python
def nova_matriz(linhas: int, colunas: int, valor=0) -> list:
    v = Fr(valor)
    return [[v for _ in range(colunas)] for _ in range(linhas)]

def matriz_identidade(ordem: int) -> list:
    return [[Fr(1) if i == j else Fr(0) for j in range(ordem)] for i in range(ordem)]
```

Repare que `nova_matriz` cria `Fr(valor)` **uma vez** e repete a referência em todas as células. Isso é seguro porque `Fraction` é **imutável** — nenhuma célula pode alterar o objeto que as outras estão apontando. Com um tipo mutável (uma lista, por exemplo) essa mesma linha seria um bug clássico.

A regra que amarra tudo: **só a `Tela` faz `print` e `input`**. As operações matemáticas chamam `Tela.erro()` para avisar e devolvem `None`, mas nunca escrevem direto.

A vantagem prática dessa separação: `OperacoesMat` pode ser testada sozinha, sem terminal. E trocar a interface por uma janela gráfica exigiria reescrever só `Tela` e `Main`.

### Por que quase tudo é `@staticmethod`

```python
class OperacoesMat:
    @staticmethod
    def transposta(matriz: list) -> list:
        return [list(col) for col in zip(*matriz)]
```

O `@staticmethod` significa que o método **não usa `self`** — ele não precisa de nenhum dado guardado no objeto. `transposta()` recebe a matriz como parâmetro, calcula e devolve; não existe "estado" para lembrar entre chamadas.

Por isso `OperacoesMat.transposta(m)` é chamado direto pelo nome da classe, sem criar objeto.

| Situação | O que usar |
|----------|-----------|
| O método precisa ler ou alterar algo guardado no objeto | `self` |
| O método só transforma o que recebeu por parâmetro | `@staticmethod` |

Neste projeto **nenhuma classe guarda estado**. Nem a `Main`: o laço principal é um `while True` que sai com `return`, sem precisar de uma flag `self.ativo`.

```python
if escolha == "0":
    Tela.sucesso("Até logo!")
    Tela.carregando("Saindo")
    return
```

O `return` encerra `executar()`, que encerra o `if __name__ == "__main__"`, que encerra o programa. Uma variável de controle a menos para manter sincronizada.

---

## O dicionário de operações

Não existe `match/case` nem cadeia de `if` para rotear o menu. Cada operação é uma **tupla nomeada** que descreve o que ela precisa e o que devolve:

```python
class Operacao(NamedTuple):
    rotulo: str
    cor: str
    funcao: Callable
    matrizes: int = 1
    quadrada: bool = False
    escalar: bool = False
    aviso_singular: bool = False
```

E o menu inteiro é um dicionário dessas tuplas:

```python
OPERACOES = {
    "1": Operacao("Somar matrizes", VERD, OperacoesMat.soma, matrizes=2),
    "4": Operacao("Determinante", VERM, OperacoesMat.determinante,
                  quadrada=True, escalar=True, aviso_singular=True),
    "5": Operacao("Transposta", CI, OperacoesMat.transposta),
    ...
}
```

Repare que `OperacoesMat.soma` aparece **sem parênteses** — é a referência à função, não a chamada dela. Com parênteses, o Python tentaria executar a soma no momento de montar o menu.

O método `Main._rodar()` lê esses campos e monta o roteiro:

| Campo | O que ele decide |
|-------|------------------|
| `rotulo` | Texto do título e do resultado |
| `cor` | Cor do título |
| `funcao` | Qual conta é executada |
| `matrizes` | Quantas voltas o laço de coleta dá (1 ou 2) |
| `quadrada` | Se `criar()` pede a ordem ou pede linhas × colunas |
| `escalar` | Se a saída é linha de texto ou tabela |
| `aviso_singular` | Se checa determinante zero |

O coração disso é uma linha só:

```python
resultado = op.funcao(*matrizes)
```

O `*` desempacota a lista em argumentos posicionais:

| `op.matrizes` | `matrizes` | Vira a chamada |
|---|---|---|
| 1 | `[A]` | `OperacoesMat.determinante(A)` |
| 2 | `[A, B]` | `OperacoesMat.soma(A, B)` |

**Consequência prática:** para adicionar uma operação nova ao programa, escreve-se a função em `OperacoesMat` e uma linha em `OPERACOES`. O `_rodar()` não é tocado.

---

## As operações matemáticas

### Escalonamento — a base de tudo

`determinante()` e `rank()` compartilham o mesmo motor. `_escalonar()` devolve três coisas de uma vez:

```python
return M, sinal, pivo
```

| Valor | O que é | Quem usa |
|-------|---------|----------|
| `M` | A matriz já triangularizada | `determinante()` (produto da diagonal) |
| `sinal` | `1` ou `-1`, conforme o número de trocas de linha | `determinante()` |
| `pivo` | Quantidade de pivôs encontrados | `rank()` (é o próprio rank) |

A primeira linha do método é a mais importante:

```python
M = [linha[:] for linha in matriz]
```

Isso **copia** a matriz antes de destruí-la. O `[:]` copia cada linha interna — um `matriz.copy()` simples não resolveria, porque criaria uma lista nova apontando para as **mesmas listas internas**, e alterar `M[0][0]` alteraria a matriz original do usuário.

A eliminação em si é um laço explícito sobre as colunas da linha:

```python
for lin in range(pivo + 1, linhas):
    if M[lin][col] != 0:
        fator = M[lin][col] / M[pivo][col]
        for k in range(col, colunas):
            M[lin][k] -= fator * M[pivo][k]
```

O `fator` é calculado **antes** do laço interno de propósito. Se ele fosse recalculado dentro, a primeira iteração já zeraria `M[lin][col]` e o fator viraria zero nas colunas seguintes — a linha ficaria pela metade.

### Determinante — eliminação de Gauss

O determinante é calculado escalonando a matriz até virar triangular superior e depois multiplicando a diagonal. Duas regras de álgebra linear sustentam isso:

1. Somar um múltiplo de uma linha a outra **não altera** o determinante.
2. Trocar duas linhas de lugar **inverte o sinal** do determinante.

Por isso existe a variável `sinal`:

```python
if alvo != pivo:
    M[pivo], M[alvo] = M[alvo], M[pivo]
    sinal *= -1
```

A troca usa **atribuição múltipla**, que avalia o lado direito inteiro antes de atribuir — por isso não precisa de variável temporária.

Quando o pivô (elemento da diagonal) é zero, não dá para dividir por ele — o algoritmo procura uma linha abaixo com valor não nulo naquela coluna e troca. A busca usa `next()` com um gerador e um padrão de segurança:

```python
alvo = next((lin for lin in range(pivo, linhas) if M[lin][col] != 0), None)
if alvo is None:
    continue
```

O segundo argumento do `next()` é o valor devolvido quando o gerador se esgota. Sem ele, o Python levantaria `StopIteration` em vez de avisar que a coluna é toda zero. Coluna toda zero significa que não há pivô ali: pula para a próxima coluna **sem** incrementar o contador de pivôs — e é exatamente isso que faz o rank sair certo em matrizes não quadradas.

No final, a checagem de singularidade não depende do produto:

```python
if rank < ordem:
    return Fr(0)
return sinal * math.prod(escalonada[i][i] for i in range(ordem))
```

Se faltou pivô, o determinante é zero por definição — não precisa multiplicar nada.

### Inversa — Gauss-Jordan com matriz aumentada

A inversa é calculada colando a matriz identidade ao lado da matriz original:

```python
identidade = matriz_identidade(ordem)
aumentada = [matriz[i][:] + identidade[i] for i in range(ordem)]
```

O `+` entre duas listas as **concatena** — é assim que cada linha da aumentada nasce com o dobro do comprimento.

**Resultado para uma matriz 2×2:**

```
Matriz original      Matriz aumentada [A | I]
┌       ┐            ┌               ┐
│ 1   2 │      →     │ 1   2 │ 1   0 │
│ 3   4 │            │ 3   4 │ 0   1 │
└       ┘            └               ┘
```

Depois o escalonamento transforma o lado esquerdo em identidade, e o lado direito vira a inversa automaticamente. No final, corta-se a metade da esquerda:

```python
return [linha[ordem:] for linha in aumentada]
```

**O detalhe do `for/else`:** na busca por um pivô válido, o `else` não pertence ao `if` — pertence ao `for`. Ele só executa se o laço terminar **sem passar por `break`**, ou seja, se nenhuma linha abaixo tinha valor não nulo naquela coluna:

```python
for j in range(i + 1, ordem):
    if aumentada[j][i] != 0:
        aumentada[i], aumentada[j] = aumentada[j], aumentada[i]
        break
else:
    Tela.erro("Matriz é singular, não tem inversa")
    Tela.aviso("Determinante é zero")
    return None
```

Sem o `for/else`, seria preciso uma variável de flag (`achou = False`) e um `if` depois do laço — três linhas a mais para dizer a mesma coisa.

### Norma-1

```python
return max(
    sum((abs(matriz[l][j]) for l in range(len(matriz))), Fr(0))
    for j in range(len(matriz[0]))
)
```

Para cada coluna, soma o módulo de todos os elementos; devolve a maior dessas somas. O `Fr(0)` como segundo argumento do `sum()` garante que o acumulador comece como fração, não como `int`.

---

## Modos de preenchimento

| Modo | Como funciona | Quando usar |
|------|---------------|-------------|
| Número único | Preenche todas as células com o mesmo valor | Matrizes constantes, teste rápido |
| Manual | Digita célula por célula, com a posição `[linha, coluna]` indicada | Matrizes específicas |
| Exponencial | Gera progressão geométrica a partir de valor inicial, fator e limite | Matrizes grandes de teste |

O modo exponencial ainda se subdivide em duas escolhas.

**Escopo do crescimento:**
- Mesma regra na matriz inteira — a sequência corre continuamente por todas as células.
- Uma regra por linha — cada linha recebe seus próprios parâmetros.

**O que fazer ao atingir o limite:**
- Preencher o resto com `0`.
- Reiniciar a sequência do começo em cada linha.

**Exemplo:** inicial `2`, fator `-2`, limite `100`, matriz 2×3.

**Resultado no terminal:**

```
     1    2    3
  ┌───────────────┐
1 │  2   -4    8  │
2 │ -16  32   -64 │
  └───────────────┘
```

A comparação com o limite usa **módulo**, não o valor com sinal:

```python
if abs(atual) > abs(limite):
```

Sem o `abs()`, um valor como `-256` passaria pela checagem `-256 > 100` (que é falsa) e continuaria sendo escrito, mesmo já tendo estourado o limite em magnitude.

O método `_preencher_linha()` devolve o **próximo valor da sequência**, e é isso que permite o modo contínuo:

```python
atual = Matriz._preencher_linha(matriz, lin, inicial if reiniciar else atual, limite, fator)
```

O ternário decide, a cada linha, se a sequência recomeça do `inicial` ou continua de onde a linha anterior parou.

### Tratamento de zeros

Se o modo "preencher com 0" deixar buracos na matriz, o programa detecta e oferece corrigir:

```python
zeros = [(i, j) for i, linha in enumerate(matriz) for j, v in enumerate(linha) if v == 0]
if not zeros:
    return matriz
```

A list comprehension com dois `for` aninhados varre a matriz inteira e guarda as **coordenadas** de cada zero — não só a informação de que existem. Assim o programa consegue perguntar célula por célula, citando a posição exata, em vez de mandar refazer tudo.

<!-- COLE AQUI O PRINT DO PREENCHIMENTO EXPONENCIAL -->

---

## Etapas e fluxo do programa

### 1. Menu principal

A tela é limpa e a tabela com as 10 opções é exibida. O usuário digita o número da operação, buscado direto no dicionário `OPERACOES`:

```python
if escolha not in OPERACOES:
    Tela.erro("Opção inválida", 1.0)
    continue
Main._rodar(OPERACOES[escolha])
```

### 2. Criação da matriz

O programa pede as dimensões. Se a operação exige matriz quadrada (determinante, traço, inversa), pede só a **ordem** e define linhas = colunas automaticamente:

```python
if quadrada:
    linhas = colunas = Tela.ler_inteiro("  Ordem (n de n×n)", minimo=1)
else:
    linhas = Tela.ler_inteiro("  Linhas", minimo=1)
    colunas = Tela.ler_inteiro("  Colunas", minimo=1)
```

Isso impede na origem que o usuário crie uma matriz inválida para aquela operação.

### 3. Preenchimento

O usuário escolhe entre os três modos descritos acima. A matriz é criada zerada e depois populada.

<!-- COLE AQUI O PRINT DA ESCOLHA DE PREENCHIMENTO -->

### 4. Exibição e cálculo

A matriz é exibida com moldura, a operação é executada e o resultado aparece — matriz nova (soma, inversa, transposta) ou valor único (determinante, traço, norma, rank), conforme o campo `escalar`.

### 5. Retorno ao menu

O programa pausa esperando ENTER, para o usuário conseguir ler o resultado antes da tela ser limpa:

```python
input(f"\n{CI}Pressione ENTER para voltar ao menu\n>> {RE}")
```

Essa pausa fica **depois** da checagem da opção "0", então quem escolheu sair não precisa apertar ENTER para se despedir.

### Interrupções

O laço principal trata dois sinais que normalmente derrubariam o programa com stack trace:

```python
except KeyboardInterrupt:
    Tela.aviso("\nOperação cancelada", 1.0)
except EOFError:
    Tela.aviso("\nEntrada encerrada", 1.0)
    return
```

`Ctrl+C` no meio de uma operação cancela e volta ao menu; `Ctrl+D` encerra o programa com mensagem limpa.

---

## Validações de entrada

Existem dois leitores diferentes, porque existem dois tipos de dado.

| Leitor | Aceita | Onde é usado |
|--------|--------|--------------|
| `Tela.ler_inteiro()` | Só inteiro, com mínimo opcional | Linhas, colunas, ordem |
| `Tela.ler_numero()` | Inteiro, fração ou decimal | Valores das células |

Dimensão fracionária não existe — não faz sentido uma matriz `2.5 × 3`. Já o conteúdo da célula precisa aceitar tudo que o `Fraction` entende:

```python
@staticmethod
def ler_numero(msg: str) -> Fr:
    while True:
        texto = input(f"{AZ}{msg}{RE}\n>> ").strip()
        try:
            return Fr(texto)
        except ZeroDivisionError:
            Tela.erro("Denominador não pode ser 0")
        except ValueError:
            Tela.erro("Use inteiro (3), fração (3/4) ou decimal (0.5)")
```

São **dois `except` diferentes para dois erros diferentes**:

| O usuário digita | O que o Python levanta | Mensagem |
|------------------|------------------------|----------|
| `abc` | `ValueError` | "Use inteiro (3), fração (3/4) ou decimal (0.5)" |
| `3/0` | `ZeroDivisionError` | "Denominador não pode ser 0" |
| `-2` | Nada — é válido | Aceito |

**Resultado no terminal:**

```
[1,1]
>> ✗ Erro: Use inteiro (3), fração (3/4) ou decimal (0.5)
[1,1]
>> ✗ Erro: Denominador não pode ser 0
[1,1]
>> ✓ Preenchimento manual concluído
```

No `ler_inteiro()`, a lógica é a mesma, mas com uma defesa a mais:

```python
try:
    valor = int(input(f"{AZ}{msg}{RE}\n>> "))
except ValueError:
    Tela.erro("Digite um número inteiro")
    continue
if minimo is not None and valor < minimo:
    Tela.erro(f"Precisa ser ≥ {minimo}")
    continue
```

O `except` só pega erro de **tipo**. Um número negativo é um inteiro perfeitamente válido para o Python — quem precisa recusar é a regra do programa, no `if`.

As escolhas de menu são normalizadas antes da comparação:

```python
escolha = input(f"{cor}Escolha{RE}: ").strip().upper()
if escolha in validas:
    return escolha
```

`.strip()` remove espaços acidentais nas pontas e `.upper()` converte para maiúscula, então `" s "`, `"S"` e `"s"` são tratados igual. O conjunto `validas` é montado a partir das próprias opções passadas — nunca fica dessincronizado com o que foi exibido na tela.

A regra do preenchimento exponencial também é validada antes de rodar:

```
✗ Erro: Inicial 50 já passa do limite 10: a matriz sairia toda zerada
```

E as operações validam dimensões **antes** de calcular, retornando `None` em vez de quebrar:

```python
if len(A[0]) != len(B):
    Tela.erro(f"Multiplicação impossível: colunas de A({len(A[0])}) ≠ linhas de B({len(B)})")
    return None
```

Quem chamou verifica o retorno:

```python
resultado = op.funcao(*matrizes)
if resultado is None:
    return
```

**Por que `is None` e não `if not resultado`:** um determinante igual a `0`, um rank `0` ou uma matriz de zeros são resultados **válidos**, mas o Python os considera falsos numa condição — `if not resultado` os esconderia da tela. O `is` compara **identidade** de objeto, não valor, então funciona igual para lista, `int` e `Fraction`.

---

## Testes

A camada matemática foi validada contra uma referência independente:

- **300 matrizes aleatórias** de ordem 1 a 4, valores de -4 a 4.
- Determinante conferido contra **expansão de Laplace** recursiva, implementada à parte só para o teste.
- Inversa conferida pela definição: `A × A⁻¹` tem que dar a identidade exata.
- Rank, norma e escalonamento comparados célula a célula contra a versão NumPy do projeto.

```
300 testes aleatorios -> falhas: 0
```

O teste só é possível porque `OperacoesMat` não imprime nada nem lê teclado — dá para importar a classe e chamar os métodos direto, sem simular entrada de usuário.

---

## Problemas enfrentados

### 1. Erro de ponto flutuante no determinante

Na primeira versão, com `float`, matrizes singulares davam determinante `-4.44e-16` em vez de `0`. Como a checagem era `if det == 0`, o programa nunca detectava a matriz singular e a inversa quebrava com divisão por zero.

**Solução:** converter tudo para `fractions.Fraction` já na entrada do usuário. Nenhuma divisão perde precisão, e a comparação com zero volta a ser confiável.

### 2. Pivô zero na eliminação de Gauss

Quando o elemento da diagonal era `0`, a linha `fator = M[lin][col] / M[pivo][col]` gerava `ZeroDivisionError`.

**Solução:** antes de dividir, procurar uma linha abaixo com valor não nulo e trocar. Se não existir nenhuma, a coluna inteira é zero: pula para a próxima coluna sem contar pivô.

### 3. O sinal invertido

Depois de implementar a troca de linhas, os determinantes começaram a sair com sinal errado em algumas matrizes.

**Causa:** cada troca de linhas inverte o sinal do determinante — regra de álgebra linear que o código estava ignorando.

**Solução:** a variável `sinal`, multiplicada por `-1` a cada troca e aplicada no produto final.

### 4. Alinhamento da moldura com números de tamanhos diferentes

Com largura de célula fixa, uma matriz contendo `1` e `-15/4` ficava com a moldura torta.

**Solução:** calcular a largura em tempo de execução, medindo o maior valor já convertido para texto, e usar esse número na f-string aninhada `{v:^{largura}}`.

### 5. Matriz alterada in-place

`determinante()` escalonava a matriz **recebida**, destruindo a original. Não causava bug visível porque a matriz é exibida antes do cálculo, mas quebraria ao calcular determinante e inversa da mesma matriz em sequência.

**Solução:** copiar antes de escalonar, dentro do próprio `_escalonar()`:

```python
M = [linha[:] for linha in matriz]
```

O `[:]` copia cada linha interna. Um `matriz.copy()` simples **não** resolveria: criaria uma lista nova, mas com as **mesmas listas internas** dentro — alterar `M[0][0]` continuaria alterando a matriz original.

### 6. Índice 1-based na entrada, 0-based na exibição

O prompt pedia o valor de `[2,3]`, mas a tabela rotulava aquela mesma célula como linha `1`, coluna `2`. Quem digitava a matriz não conseguia conferir o que digitou.

**Solução:** padronizar tudo em 1-based na exibição:

```python
print(f"{CI}{margem} " + "".join(f"{c:^{largura}}" for c in range(1, colunas + 1)) + RE)
for i, linha in enumerate(textos, start=1):
```

O cálculo da margem também mudou, de `len(str(linhas - 1))` para `len(str(linhas))` — agora o maior rótulo impresso é `linhas`, não `linhas - 1`, e sem esse ajuste uma matriz de 10 linhas desalinharia justamente na última.

### 7. Limite exponencial comparado com sinal

Com fator negativo, a sequência `2, -4, 8, -16, 32, -64, 128` passava do limite `100` sem ser barrada, porque `-64 > 100` é falso.

**Solução:** comparar módulos — `abs(atual) > abs(limite)`. "Limite" passa a significar distância do zero, que é o que o usuário espera.

### 8. Aviso de matriz singular preso a uma string

O aviso de determinante zero era disparado por `if op.rotulo == "Determinante"`. Renomear o rótulo no menu apagaria o aviso silenciosamente, sem erro nenhum.

**Solução:** o campo `aviso_singular: bool` na `Operacao`. O comportamento passou a ser configuração, não coincidência de texto.

### 9. Entrada limitada a inteiros

A calculadora usava `Fraction` internamente, mas o leitor só aceitava `int` — não dava para digitar `1/2` numa célula. A precisão exata existia só na saída.

**Solução:** o método `ler_numero()`, que entrega a string direto para o `Fraction` e trata os dois erros possíveis separadamente. `ler_inteiro()` continua existindo, restrito às dimensões.

---

## Autor

**João Pedro Iop Beltrame** — Ciência da Computação, PUCPR

[![GitHub](https://img.shields.io/badge/GitHub-JoaoIopBeltrame-181717?style=flat-square&logo=github)](https://github.com/JoaoIopBeltrame)

Projeto desenvolvido para estudo de **álgebra linear**, **estruturas de dados** e **programação orientada a objetos**.
