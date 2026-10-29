from utils import BinaryHeap

# Algoritmo: percorre todos os índices do array verificando, para cada nó i,
# se o filho esquerdo (2i+1) e o filho direito (2i+2) - quando existem -
# são menores ou iguais ao pai. A primeira violação encontrada encerra a
# verificação imediatamente e retorna False.
# Justificativa: como a heap é representada nível a nível no array, iterar
# linearmente cobre todas as relações pai-filho exatamente uma vez. Não é
# necessário percorrer subárvores recursivamente, os índices já fazem isso.
# Complexidade: O(n) no pior caso (array válido, todas as relações verificadas).
# Melhor caso O(1): violação na primeira relação verificada (índices 0 e 1).

def check(description: str, array: list) -> None:
    is_valid, violation = BinaryHeap.is_valid_heap(array)
    status = "válida" if is_valid else "inválida"
    print(f"{description}")
    print(f"array: {array}")
    if violation:
        parent, child = violation
        print(f"resultado: {status} -> array[{child}]={array[child]} > array[{parent}]={array[parent]}")
    else:
        print(f"resultado: {status}")
    print()

heap, _ = BinaryHeap.build_heap([50, 30, 40, 10, 20, 35, 25])

# Arrays válidos
check("Heap válida - construída pela classe", heap.data)
check("Heap válida - um elemento", [42])
check("Heap válida - array vazio", [])

# Arrays inválidos
check("Inválida - violação na raiz", [40, 50, 30])
check("Inválida - violação na subárvore esquerda", [50, 30, 40, 10, 45, 35, 25])
check("Inválida - violação na subárvore direita", [50, 30, 20, 10, 25, 15, 30])
