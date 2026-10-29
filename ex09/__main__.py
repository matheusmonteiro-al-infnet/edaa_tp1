import math
import random
from utils import BinaryHeap, benchmark, print_table, generate_vector

# Inserção incremental: O(n log n)
# Cada insert() faz sift-up, que no pior caso percorre log n níveis.
# Para n elementos: n × O(log n) = O(n log n).
# Os primeiros elementos inseridos ocupam posições próximas à raiz e
# podem ter que subir muitos níveis conforme a heap cresce.
# build_heap: O(n)
# Aplica sift-down nos nós internos de baixo para cima.
# A maioria dos nós fica nos níveis inferiores e faz poucas trocas.
# A soma das alturas de todos os nós converge para O(n).
# Métrica: passos = comparações entre elementos + trocas (contador da BinaryHeap).

random.seed(42)

def compare(pattern: str, n: int) -> tuple:
    array = generate_vector(n, pattern)

    heap_insert = BinaryHeap()
    for v in array:
        heap_insert.insert(v)

    heap_build, _ = BinaryHeap.build_heap(array, snapshots=False)

    assert sorted(heap_insert.data) == sorted(heap_build.data)

    return (heap_insert.steps, heap_build.steps,
            heap_insert.swaps, heap_build.swaps,
            heap_insert.steps / (n * math.log2(n)),
            heap_build.steps / n)

rows, headers = benchmark(
    axes={"padrão": ["sorted", "reverse", "random", "nearly_sorted"],
          "n": [10, 100, 1000, 10000]},
    measure=compare,
    metrics=["insert (passos)", "build (passos)",
             "insert (trocas)", "build (trocas)",
             "insert/(n·log2n)", "build/n"],
    samples=5,
)
print_table("Inserção incremental vs build_heap (média de 5 execuções)",
            rows, headers, floatfmt=".2f")

# Discussão dos resultados:
# - sorted (pior caso da inserção): cada novo elemento sobe até a raiz.
#   insert/(n·log2n) cresce de 1.14 para 1.71 e tende a uma constante (~2,
#   uma comparação + uma troca por nível), confirmando O(n log n). Com
#   n=10000, a inserção faz ~7.6x mais passos que o build_heap.
# - build/n fica sempre entre 0.9 e 3.0, para qualquer padrão e tamanho:
#   o custo cresce linearmente com n, confirmando O(n).
# - reverse: o array já é uma heap de máximo, então nenhuma troca acontece
#   e as duas abordagens custam n-1 comparações (O(n), melhor caso).
# - random: a inserção fica bem abaixo do pior caso (insert/(n·log2n)
#   diminui com n), pois um elemento aleatório sobe em média poucos níveis.
#   Mesmo assim o build_heap faz menos passos em todos os tamanhos.
# Conclusão: build_heap nunca é pior que a inserção incremental e, no pior
# caso, a diferença é assintótica: O(n) contra O(n log n).
