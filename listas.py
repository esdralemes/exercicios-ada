def numero_unico(temperaturas):
    # Crie um dicionário para rastrear a contagem de cada número
    contagem = {}

    # Percorra a lista e atualize a contagem de cada número
    for temperatura in temperaturas:
        if temperatura in contagem:
            contagem[temperatura] += 1
        else:
            contagem[temperatura] = 1

    # Encontre o número único (contagem igual a 1)
    for chave, valor in contagem.items():
        if valor == 1:
            return chave


# Exemplos de uso da função
entrada1 = [18, 19, 20, 21, 20, 19, 18]
saida1 = numero_unico(entrada1)
print(saida1)  # Saída: 21

entrada2 = [28.5, 27.9, 28.5, 27.9, 30, 28.5]
saida2 = numero_unico(entrada2)
print(saida2)  # Saída: 30
