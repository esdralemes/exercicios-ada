def primeiro_caractere_unico(palavra):
    # Inicialize um dicionário para contar a frequência de cada caractere na palavra
    frequencia = {}

    # Preencha o dicionário contando as ocorrências de cada caractere
    for caractere in palavra:
        if caractere in frequencia:
            frequencia[caractere] += 1
        else:
            frequencia[caractere] = 1

    # Percorra a palavra novamente para encontrar o primeiro caractere não repetido
    for i, caractere in enumerate(palavra):
        if frequencia[caractere] == 1:
            return i

    # Se não houver caractere único, retorne -1
    return -1


# Exemplos de uso:
print(primeiro_caractere_unico("amor"))  # Saída: 0
print(primeiro_caractere_unico("cocada"))  # Saída: 1
print(primeiro_caractere_unico("aaabbb"))  # Saída: -1
