def dividir_iterativo(a, i, j):
    pivo = a[(i + j) // 2]
    esq = i
    dir = j
    while True:
        while a[esq] > pivo:
            esq += 1
        while a[dir] < pivo:
            dir -= 1
        if esq >= dir:
            return dir
        a[esq], a[dir] = a[dir], a[esq]
        esq += 1
        dir -= 1


def quicksort_iterativo(a, ini, fim):
    pilha = [(ini, fim)]
    while pilha:
        i, j = pilha.pop()
        if i < j:
            k = dividir_iterativo(a, i, j)
            pilha.append((i, k))
            pilha.append((k + 1, j))


nums = [8, 3, 1, 7, 0, 10, 2]
quicksort_iterativo(nums, 0, len(nums) - 1)
print("Vetor ordenado (decrescente):", nums)
