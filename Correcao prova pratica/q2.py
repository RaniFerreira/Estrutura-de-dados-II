def selection_sort_inverse(array):
    n = len(array)
    for i in range(n):
        # encontra o maior elemento na parte não ordenada
        indice_maior = i
        for j in range(i + 1, n):
            if array[j] > array[indice_maior]:
                indice_maior = j
        # troca o maior elemento encontrado com o atual
        array[i], array[indice_maior] = array[indice_maior], array[i]
    return array

# Teste
lista_exemplo = [11, 4, 30, 22, 7, 26]
selection_sort_inverse(lista_exemplo)
print(lista_exemplo)  # Saída esperada: [30, 26, 22, 11, 7, 4]