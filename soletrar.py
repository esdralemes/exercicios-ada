def separar_caracteres(palavra):
    # Inicializa uma lista vazia para armazenar os caracteres separados
    lista_caracteres = []

    # Percorre cada caractere na palavra
    for caractere in palavra:
        # Adiciona o caractere à lista
        lista_caracteres.append(caractere)

    # Retorna a lista de caracteres
    return lista_caracteres


# Exemplos de uso da função
entrada1 = "familia"
saida1 = separar_caracteres(entrada1)
print(saida1)  # Saída: ["f", "a", "m", "i", "l", "i", "a"]
