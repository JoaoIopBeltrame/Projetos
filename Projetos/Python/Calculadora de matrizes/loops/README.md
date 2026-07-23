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

Calculadora de matrizes com interface colorida em códigos ANSI e molduras em caracteres box-drawing. O diferencial está em dois pontos: todos os cálculos usam **aritmética exata com frações** (`1/3` continua sendo `1/3`, nunca vira `0.3333333333333333`), e o código é dividido em **quatro classes com responsabilidade única**.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Demonstração](#demonstração)
- [Bibliotecas utilizadas](#bibliotecas-utilizadas)
- [Cores e estilização no terminal](#cores-e-estilização-no-terminal)
- [Desenho das tabelas com f-string](#desenho-das-tabelas-com-f-string)
- [Arquitetura em classes](#arquitetura-em-classes)
- [As operações matemáticas](#as-operações-matemáticas)
- [Modos de preenchimento](#modos-de-preenchimento)
- [Etapas e fluxo do programa](#etapas-e-fluxo-do-programa)
- [Validações de entrada](#validações-de-entrada)
- [Problemas enfrentados](#problemas-enfrentados)

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
- Três modos de preenchimento: número único, manual célula a célula e crescimento exponencial automático.
- Exibição com moldura, índices de linha/coluna e alinhamento calculado em tempo de execução.
- Mensagens padronizadas de sucesso, erro, aviso e informação.
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

**Exibição de matriz com índices:**

```
    0  1  2
  ┌─────────┐
0 │ 1  2  3 │
1 │ 4  5  6 │
2 │ 7  8  9 │
  └─────────┘
```

**Saída fracionária exata (inversa):**

```
      0      1
  ┌───────────────┐
0 │  -2      1    │
1 │  3/2   -1/2   │
  └───────────────┘

✓ Inversa calculada
```

<!-- COLE AQUI O PRINT DE UMA INVERSA COM FRAÇÕES -->

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
time.sleep(0.17)
```

`sys.stdout.write()` escreve texto na tela **sem pular linha** (diferente do `print`). Isso permite que os pontinhos apareçam um ao lado do outro, na mesma linha. O `flush()` força a exibição imediata — sem ele, o Python guardaria os pontos no buffer e mostraria todos de uma vez no final, quebrando a animação.

**Comparação prática:**

```python
# Com flush()                          # Sem flush()
for k in range(3):                     for k in range(3):
    sys.stdout.write(".")                  sys.stdout.write(".")
    sys.stdout.flush()                     time.sleep(0.17)
    time.sleep(0.17)
```

**Resultado com `flush()`:** aparece `.` → espera → `..` → espera → `...`
**Resultado sem `flush()`:** tela vazia por 0,51s → aparece `...` de uma vez

O responsável pela diferença é o **buffer de saída**: o Python acumula texto na memória e só escreve na tela quando o buffer enche ou encontra uma quebra de linha. O `flush()` esvazia esse buffer na força.

### `time` — Controle de pausas

```python
time.sleep(1.3)
```

Pausa a execução pelo número de segundos informado. No projeto tem duas funções: dar tempo do usuário ler as mensagens de erro antes do loop repetir a pergunta (`Tela.pausa_erro()`) e controlar a velocidade da animação de saída.

### `fractions` — Aritmética exata

É a biblioteca mais importante do projeto:

```python
from fractions import Fraction as Fr
```

`Fraction` guarda o número como **numerador e denominador separados**, em vez de convertê-lo para um decimal aproximado. Toda entrada do usuário é convertida antes de entrar na matriz:

```python
valor = Fr(int(input("[1,1]: ")))
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

---

## Cores e estilização no terminal

A interface colorida é feita com **sequências de escape ANSI**, códigos especiais interpretados pelo terminal para alterar cor e estilo do texto.

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

As mensagens são padronizadas em quatro métodos da classe `Tela`, cada um com sua cor e símbolo fixos:

| Método | Cor | Símbolo | Quando usar |
|--------|-----|---------|-------------|
| `Tela.sucesso()` | Verde | `✓` | Operação concluída |
| `Tela.erro()` | Vermelho | `✗` | Entrada inválida ou operação impossível |
| `Tela.aviso()` | Amarelo | `⚠` | Explica *por que* o erro aconteceu |
| `Tela.info()` | Ciano | `i` | Informação neutra |

O padrão de uso é **erro + aviso juntos**: o erro diz o que houve, o aviso ensina a regra.

```python
Tela.erro(f"Matriz não é quadrada: {len(m)}x{len(m[0])}")
Tela.aviso("Determinante só existe para matrizes quadradas (nxn)")
```

**Resultado no terminal:**

```
✗ Erro: Matriz não é quadrada: 2x3
⚠ Determinante só existe para matrizes quadradas (nxn)
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
textos = [[str(v) for v in linha] for linha in mat]
cel = max(len(v) for linha in textos for v in linha) + 2
```

Cada valor vira texto, mede-se o mais comprido e soma-se 2 de respiro. Por isso a moldura fica alinhada tanto com números de 1 dígito quanto com frações como `-15/4`:

```
Célula = 3                    Célula = 7
    0  1  2                         0      1
  ┌─────────┐                  ┌───────────────┐
0 │ 1  2  3 │                0 │  -2      1    │
1 │ 4  5  6 │                1 │  3/2   -1/2   │
  └─────────┘                  └───────────────┘
```

---

## Arquitetura em classes

O código é dividido em **quatro classes**, cada uma com uma responsabilidade única:

| Classe | Responsabilidade | Não faz | Métodos principais |
|--------|------------------|---------|--------------------|
| `Tela` | Toda a parte visual: menu, molduras, mensagens, animações | Não sabe o que é uma matriz | `tabela()`, `titulo()`, `sucesso()`, `erro()`, `aviso()`, `reloading()` |
| `Matriz` | Criar, preencher e exibir matrizes | Não faz cálculo matemático | `criar()`, `preencher()`, `exibir()`, `_tratar_zeros()` |
| `Operacoes` | Matemática pura: recebe matriz, devolve resultado | Não imprime nem lê nada | `soma_subtracao()`, `multiplicacao()`, `determinante()`, `inversa()`, `rank()` |
| `Main` | Controle de fluxo e roteamento do menu | Não implementa algoritmo | `executar()`, `_processar_opcao()` |

A vantagem prática dessa separação: `Operacoes` pode ser testada sozinha, sem terminal. E trocar a interface por uma janela gráfica exigiria reescrever só `Tela` e `Main`.

### Por que quase tudo é `@staticmethod`

```python
class Operacoes:
    @staticmethod
    def transposta(m):
        return [list(col) for col in zip(*m)]
```

O `@staticmethod` significa que o método **não usa `self`** — ele não precisa de nenhum dado guardado no objeto. `transposta()` recebe a matriz como parâmetro, calcula e devolve; não existe "estado" para lembrar entre chamadas.

Por isso `Operacoes.transposta(m)` é chamado direto pelo nome da classe, sem criar objeto.

**A única classe que tem estado é `Main`:**

```python
class Main:
    def __init__(self):
        self.ativo = True
```

`self.ativo` é o que mantém o programa rodando. O loop principal depende dele, e a opção "Sair" o desliga:

```python
def executar(self):
    while self.ativo:
        Main._exibir_menu()
        self._processar_opcao()

def _sair(self):
    Tela.sucesso("Até logo!")
    self.ativo = False
```

Como `_sair()` precisa **modificar** um dado do objeto, ele usa `self` e não pode ser estático.

| Situação | O que usar |
|----------|-----------|
| O método precisa ler ou alterar algo guardado no objeto | `self` |
| O método só transforma o que recebeu por parâmetro | `@staticmethod` |

---

## As operações matemáticas

### Soma e subtração num só método

Em vez de escrever dois métodos quase idênticos, a operação é passada como **função anônima**:

```python
case 1:
    Main._soma_subtracao("Soma", lambda a, b: a + b)
case 2:
    Main._soma_subtracao("Subtração", lambda a, b: a - b)
```

E dentro do método, o `operador` é chamado como qualquer função:

```python
return [
    [operador(matrizA[lin][col], matrizB[lin][col]) for col in range(len(matrizA[0]))]
    for lin in range(len(matrizA))
]
```

O que muda entre somar e subtrair é uma linha só. O `lambda` transforma a operação em **argumento**, eliminando código duplicado.

### Determinante — eliminação de Gauss

O determinante é calculado escalonando a matriz até virar triangular superior e depois multiplicando a diagonal. Duas regras de álgebra linear sustentam isso:

1. Somar um múltiplo de uma linha a outra **não altera** o determinante.
2. Trocar duas linhas de lugar **inverte o sinal** do determinante.

Por isso existe a variável `sinal`:

```python
if m[i][i] == 0:
    for k in range(i + 1, t):
        if m[k][i] != 0:
            m[i], m[k] = m[k], m[i]
            sinal *= -1
            break
    else:
        return Fr(0)
```

Quando o pivô (elemento da diagonal) é zero, não dá para dividir por ele — o algoritmo procura uma linha abaixo com valor não nulo naquela coluna e troca. Cada troca multiplica `sinal` por `-1`.

**O detalhe do `for/else`:** aquele `else` não pertence ao `if`, pertence ao `for`. Ele só executa se o loop terminar **sem passar por `break`** — ou seja, se nenhuma linha abaixo tinha valor não nulo. Isso significa que a coluna inteira é zero, e o determinante é `0` na hora.

### Inversa — Gauss-Jordan com matriz aumentada

A inversa é calculada colando a matriz identidade ao lado da matriz original:

```python
aug = [linha[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
       for i, linha in enumerate(m)]
```

**Resultado para uma matriz 2×2:**

```
Matriz original      Matriz aumentada [A | I]
┌       ┐            ┌               ┐
│ 1   2 │      →     │ 1   2 │ 1   0 │
│ 3   4 │            │ 3   4 │ 0   1 │
└       ┘            └               ┘
```

Depois o escalonamento transforma o lado esquerdo em identidade, e o lado direito vira a inversa automaticamente. No final, corta-se a metade da direita:

```python
return [linha[n:] for linha in aug]
```

Se em algum momento não existe pivô válido, a matriz é **singular** (determinante zero) e não tem inversa — o programa avisa e retorna `None`.

---

## Modos de preenchimento

| Modo | Como funciona | Quando usar |
|------|---------------|-------------|
| Número único | Preenche todas as células com o mesmo valor | Matrizes constantes, teste rápido |
| Manual | Digita célula por célula, com a posição `[linha, coluna]` indicada | Matrizes específicas |
| Exponencial | Gera progressão geométrica a partir de valor inicial, fator e limite | Matrizes grandes de teste |

O modo exponencial ainda se subdivide em duas escolhas.

**Escopo do crescimento:**
- Mesmo crescimento na matriz inteira — a sequência corre continuamente por todas as células.
- Crescimento por linha — cada linha recebe seus próprios parâmetros.

**O que fazer ao atingir o limite:**
- Preencher o resto com `0`.
- Reiniciar a sequência do começo.

**Exemplo:** inicial `2`, fator `2`, limite `50`, matriz 3×3, modo reiniciar.

**Resultado no terminal:**

```
     0   1   2
  ┌────────────┐
0 │  2   4   8 │
1 │  2   4   8 │
2 │  2   4   8 │
  └────────────┘
```

A sequência seria `2 → 4 → 8 → 16 → 32 → 64`, mas `64` passa do limite `50`. Como o modo é "reiniciar", cada linha nova volta para `2`.

<!-- COLE AQUI O PRINT DO PREENCHIMENTO EXPONENCIAL -->

### Tratamento de zeros

Se o modo "preencher com 0" deixar buracos na matriz, o programa detecta e oferece corrigir:

```python
tem_zero = any(v == 0 for linha in m for v in linha)
if not tem_zero:
    return m
```

O `any()` com dois `for` aninhados varre a matriz inteira e para no primeiro zero encontrado. Se não achar nenhum, devolve a matriz sem incomodar o usuário.

---

## Etapas e fluxo do programa

### 1. Menu principal

A tela é limpa e a tabela com as 10 opções é exibida. O usuário digita o número da operação, roteado por um `match/case`.

### 2. Criação da matriz

O programa pede as dimensões. Se a operação exige matriz quadrada (determinante, traço, inversa), pede só a **ordem** e define linhas = colunas automaticamente:

```python
if quadrada:
    n = int(input("Ordem (n de n×n): "))
    l = c = n
else:
    l = int(input("Linhas: "))
    c = int(input("Colunas: "))
```

Isso impede na origem que o usuário crie uma matriz inválida para aquela operação.

### 3. Preenchimento

O usuário escolhe entre os três modos descritos acima. A matriz é criada zerada e depois populada.

<!-- COLE AQUI O PRINT DA ESCOLHA DE PREENCHIMENTO -->

### 4. Exibição e cálculo

A matriz é exibida com moldura, a operação é executada e o resultado aparece — matriz nova (soma, inversa, transposta) ou valor único (determinante, traço, norma, rank).

### 5. Retorno ao menu

O programa pausa esperando ENTER, para o usuário conseguir ler o resultado antes da tela ser limpa:

```python
if self.ativo:
    input("\nPressione ENTER para voltar ao menu\n>>")
```

A condição `if self.ativo` evita que essa pausa apareça quando o usuário escolheu "Sair" — sem ela, o programa pediria ENTER depois de já ter se despedido.

---

## Validações de entrada

Toda entrada numérica passa pelo mesmo padrão: `while True` + `try/except`.

```python
while True:
    try:
        l = int(input("Linhas: "))
        if l < 1:
            Tela.erro("Dimensões devem ser ≥ 1")
            Tela.pausa_erro()
            continue
    except ValueError:
        Tela.erro("Digite apenas números inteiros")
        Tela.pausa_erro()
        continue
    break
```

São **duas defesas diferentes** para dois erros diferentes:

| Erro do usuário | O que acontece | Quem barra |
|-----------------|----------------|------------|
| Digita `abc` | `int()` levanta `ValueError` | O `except ValueError` |
| Digita `-3` | `int()` funciona normalmente | O `if l < 1` |

O `except` só pega erro de **tipo**. Um número negativo é um inteiro perfeitamente válido para o Python — quem precisa recusar é a regra do programa.

As escolhas de texto (S/N) são normalizadas antes da comparação:

```python
choice = input("Escolha: ").strip().upper()
if choice in ["S", "SIM", "SI", "Y", "YES"]:
```

`.strip()` remove espaços acidentais nas pontas e `.upper()` converte para maiúscula. Assim `" sim "`, `"Sim"` e `"S"` são tratados igual.

E as operações validam dimensões **antes** de calcular, retornando `None` em vez de quebrar:

```python
if len(matrizA[0]) == len(matrizB):
    return [...]
else:
    Tela.erro(f"Multiplicação impossível: colunas A({len(matrizA[0])}) ≠ linhas B({len(matrizB)})")
    Tela.aviso("Colunas de A devem ser iguais às linhas de B")
    return None
```

Quem chamou verifica o retorno:

```python
resultado = Operacoes.multiplicacao(mA, mB)
if resultado is not None:
    Matriz.exibir(resultado, "Resultado (A x B)")
```

**Por que `is not None` e não só `if resultado`:** uma matriz de zeros ou um determinante igual a `0` são resultados **válidos**, mas o Python os considera "falsos" numa condição. Usar `if resultado` esconderia esses resultados legítimos.

---

## Problemas enfrentados

### 1. Erro de ponto flutuante no determinante

Na primeira versão, com `float`, matrizes singulares davam determinante `-4.44e-16` em vez de `0`. Como a checagem era `if det == 0`, o programa nunca detectava a matriz singular e a inversa quebrava com divisão por zero.

**Solução:** converter tudo para `fractions.Fraction` já na entrada do usuário. Nenhuma divisão perde precisão, e a comparação com zero volta a ser confiável.

### 2. Pivô zero na eliminação de Gauss

Quando o elemento da diagonal era `0`, a linha `fator = m[j][i] / m[i][i]` gerava `ZeroDivisionError`.

**Solução:** antes de dividir, procurar uma linha abaixo com valor não nulo e trocar. Se não existir nenhuma, a coluna é toda zero e o determinante é `0` — retorno imediato pelo `else` do `for`.

### 3. O sinal invertido

Depois de implementar a troca de linhas, os determinantes começaram a sair com sinal errado em algumas matrizes.

**Causa:** cada troca de linhas inverte o sinal do determinante — regra de álgebra linear que o código estava ignorando.

**Solução:** a variável `sinal`, multiplicada por `-1` a cada troca e aplicada no produto final.

### 4. Alinhamento da moldura com números de tamanhos diferentes

Com largura de célula fixa, uma matriz contendo `1` e `-15/4` ficava com a moldura torta.

**Solução:** calcular a largura em tempo de execução, medindo o maior valor já convertido para texto, e usar esse número na f-string aninhada `{v:^{cel}}`.

### 5. Matriz alterada in-place

`Operacoes.determinante(m)` escalona a matriz **recebida**, ou seja, destrói a original. Não causa bug visível porque a matriz é exibida antes do cálculo, mas quebraria se o programa calculasse determinante e inversa da mesma matriz em sequência.

**Solução:** copiar antes de escalonar, como já é feito em `rank()`:

```python
m = [linha[:] for linha in m]
```

O `[:]` copia cada linha interna. Um `m.copy()` simples **não** resolveria: ele criaria uma lista nova, mas com as **mesmas listas internas** dentro — alterar `m[0][0]` continuaria alterando a matriz original.

---

## Autor

**João Pedro Iop Beltrame** — Ciência da Computação, PUCPR

[![GitHub](https://img.shields.io/badge/GitHub-JoaoIopBeltrame-181717?style=flat-square&logo=github)](https://github.com/JoaoIopBeltrame)

Projeto desenvolvido para estudo de **álgebra linear**, **estruturas de dados** e **programação orientada a objetos**.
