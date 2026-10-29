import math
import random
from utils import BinaryHeap, benchmark, print_table, generate_vector

def run_sequence(name: str, values: list) -> None:
    heap = BinaryHeap()
    total = 0
    print(f"\n{name}: {values}")
    for value in values:
        swapped = heap.insert(value)
        total += len(swapped)
        print(f"insert({value:2d}) -> trocas: {swapped}")
    print(f"total de trocas: {total}")

def measure(pattern: str, n: int) -> tuple:
    heap = BinaryHeap()
    total = 0
    for value in generate_vector(n, pattern):
        total += len(heap.insert(value))
    return total, total / n, math.log2(n)

random.seed(42)

# Pior caso: sequência crescente força sift-up máximo em cada inserção.
# O novo elemento é sempre o maior, sobe até a raiz percorrendo todos os
# níveis. Para n elementos, cada inserção custa O(log n), totalizando
# O(n log n) trocas na sequência inteira.
# Melhor caso: sequência decrescente, nenhum elemento precisa subir,
# custo O(1) por inserção, O(n) no total.
run_sequence("Crescente", [10, 20, 30, 40, 50])
run_sequence("Decrescente", [50, 40, 30, 20, 10])
run_sequence("Aleatória", [30, 10, 50, 20, 40])

# Em escala: no padrão sorted, trocas/inserção cresce com log2 n (pior caso);
# em reverse fica em 0 (melhor caso); random e nearly_sorted ficam entre os dois.
rows, headers = benchmark(
    axes={"padrão": ["sorted", "reverse", "random", "nearly_sorted"],
          "n": [10, 100, 1000, 10000]},
    measure=measure,
    metrics=["trocas", "trocas/inserção", "log2 n (altura)"],
    samples=5,
)
print_table("Trocas na inserção por padrão de entrada (média de 5 execuções)",
            rows, headers, floatfmt=".2f")
