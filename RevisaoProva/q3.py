def selection_sort_k_trocas(lista, n):
    n = len(lista)
    trocas = 0  
    
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]
        trocas += 1

        if trocas == n:
            break

    return lista


# Programa principal
vetor = [64, 25, 12, 22, 11]
k = 2
print("Vetor original:", vetor)

resultado = selection_sort_k_trocas(vetor, k)
print(f"Vetor após {k} trocas do Selection Sort:", resultado)