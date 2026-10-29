import math
import time
from utils import BinaryHeap, benchmark, print_table, generate_vector

# Métrica: passos = comparações entre elementos + trocas.
# Tempo: time.perf_counter() em volta apenas da operação medida (a montagem
# da heap de entrada fica fora da medição).
# Pior caso: array em ordem crescente.
# insert n vezes: cada elemento sobe até a raiz -> O(n log n)
# build_heap: sift-down de baixo para cima -> O(n)
# extract_max n vezes: cada extração faz sift-down completo -> O(n log n)
# contains: varredura linear, elemento ausente -> O(n)
# delete: busca linear até o último índice -> O(n)

def build_by_insertion(array: list) -> BinaryHeap:
    heap = BinaryHeap()
    for v in array:
        heap.insert(v)
    heap.reset_counters()
    return heap

def op_insert(array):
    heap = BinaryHeap()
    start = time.perf_counter()
    for v in array:
        heap.insert(v)
    return heap.steps, time.perf_counter() - start

def op_build(array):
    start = time.perf_counter()
    heap, _ = BinaryHeap.build_heap(array, snapshots=False)
    return heap.steps, time.perf_counter() - start

def op_extract_max(array):
    heap, _ = BinaryHeap.build_heap(array, snapshots=False)
    heap.reset_counters()
    start = time.perf_counter()
    for _ in range(len(array)):
        heap.extract_max()
    return heap.steps, time.perf_counter() - start

def op_contains(array):
    heap = build_by_insertion(array)
    start = time.perf_counter()
    heap.contains(-1)  # pior caso: elemento ausente, percorre tudo
    return heap.steps, time.perf_counter() - start

def op_delete(array):
    heap = build_by_insertion(array)
    target = heap.data[-1]  # pior caso: valor no último índice do array interno
    start = time.perf_counter()
    heap.delete(target)
    return heap.steps, time.perf_counter() - start

OPERATIONS = {
    "insert": (op_insert, "n·log2n", lambda n: n * math.log2(n)),
    "build_heap": (op_build, "n", lambda n: n),
    "extract_max": (op_extract_max, "n·log2n", lambda n: n * math.log2(n)),
    "contains": (op_contains, "n", lambda n: n),
    "delete": (op_delete, "n", lambda n: n),
}

def measure(operation: str, n: int) -> tuple:
    function, _, reference = OPERATIONS[operation]
    steps, seconds = function(generate_vector(n, "sorted"))
    ref = reference(n)
    return steps, ref, steps / ref, seconds * 1000

rows, headers = benchmark(
    axes={"operação": list(OPERATIONS), "n": [100, 500, 1000, 5000, 10000]},
    measure=measure,
    metrics=["passos", "referência", "passos/ref", "tempo (ms)"],
    samples=5,
)
for row in rows:
    row.insert(2, OPERATIONS[row[0]][1])  # coluna com a fórmula de referência
headers.insert(2, "teoria")
print_table("Complexidade empírica (entrada crescente, média de 5 execuções)",
            rows, headers, floatfmt=".3f")

# Comparação com a análise teórica:
# - Se a operação tem a complexidade prevista, passos/ref se estabiliza em
#   uma constante à medida que n cresce.
# - insert: passos/ref sobe de 1.44 para 1.71 e desacelera. A constante tende
#   a 2 porque cada nível percorrido custa uma comparação + uma troca. O(n log n).
# - build_heap: passos/ref converge para 3.0 (n=100 -> 2.86, n=10000 -> 3.00).
#   Custo linear, O(n), mesmo no pior caso.
# - extract_max (n extrações): passos/ref sobe de 2.01 para 2.53 e desacelera,
#   pois cada nível do sift-down custa até duas comparações + uma troca. O(n log n).
# - contains e delete: passos/ref = 1.000 exato, pois o pior caso visita
#   todos os n elementos. O(n).
# - Tempo: Tempo: acompanha a tendência dos passos, mas varia entre execuções e máquinas (ruído do sistema).
# Por isso os passos, que são determinísticos, são a métrica principal
