
#Questão1

def verifica (lista):
    n = len(lista)

    for i in range(n-1):
        if lista[i] > lista[i+1]:
            return False
    return True


#Questão2

def bubble_sort_otimizado(lista):
    n = len(lista)

    for i in range(n-1):
        troca = False
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[i], lista[j+1] = lista[j+1],lista[j]
                Troca = True
        if not troca:
            break

    return lista


#Questão6

def insertion_sort(lista):
    n = len(lista)

    for i in range(1,n):
        chave = lista[i]
        j = n-1

        while j>=0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j-=1

        lista[j+1] = chave

    return lista

#Questao7

def insertion_sort_recursivo(lista,n=None):
    if n is None:
        n = len(lista)
    
    if n<=1:
        return

    insertion_sort_recursivo(lista,n-1)

        ultimo = lista[n-1]
        j = n-2

        whiile j>=0 and lista[j] > ultimo
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = ultimo


    


