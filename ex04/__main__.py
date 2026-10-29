from utils import BinaryHeap

def drain_heap(values: list):
    heap = BinaryHeap()
    for v in values:
        heap.insert(v)
    print(f"Heap inicial: {heap.data}")
    step = 1
    while True:
        maximum, swapped = heap.extract_max()
        if maximum is None:
            break
        print(f"\nPasso {step}: extract_max() -> {maximum}")
        print(f"trocas (sift-down): {swapped}")
        print(f"array resultante: {heap.data}")
        step += 1

# Complexidade de extract_max(): O(log n)
# A raiz (máximo) é removida e substituída pela última folha.
# O sift-down desce comparando o nó com seus dois filhos e trocando
# com o maior deles, repetindo até não haver filho maior.
# A árvore completa tem altura h = log2 n, portanto o sift-down
# executa no máximo log2 n trocas, ou seja, O(log n) por chamada.
# Remoções sucessivas até esvaziar a heap custam:
# log(n) + log(n-1) + ... + log(1) = O(n log n) no total.
drain_heap([40, 20, 35, 10, 15, 30, 25])
