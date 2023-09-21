def substring_str(lista):
    substrings_encontradas = []  # Lista para armazenar as substrings encontradas

    # Percorra a lista de palavras
    for palavra1 in lista:
        for palavra2 in lista:
            # Verifique se palavra1 é uma substring de palavra2 e não é igual a palavra2
            if palavra1 in palavra2 and palavra1 != palavra2:
                substrings_encontradas.append(palavra1)
                break  # Uma vez que encontramos uma correspondência, saia do loop interno

    # Remova duplicatas e ordene a lista
    substrings_unicas = list(set(substrings_encontradas))
    substrings_unicas.sort(key=lambda x: lista.index(x))  # Mantenha a ordem original

    return substrings_unicas


# Exemplos de uso da função
entrada1 = ["as", "mas", "amor", "amoreco"]
saida1 = substring_str(entrada1)
print(saida1)  # Saída: ["as", "amoreco"]

entrada2 = ["carro", "ca", "paz", "pá"]
saida2 = substring_str(entrada2)
print(saida2)  # Saída: ["ca"]
