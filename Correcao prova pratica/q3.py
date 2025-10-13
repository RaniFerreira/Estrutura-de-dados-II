def insertion_sort_por_tamanho(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        # compara tamanhos dos nomes
        while j >= 0 and len(lista[j]) > len(atual):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
    return lista

# Teste
nomes = ["Ana", "Roberto", "Beatriz", "Daiana", "Júnio", "João", "Clara", "Lu"]
insertion_sort_por_tamanho(nomes)
print(nomes)
# Saída esperada: ['Lu', 'Ana', 'João', 'Júnio', 'Daiana', 'Roberto', 'Beatriz']