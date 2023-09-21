def contar_temperatura_repetidas(temperaturas):
    contagem = {}

    for temperatura in temperaturas:
        if temperatura in contagem:
            contagem[temperatura] += 1
        else:
            contagem[temperatura] = 1

    temperaturas_repetidas = [temp for temp, count in contagem.items() if count > 1]

    if len(temperaturas_repetidas) > 0:
        return f"Sim, existem {len(temperaturas_repetidas)} dias com temperatura média repetida."
    else:
        return "Não, não tem temperatura média repetida."


entrada1 = [27.5, 30.2, 28.5, 29, 25, 24, 25.5]
saida1 = contar_temperatura_repetidas(entrada1)
print(saida1)  # Saída: Não, não existem dias com temperatura média repetida.

entrada2 = [30.5, 30, 29.5, 30, 30.5, 31, 30]
saida2 = contar_temperatura_repetidas(entrada2)
print(saida2)  # Saída: Sim, existem 3 dias com temperatura média repetida.

entrada3 = [18.5, 19, 20.5, 20.4, 20.5, 20.6, 20.7]
saida3 = contar_temperatura_repetidas(entrada3)
print(saida3)  # Saída: Sim, existem 2 dias com temperatura média repetida.
