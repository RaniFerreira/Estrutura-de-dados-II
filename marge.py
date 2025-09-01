#6.– Invente um algoritmo de ordenação que seja mais rápido que o de inserção e o de seleção.


#O Merge Sort já existe, é um algoritmo clássico e muito conhecido.
#Divide o vetor em partes menores até chegar em vetores de 1 elemento.
#Combina as partes de forma ordenada.
#Complexidade: O(n log n), mais rápido que Selection ou Insertion Sort para vetores grandes.


def merge_sort(v):
    if len(v) > 1:
        meio = len(v) // 2
        esquerda = v[:meio]
        direita = v[meio:]

        # Ordena as duas metades recursivamente
        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # Combina as duas metades ordenadas
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                v[k] = esquerda[i]
                i += 1
            else:
                v[k] = direita[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes (se houver)
        while i < len(esquerda):
            v[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            v[k] = direita[j]
            j += 1
            k += 1

# Exemplo de uso:
vetor = [38, 27, 43, 3, 9, 82, 10]
merge_sort(vetor)
print("Vetor ordenado:", vetor)
