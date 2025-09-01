# 5 Escreva uma função que permute os elementos de um vetor inteiro v[0..n-1] de modo que
#eles fiquem em ordem decrescente. Inspire-se no algoritmo Selectionsort.


def selection_sort_decrescente(v):
    n = len(v)

    # Percorre cada posição do vetor
    for i in range(n - 1):
        # Assume que o maior elemento está na posição i
        indice_maior = i

        # Busca o maior elemento no restante do vetor
        for j in range(i + 1, n):
            if v[j] > v[indice_maior]:
                indice_maior = j

        # Troca o maior elemento encontrado com o da posição atual
        v[i], v[indice_maior] = v[indice_maior], v[i]

# Exemplo de uso:
vetor = [5, 1, 9, 3, 7]
selection_sort_decrescente(vetor)
print("Vetor em ordem decrescente:", vetor)
