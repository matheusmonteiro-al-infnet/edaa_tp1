from utils import BinaryHeap

def delete_and_show(heap: BinaryHeap, value: int) -> None:
    print(f"delete({value})")
    print(f"antes: {heap.data}")
    found, swapped = heap.delete(value)
    if not found:
        print(f"valor {value} não encontrado na heap")
        return
    print(f"trocas: {swapped}")
    print(f"depois: {heap.data}")

# Complexidade de delete(value): O(n)
# O custo dominante é a busca linear pelo valor (O(n)), pois a propriedade
# de heap não impõe ordem entre irmãos e não permite descartar subárvores.
# Após encontrar o elemento, a reorganização (sift-up ou sift-down) custa
# O(log n). O total é O(n) + O(log n) = O(n).
# Impacto no desempenho global:
# delete() torna a heap ineficiente para remoções arbitrárias frequentes.
# Se buscas e deleções por valor forem comuns, a estrutura correta é uma
# BST balanceada (O(log n) para busca e remoção) ou heap + tabela hash
# de posições para O(log n) por deleção sem a busca linear.

VALUES = [100, 80, 90, 60, 70, 85, 88]

# Caso 1: valor existente, substituto (88) maior que o removido (70) -> sift-up
h1, _ = BinaryHeap.build_heap(VALUES)
print("Caso 1 - valor existente (sift-up):")
delete_and_show(h1, 70)

# Caso 2: valor existente, substituto (88) menor que o removido (100) -> sift-down
h2, _ = BinaryHeap.build_heap(VALUES)
print("\nCaso 2 - valor existente (sift-down):")
delete_and_show(h2, 100)

# Caso 3: valor inexistente
h3, _ = BinaryHeap.build_heap(VALUES)
print("\nCaso 3 - valor inexistente:")
delete_and_show(h3, 999)
