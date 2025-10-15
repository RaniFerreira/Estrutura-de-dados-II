import random
import time

# ------------------------------------------------------------
# Questão 1 – Merge Sort Recursivo (ordem decrescente)
# ------------------------------------------------------------

def combinar(lista, ini, meio, fim):
    parte_esq = lista[ini:meio + 1]
    parte_dir = lista[meio + 1:fim + 1]
    p = q = 0
    r = ini
    while p < len(parte_esq) and q < len(parte_dir):
        if parte_esq[p] >= parte_dir[q]:
            lista[r] = parte_esq[p]
            p += 1
        else:
            lista[r] = parte_dir[q]
            q += 1
        r += 1
    while p < len(parte_esq):
        lista[r] = parte_esq[p]
        p += 1
        r += 1
    while q < len(parte_dir):
        lista[r] = parte_dir[q]
        q += 1
        r += 1

def merge_sort_dec(lista, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort_dec(lista, ini, meio)
        merge_sort_dec(lista, meio + 1, fim)
        combinar(lista, ini, meio, fim)

# ------------------------------------------------------------
# Questão 2 – Testes experimentais
# ------------------------------------------------------------

def merge_sort_cres(vet):
    if len(vet) > 1:
        meio = len(vet) // 2
        lado_esq = vet[:meio]
        lado_dir = vet[meio:]
        merge_sort_cres(lado_esq)
        merge_sort_cres(lado_dir)
        i = j = k = 0
        while i < len(lado_esq) and j < len(lado_dir):
            if lado_esq[i] < lado_dir[j]:
                vet[k] = lado_esq[i]
                i += 1
            else:
                vet[k] = lado_dir[j]
                j += 1
            k += 1
        while i < len(lado_esq):
            vet[k] = lado_esq[i]
            i += 1
            k += 1
        while j < len(lado_dir):
            vet[k] = lado_dir[j]
            j += 1
            k += 1

def confere_ordenacao(seq):
    return all(seq[x] <= seq[x + 1] for x in range(len(seq) - 1))

def exec_testes():
    for n in [10, 100, 1000]:
        arr = [random.randint(0, 1000) for _ in range(n)]
        merge_sort_cres(arr)
        print(f"Tamanho {n} → Ordenado? {confere_ordenacao(arr)}")

# ------------------------------------------------------------
# Questão 3 – Variações no cálculo do meio
# ------------------------------------------------------------

def merge_sort_alt(lista, ini, fim, tipo=0):
    if ini < fim:
        if tipo == 0:
            meio = (ini + fim) // 2
        elif tipo == 1:
            meio = (ini + fim - 1) // 2
        else:
            meio = (ini + fim + 1) // 2
        merge_sort_alt(lista, ini, meio, tipo)
        merge_sort_alt(lista, meio + 1, fim, tipo)
        combinar(lista, ini, meio, fim)

def testar_alternativas():
    dados = [9, 4, 7, 1, 3]
    for modo, nome in enumerate(["normal", "-1", "+1"]):
        copia = dados.copy()
        merge_sort_alt(copia, 0, len(copia) - 1, modo)
        print(f"Modo {nome}: {copia}")

# ------------------------------------------------------------
# Questão 4 – Versão iterativa x recursiva
# ------------------------------------------------------------

def merge_sort_iter(v):
    tam = len(v)
    passo = 1
    while passo < tam:
        for ini in range(0, tam, 2 * passo):
            meio = min(ini + passo - 1, tam - 1)
            fim = min(ini + 2 * passo - 1, tam - 1)
            combinar(v, ini, meio, fim)
        passo *= 2

def medir_tempos():
    for tam in [1000, 5000, 10000]:
        vet1 = [random.randint(0, 10000) for _ in range(tam)]
        vet2 = vet1.copy()
        inicio = time.time()
        merge_sort_cres(vet1)
        t1 = time.time() - inicio
        inicio = time.time()
        merge_sort_iter(vet2)
        t2 = time.time() - inicio
        print(f"Tamanho {tam:>6} → Recursivo: {t1:.5f}s | Iterativo: {t2:.5f}s")

# ------------------------------------------------------------
# Questão 5 – Merge Sort para listas encadeadas
# ------------------------------------------------------------

class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

def separar_lista(cabeca):
    if cabeca is None or cabeca.prox is None:
        return cabeca, None
    lento, rapido = cabeca, cabeca.prox
    while rapido and rapido.prox:
        lento = lento.prox
        rapido = rapido.prox.prox
    meio = lento.prox
    lento.prox = None
    return cabeca, meio

def unir_listas(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.dado <= b.dado:
        res = a
        res.prox = unir_listas(a.prox, b)
    else:
        res = b
        res.prox = unir_listas(a, b.prox)
    return res

def merge_sort_encadeado(cabeca):
    if cabeca is None or cabeca.prox is None:
        return cabeca
    esq, dir = separar_lista(cabeca)
    esq = merge_sort_encadeado(esq)
    dir = merge_sort_encadeado(dir)
    return unir_listas(esq, dir)

def exibir_lista(cabeca):
    atual = cabeca
    while atual:
        print(atual.dado, end=" -> ")
        atual = atual.prox
    print("None")

def teste_lista():
    cabeca = No(5)
    cabeca.prox = No(1)
    cabeca.prox.prox = No(4)
    cabeca.prox.prox.prox = No(2)
    cabeca.prox.prox.prox.prox = No(3)
    print("Lista original:")
    exibir_lista(cabeca)
    cabeca = merge_sort_encadeado(cabeca)
    print("Lista ordenada:")
    exibir_lista(cabeca)

# ------------------------------------------------------------
# Execução principal
# ------------------------------------------------------------
if __name__ == "__main__":
    print("\n--- Questão 1 e 2 ---")
    exec_testes()
    print("\n--- Questão 3 ---")
    testar_alternativas()
    print("\n--- Questão 4 ---")
    medir_tempos()
    print("\n--- Questão 5 ---")
    teste_lista()
