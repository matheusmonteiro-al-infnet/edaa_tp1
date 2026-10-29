from utils import BinaryHeap

# Algoritmo: build_heap O(n) + k extrações O(k log n) = O(n + k log n).
# Vantagem sobre ordenação completa O(n log n): quando k < n, evita ordenar
# elementos que nunca serão usados. Só os k maiores saem da heap; os n - k
# restantes continuam nela sem nenhuma ordenação entre si.
def k_largest(array: list, k: int) -> tuple:
    # Devolve (k maiores em ordem decrescente, o que restou na heap).
    if not 0 <= k <= len(array):
        raise ValueError(f"k deve estar entre 0 e {len(array)}, recebido {k}")
    heap, _ = BinaryHeap.build_heap(array, snapshots=False)
    result = []
    for _ in range(k):
        maximum, _ = heap.extract_max()
        result.append(maximum)
    return result, heap.data

def demo(array: list, k: int) -> None:
    print(f"array (n={len(array)}): {array}")
    try:
        result, remaining = k_largest(array, k)
        print(f"k={k} maiores: {result}")
        print(f"restante (sem ordem): {remaining}\n")
    except ValueError as error:
        print(f"k={k} recusado: {error}\n")

small_array = [5, 3, 8, 1, 7, 2, 9, 4, 6]
large_array = list(range(1, 21))

# k < n: seleção parcial, o array não é ordenado por completo
demo(small_array, 1)
demo(small_array, 3)
demo(small_array, 5)
demo(large_array, 5)
demo(large_array, 10)

# Caso-limite k = n: todos os elementos são extraídos, o que equivale a um
# heap sort completo, O(n log n). É o maior k válido, e não o uso pretendido
# da seleção parcial.
demo(small_array, len(small_array))

# k inválido: recusado com ValueError
demo(small_array, len(small_array) + 1)
demo(small_array, -1)
