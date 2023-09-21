def par_e_impar(lista):
    # Inicializa contadores para pares e ímpares
    pares = 0
    impares = 0

    # Percorre a lista de números
    for numero in lista:
        # Verifica se o número é par (resto da divisão por 2 é igual a 0)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    # Formata a string de saída com a quantidade de pares e ímpares
    resultado = f"{pares} pares, {impares} ímpares"

    return resultado


entrada1 = [16, 6, 14, 6, 13, 6, 0, 2, 17, 28]
saida1 = par_e_impar(entrada1)
print(saida1)  # Saída: "8 pares, 2 ímpares"

entrada2 = [16, 26, 114, 16, 6, 100, 2, 7, 9, 4, 15]
saida2 = par_e_impar(entrada2)
print(saida2)  # Saída: "7 pares, 0 ímpar"

entrada3 = [5, 10, 1, 20, 21, 19, 2, 2, 10, 20]
saida3 = par_e_impar(entrada3)
print(saida3)  # Saída: "6 pares, 4 ímpares"
