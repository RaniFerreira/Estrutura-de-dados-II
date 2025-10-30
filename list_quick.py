import time

# =========================================================
# QUESTÃO 1 – Quick Sort Recursivo (ordem DECRESCENTE)
# =========================================================
def quicksort_recursivo(array, inicio, fim):
    if inicio < fim:
        pivo_index = partition_decrescente(array, inicio, fim)
        quicksort_recursivo(array, inicio, pivo_index - 1)
        quicksort_recursivo(array, pivo_index + 1, fim)

def partition_decrescente(array, inicio, fim):
    pivo = array[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if array[j] > pivo:  # comparação invertida para ordem decrescente
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[fim] = array[fim], array[i + 1]
    return i + 1


# =========================================================
# QUESTÃO 2 – Quick Sort Iterativo e Comparação de Desempenho
# =========================================================
def quicksort_iterativo(array):
    pilha = [(0, len(array) - 1)]

    while pilha:
        inicio, fim = pilha.pop()
        if inicio < fim:
            p = partition_decrescente(array, inicio, fim)
            pilha.append((inicio, p - 1))
            pilha.append((p + 1, fim))


def comparar_tempos():
    import random
    tamanhos = [10, 100, 1000, 5000]
    print("TAMANHO | TEMPO RECURSIVO (s) | TEMPO ITERATIVO (s)")
    print("-----------------------------------------------")

    for n in tamanhos:
        vetor1 = [random.randint(0, 10000) for _ in range(n)]
        vetor2 = vetor1.copy()

        inicio = time.time()
        quicksort_recursivo(vetor1, 0, len(vetor1) - 1)
        tempo_rec = time.time() - inicio

        inicio = time.time()
        quicksort_iterativo(vetor2)
        tempo_it = time.time() - inicio

        print(f"{n:7d} | {tempo_rec:19.6f} | {tempo_it:19.6f}")

    print("\nDiscussão:")
    print("- A versão recursiva é mais simples e fácil de implementar.")
    print("- A versão iterativa evita o custo das chamadas recursivas, sendo mais eficiente em casos grandes.")
    print("- Porém, a recursiva é mais legível e didática.")
    print("- Ambas possuem complexidade O(n log n) em média.")


# =========================================================
# QUESTÃO 3 – Análise de Erros na Função qsrt
# =========================================================
def qsrt(array, left, right):
    j = partition_decrescente(array, left, right)
    if (left < j - 1):
        qsrt(array, left, j - 1)
    if (j + 1 < right):
        qsrt(array, j + 1, right)

"""
Análise:
- O algoritmo pode falhar para subvetores pequenos (1 ou 2 elementos).
- Isso acontece porque a condição de parada depende de (left < j - 1) e (j + 1 < right),
  o que pode ignorar partes do vetor com 1 elemento.
- Também pode gerar chamadas com índices fora de faixa.
Correção:
- Deve haver uma verificação principal if left < right antes de chamar partition.
"""

def qsrt_corrigido(array, left, right):
    if left < right:
        j = partition_decrescente(array, left, right)
        qsrt_corrigido(array, left, j - 1)
        qsrt_corrigido(array, j + 1, right)


# =========================================================
# QUESTÃO 4 – Crítica à Função sep
# =========================================================
"""
A função abaixo está incorreta:

def sep(array, left, right):
    j = right
    for i in range(right - 1, left - 1, -1):
        if array[i] > array[right]:
            array[i], array[right] = array[right], array[i]
            j = i
    return j

Problemas:
1. O pivô (array[right]) muda de posição a cada troca, o que quebra a lógica de separação.
2. O índice 'j' não separa os elementos menores/maiores corretamente.
3. Isso pode gerar uma ordenação incorreta e até loops infinitos.

Solução Correta:
Usar o método clássico de partição de Lomuto ou Hoare.
"""

def partition_correta(array, left, right):
    pivo = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


# =========================================================
# QUESTÃO 5 – Rastreamento das Chamadas do Quick Sort
# =========================================================
def quicksort_rastreamento(array, left, right):
    print(f"quicksort(array, {left}, {right})")
    if left < right:
        p = partition_correta(array, left, right)
        quicksort_rastreamento(array, left, p - 1)
        quicksort_rastreamento(array, p + 1, right)


def teste_rastreamento():
    print("=== Rastreamento 1 ===")
    array1 = [77, 55, 33, 99]
    quicksort_rastreamento(array1, 0, len(array1) - 1)

    print("\n=== Rastreamento 2 ===")
    array2 = [55, 44, 22, 11, 66, 33]
    quicksort_rastreamento(array2, 0, len(array2) - 1)


# =========================================================
# EXECUÇÃO PRINCIPAL (para testes)
# =========================================================
if __name__ == "__main__":
    print("===== QUESTÃO 1 e 2: Quick Sort Decrescente =====")
    comparar_tempos()

    print("\n===== QUESTÃO 3: Análise =====")
    print("Função qsrt pode falhar em subvetores pequenos. Correção aplicada com verificação (left < right).")

    print("\n===== QUESTÃO 4: Crítica =====")
    print("A função sep move o pivô incorretamente e quebra a lógica da partição. Corrigida com método de Lomuto.")

    print("\n===== QUESTÃO 5: Rastreamento =====")
    teste_rastreamento()