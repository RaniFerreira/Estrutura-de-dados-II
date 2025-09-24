def bubble_sort_string(s):
    s = list(s)  # transforma a string em lista (para poder trocar os elementos)
    n = len(s)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if s[j] > s[j + 1]:
                # troca
                s[j], s[j + 1] = s[j + 1], s[j]
    
    return "".join(s)  # junta de volta em string


# Programa principal
palavra = "cdeab"
resultado = bubble_sort_string(palavra)
print("String em ordem crescente:", resultado)
