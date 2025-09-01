#– 1 Escreva uma função que verifique se um vetor v[0..n-1] está em ordem crescente.


def verificar_ordem_crescente(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            print("O vetor NÃO está em ordem crescente.")
            return
    print("O vetor está em ordem crescente.")

# Exemplo de uso:
vetor1 = [1, 2, 3, 4, 5]
verificar_ordem_crescente(vetor1)  # Saída: O vetor está em ordem crescente.

vetor2 = [1, 3, 2, 4, 5]
verificar_ordem_crescente(vetor2)  # Saída: O vetor NÃO está em ordem crescente.
