import random
from itertools import product
from tabulate import tabulate

class BinaryHeap:
    def __init__(self, data: list = None):
        self.__data = list(data) if data is not None else []
        self.__comparisons = 0
        self.__swaps = 0
    def reset_counters(self):
        self.__comparisons = 0
        self.__swaps = 0
    @property
    def data(self) -> list:
        return self.__data.copy()
    @property
    def comparisons(self) -> int:
        return self.__comparisons
    @property
    def swaps(self) -> int:
        return self.__swaps
    @property
    def steps(self) -> int:
        return self.__comparisons + self.__swaps
    def __parent(self, i: int) -> int:
        return (i - 1) // 2
    def __left(self, i: int) -> int:
        return 2 * i + 1
    def __right(self, i: int) -> int:
        return 2 * i + 2
    def __sift_up(self, i: int) -> list:
        # Sobe o elemento da posição i enquanto ele for maior que o pai.
        swapped = []
        while i > 0:
            parent = self.__parent(i)
            self.__comparisons += 1
            if self.__data[i] > self.__data[parent]:
                swapped.append((i, parent))
                self.__data[i], self.__data[parent] = self.__data[parent], self.__data[i]
                self.__swaps += 1
                i = parent
            else:
                break
        return swapped
    def __sift_down(self, i: int) -> list:
        # Desce o elemento da posição i trocando com o maior filho até
        # nenhum filho ser maior que ele.
        swapped = []
        n = len(self.__data)
        while True:
            left = self.__left(i)
            right = self.__right(i)
            maximum = i
            if left < n:
                self.__comparisons += 1
                if self.__data[left] > self.__data[maximum]:
                    maximum = left
            if right < n:
                self.__comparisons += 1
                if self.__data[right] > self.__data[maximum]:
                    maximum = right
            if maximum == i:
                break
            swapped.append((i, maximum))
            self.__data[i], self.__data[maximum] = self.__data[maximum], self.__data[i]
            self.__swaps += 1
            i = maximum
        return swapped
    def insert(self, value) -> list:
        self.__data.append(value)
        return self.__sift_up(len(self.__data) - 1)
    def extract_max(self) -> tuple:
        if not self.__data:
            return None, []
        if len(self.__data) == 1:
            return self.__data.pop(), []
        maximum = self.__data[0]
        self.__data[0] = self.__data.pop()
        return maximum, self.__sift_down(0)
    def contains(self, value) -> tuple:
        visited = []
        for i, v in enumerate(self.__data):
            visited.append(i)
            self.__comparisons += 1
            if v == value:
                return True, visited
        return False, visited
    def delete(self, value) -> tuple:
        index = -1
        for i, v in enumerate(self.__data):
            self.__comparisons += 1
            if v == value:
                index = i
                break
        if index == -1:
            return False, []
        if index == len(self.__data) - 1:
            self.__data.pop()
            return True, []
        removed_value = self.__data[index]
        self.__data[index] = self.__data.pop()
        replacement = self.__data[index]
        self.__comparisons += 1  # comparação entre substituto e removido
        if replacement > removed_value:
            return True, self.__sift_up(index)
        return True, self.__sift_down(index)
    @classmethod
    def build_heap(cls, array: list, snapshots: bool = True) -> tuple["BinaryHeap", list]:
        # snapshots guarda o array após cada sift-down; cada cópia custa O(n).
        heap = cls(array)
        n = len(heap.__data)
        log = []
        for i in range((n - 2) // 2, -1, -1):
            swapped = heap.__sift_down(i)
            log.append((i, swapped, list(heap.__data) if snapshots else None))
        return heap, log
    @classmethod
    def is_valid_heap(cls, array: list) -> tuple:
        heap = cls(array)
        n = len(heap.__data)
        for i in range(n):
            left = heap.__left(i)
            right = heap.__right(i)
            if left < n and heap.__data[left] > heap.__data[i]:
                return False, (i, left)
            if right < n and heap.__data[right] > heap.__data[i]:
                return False, (i, right)
        return True, None
def benchmark(axes, measure, metrics, samples=1):
    """
    Executa `measure` sobre o produto cartesiano de `axes` e devolve
    (rows, headers) prontos para o print_table.

    axes:    dict {nome_da_coluna: [valores]}. As colunas de identificação da
             tabela, na ordem em que devem aparecer. O último eixo é o que
             varia mais rápido, como em laços aninhados.
    measure: recebe os valores de uma combinação, na ordem de `axes`, e devolve
             uma sequência de números — as métricas daquela linha.
    metrics: nomes das colunas devolvidas por `measure`.
    samples: repetições por combinação. Cada métrica sai pela média; com
             entradas determinísticas a média é o próprio valor.
    """
    rows = []
    for combo in product(*axes.values()):
        _samples = [measure(*combo) for _ in range(samples)]
        medias = []
        for i in range(len(metrics)):
            soma = sum(amostra[i] for amostra in _samples)
            medias.append(soma if samples == 1 else soma / samples)
        rows.append(list(combo) + medias)
    return rows, list(axes) + list(metrics)
def print_table(title, rows, headers, floatfmt=".4f"):
    print(f"{title}")
    print(tabulate(
        rows,
        headers=headers,
        tablefmt='github',
        floatfmt=floatfmt    
    ))
def generate_nearly_sorted(n):
    arr = list(range(n))
    swaps = max(1, n // 20)
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
def generate_vector(n, pattern):
    patterns = {
        "sorted": lambda: list(range(n)),
        "reverse": lambda: list(range(n - 1, -1, -1)),
        "random": lambda: [random.randint(0, n) for _ in range(n)],
        "nearly_sorted": lambda: generate_nearly_sorted(n)
    }
    return patterns[pattern]()
