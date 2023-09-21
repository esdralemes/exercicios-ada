def ordenar_lista(lista):
    # Usando a função sorted para ordenar a lista de forma crescente
    lista_ordenada = sorted(lista)

    # Retornando a lista ordenada
    return lista_ordenada


# Exemplo de uso da função
dados = [5, 2, 9, 1, 8]
dados_ordenados = ordenar_lista(dados)
print(dados_ordenados)  # Saída: [1, 2, 5, 8, 9]
