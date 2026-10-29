from utils import BinaryHeap

def search_heap(values):
    heap, _ = BinaryHeap.build_heap(values)
    print(f"Array: {heap.data}")
    for target in [35, 20, 99]:
        found, visited = heap.contains(target)
        status = "encontrado" if found else "não encontrado"
        print(f"\ncontains({target}): {status}")
        print(f"índices visitados: {visited}")
        print(f"comparações: {len(visited)}/{len(heap.data)}")

# Algoritmo: varredura linear do array interno.
# A propriedade de heap (pai >= filhos) não impõe ordem entre elementos
# de subárvores diferentes nem entre irmãos, portanto não há como descartar
# regiões do array sem verificá-las. A busca precisa percorrer todos os
# elementos no pior caso.
# Complexidade: O(n)
# - Melhor caso O(1): valor encontrado na raiz (índice 0).
# - Pior caso O(n): valor está na última posição ou não existe na heap.
# Por que heap não é adequada para buscas frequentes:
# Uma BST balanceada garante busca em O(log n) explorando
# a ordenação total entre nós. A heap mantém apenas a relação pai >= filho,
# sem ordenação entre irmãos, não há como decidir em qual subárvore buscar.
# Aplicações que misturam extração de máximo com buscas frequentes devem
# combinar heap com uma tabela hash (O(1) por busca) ou trocar para outra
# estrutura.
search_heap([50, 30, 40, 10, 20, 35, 25])
