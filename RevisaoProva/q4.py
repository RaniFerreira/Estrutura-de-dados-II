def insertion_sort_contando(vetor):
    n = len(vetor)
    copias = 0  
    
    for i in range(1, n):
        chave = vetor[i]
        j = i - 1
        
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]  # cópia
            copias += 1
            j -= 1
        
        vetor[j + 1] = chave  
    
    return vetor, copias


# Programa principal
vetor = [72, 12, 62, 69, 27, 67, 41, 56, 33, 74]
ordenado, total_copias = insertion_sort_contando(vetor)

print("Vetor ordenado:", ordenado)
print("Número total de cópias:", total_copias)