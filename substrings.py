def soletrando_invertido_str(palavra):
    # Inverte a string usando slicing [::-1]
    palavra_invertida = palavra[::-1]

    # Converte a string invertida em uma lista de caracteres
    lista_caracteres = list(palavra_invertida)

    # Retorna a lista de caracteres
    return lista_caracteres

# Exemplos de uso da função
entrada1 = "amor"
saida1 = soletrando_invertido_str(entrada1)
print(saida1)  # Saída: ["r", "o", "m", "a"]

entrada2 = "carro"
saida2 = soletrando_invertido_str(entrada2)
print(saida2)  # Saída: ["o", "r", "r", "a", "c"]
