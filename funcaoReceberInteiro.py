#– 2 Escreva uma função que receba um inteiro x e um vetor v[0..n-1] de inteiros em ordem
#crescente e insira x no vetor de modo a manter a ordem crescente.

def inserir_ordenado(v, x):
    # Percorre o vetor para encontrar a posição correta de inserção
    for i in range(len(v)):
        if x <= v[i]:
            v.insert(i, x)  # Insere x antes do elemento maior ou igual
            print(f"Vetor após inserção: {v}")
            return
    # Se não encontrou posição, significa que x é maior que todos os elementos
    v.append(x)
    print(f"Vetor após inserção: {v}")

# Exemplo de uso:
vetor = [1, 3, 5, 7, 9]
inserir_ordenado(vetor, 6)  # Saída: [1, 3, 5, 6, 7, 9]

inserir_ordenado(vetor, 0)  # Saída: [0, 1, 3, 5, 6, 7, 9]

inserir_ordenado(vetor, 10) # Saída: [0, 1, 3, 5, 6, 7, 9, 10]