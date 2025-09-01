# 4 Escreva uma versão recursiva do algoritmo de ordenação por seleção.

def selection_sort_recursivo(v, inicio=0):
    n = len(v)

    # Caso base: quando chegamos no último elemento
    if inicio >= n - 1:
        return

    # Encontra o índice do menor elemento a partir de 'inicio'
    indice_minimo = inicio
    for i in range(inicio + 1, n):
        if v[i] < v[indice_minimo]:
            indice_minimo = i

    # Troca o menor elemento encontrado com o elemento da posição 'inicio'
    v[inicio], v[indice_minimo] = v[indice_minimo], v[inicio]

    # Chamada recursiva para o restante do vetor
    selection_sort_recursivo(v, inicio + 1)

# Exemplo de uso:
vetor = [64, 25, 12, 22, 11]
selection_sort_recursivo(vetor)
print("Vetor ordenado:", vetor)
