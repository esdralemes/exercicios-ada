def avaliacao(lista):
    result = []  # Lista para armazenar os resultados dos alunos

    # Itera sobre a lista de alunos
    for aluno in lista:
        nome = aluno["nome"]  # Obtém o nome do aluno
        nota = aluno["nota"]  # Obtém a nota do aluno
        faltas = aluno["faltas"]  # Obtém o número de faltas do aluno

        # Calcula a porcentagem de presença do aluno
        presenca = ((60 - faltas) / 60) * 100

        # Verifica se o aluno atende aos critérios de aprovação
        if presenca >= 60 and nota >= 7:
            result.append(f"{nome} está aprovado(a)")  # Adiciona mensagem de aprovação à lista
        else:
            result.append(f"{nome} está reprovado(a)")  # Adiciona mensagem de reprovação à lista

    return result


# Lista de alunos com seus dados
alunos = [
    {"nome": "João", "nota": 7, "faltas": 5},
    {"nome": "Maria", "nota": 7, "faltas": 30},
    {"nome": "Jose", "nota": 7, "faltas": 20}
]

# Chama a função para avaliar os alunos e obter os resultados
resultados = avaliacao(alunos)

# Exibe os resultados
for resultado in resultados:
    print(resultado)
