# TP1 – Heap Binária em Python

Implementação de uma heap binária de máximo do zero, com orientação a objetos, e exercícios que demonstram e medem cada operação. A parte teórica (exercícios 1, 2 e 12) e a análise de cada exercício estão no documento do trabalho.

## Estrutura

```
tp1/
├── utils.py            # classe BinaryHeap e funções de apoio aos testes
├── requirements.txt    # dependências (tabulate)
├── ex03/               # insert
├── ex04/               # extract_max
├── ex05/               # contains
├── ex06/               # delete
├── ex07/               # is_valid_heap
├── ex08/               # build_heap
├── ex09/               # build_heap × inserção incremental
├── ex10/               # heap sort parcial (k maiores)
└── ex11/               # análise de complexidade empírica
```

Cada pasta `exNN/` contém:

- `__init__.py` – torna a pasta um pacote Python;
- `__main__.py` – código do exercício;
- `execucao.txt` – saída registrada da execução.

## Como executar

Requisito: Python 3.9 ou superior (desenvolvido com o 3.12). Todos os comandos são rodados na raiz do projeto.

### 1. Criar o ambiente virtual e instalar as dependências

Windows (PowerShell ou Prompt de Comando):

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Linux e macOS:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Executar um exercício

Com o ambiente ativado, cada exercício roda como módulo, pelo nome da pasta:

```
python -m ex03
```

### 3. Gravar a saída no `execucao.txt`

Windows:

```
python -X utf8 -m ex03 > ex03\execucao.txt
```

Linux e macOS:

```
python -X utf8 -m ex03 > ex03/execucao.txt
```

O `-X utf8` garante que os acentos sejam gravados corretamente no arquivo.

Os exercícios com arrays aleatórios usam `random.seed(42)`, então os resultados se repetem a cada execução. Só os tempos (ms) do `ex11` variam.
