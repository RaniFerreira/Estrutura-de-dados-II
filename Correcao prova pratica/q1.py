# Função Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Função para inserir um número mantendo a ordem crescente
def inserir_ordenado(array, x):
    array.append(x)       # adiciona o novo elemento no final
    bubble_sort(array)    # reordena a lista
    return array

# Testes
lista = []
print(inserir_ordenado(lista, 5))      # inserindo em lista vazia
print(inserir_ordenado(lista, 2))      # inserindo menor que todos
print(inserir_ordenado(lista, 10))     # inserindo maior que todos
print(inserir_ordenado(lista, 5))      # inserindo número repetido