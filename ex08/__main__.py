import random
from utils import BinaryHeap, benchmark, print_table, generate_vector

# Algoritmo: percorre os nós internos de baixo para cima
# (do índice (n-2)//2 até 0) aplicando sift-down em cada um. Folhas são
# ignoradas, pois já satisfazem a propriedade trivialmente.
# Por que é O(n) e não O(n log n):
# A maioria dos nós fica nos níveis inferiores da árvore e percorre poucos
# níveis no sift-down. A soma das alturas de todos os nós de uma árvore
# completa com n elementos converge para O(n). Inserir um a um custaria
# O(n log n) porque cada inserção pode subir até a raiz.

random.seed(42)

def demo(description: str, array: list) -> None:
    print(f"{description}")
    print(f"inicial: {array}")
    heap, log = BinaryHeap.build_heap(array)
    for i, swapped, state in log:
        print(f"sift-down i={i}: trocas={swapped} -> {state}")
    if not log:
        print("nenhum sift-down necessário (array já é heap válida)")
    is_valid, _ = BinaryHeap.is_valid_heap(heap.data)
    print(f"final: {heap.data} válida={is_valid}")
    print()

def measure(pattern: str, n: int) -> tuple:
    heap, _ = BinaryHeap.build_heap(generate_vector(n, pattern), snapshots=False)
    is_valid, _ = BinaryHeap.is_valid_heap(heap.data)
    assert is_valid, f"build_heap gerou heap inválida ({pattern}, n={n})"
    return heap.steps, heap.swaps, heap.steps / n

demo("1 elemento", [42])
demo("2 elementos", [1, 5])
demo("Array arbitrário (7)", [5, 3, 8, 1, 7, 2, 9])
demo("Ordem crescente (7)", [1, 2, 3, 4, 5, 6, 7])
demo("Ordem decrescente (7)", [7, 6, 5, 4, 3, 2, 1])
demo("Array arbitrário (10)", [4, 10, 3, 5, 1, 8, 9, 2, 7, 6])
demo("Ordem crescente (15)", list(range(1, 16)))

# Tamanhos e padrões variados: os passos crescem na mesma proporção que n
# (n 10× maior, passos ~10× maiores), por isso passos/n fica estável,
# em torno de 3: O(n)
rows, headers = benchmark(
    axes={"padrão": ["sorted", "reverse", "random", "nearly_sorted"],
          "n": [10, 100, 1000, 10000]},
    measure=measure,
    metrics=["passos", "trocas", "passos/n"],
    samples=5,
)
print_table("build_heap por padrão de entrada (média de 5 execuções; todas as heaps válidas)",
            rows, headers, floatfmt=".2f")
