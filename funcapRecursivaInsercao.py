#3.– Escreva uma versão recursiva do algoritmo de ordenação por inserção.

def insertion_sort_recursivo(v, n=None):
    # Na primeira chamada, define n como o tamanho do vetor
    if n is None:
        n = len(v)

    # Caso base: vetor com 1 elemento já está ordenado
    if n <= 1:
        return

    # Ordena os primeiros n-1 elementos de forma recursiva
    insertion_sort_recursivo(v, n - 1)

    # Insere o último elemento na posição correta
    ultimo = v[n - 1]
    j = n - 2

    # Move elementos maiores que "ultimo" uma posição à frente
    while j >= 0 and v[j] > ultimo:
        v[j + 1] = v[j]
        j -= 1

    v[j + 1] = ultimo

# Exemplo de uso:
vetor = [5, 2, 9, 1, 5, 6]
insertion_sort_recursivo(vetor)
print("Vetor ordenado:", vetor)
