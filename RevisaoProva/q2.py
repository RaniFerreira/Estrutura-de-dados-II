def selection_descrescente(lista):
    n = len(lista)
    
    for i in range(n-1):
        menor = i
        for j in range(i+1,n):
            if lista[j] > lista[menor]:
                menor = j
        
        lista[i],lista[menor] = lista[menor], lista[i]
    return lista


# Programa principal
vetor = [5, 2, 9, 1, 7, 3]
print("Vetor original:", vetor)

resultado = selection_descrescente(vetor)
print("Vetor em ordem decrescente:", resultado)