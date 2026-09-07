# Exercício - sistema de perguntas e respostas

import os

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

perguntas = [
    {
        'Pergunta': 'Qual é o maior planeta do Sistema Solar?',
        'Opções': ['Terra', 'Marte', 'Júpiter', 'Saturno'],
        'Resposta': 'Júpiter',
    },
    {
        'Pergunta': 'Qual animal é conhecido como o rei da selva?',
        'Opções': ['Tigre', 'Leão', 'Elefante', 'Gorila'],
        'Resposta': 'Leão',
    },
    {
        'Pergunta': 'Quanto é 12 x 4?',
        'Opções': ['36', '42', '48', '52'],
        'Resposta': '48',
    },
    {
        'Pergunta': 'Quanto é 8*4?',
        'Opções': ['28', '30', '32', '36'],
        'Resposta': '32',
    },
    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'Resposta': 'Brasília',
    },
]

alternativas= ['A', None],['B', None],['C', None],['D', None]
acertos=0

def pergunta(lista):
    acertos=0
    for pergunta in lista:
        i=0
        print(list(pergunta.values())[0])
        for alternativa in list(pergunta.values())[1]:
            (alternativas)[i][1]=alternativa
            print(f"{alternativas[i][0]})"f"{alternativas[i][1]}")
            i+=1
        resposta=str(list(pergunta.values())[2])

        resposta_inserida=None

        while resposta_inserida not in dict(alternativas).keys():
            resposta_inserida=input("Insira sua resposta:").upper()
            if resposta_inserida in dict(alternativas).keys():
                break
            else:
                print("Insira uma das alternativas!")
                continue
        
        if resposta_inserida=="A":
            _=0
        if resposta_inserida=="B":
            _=1
        if resposta_inserida=="C":
            _=2
        if resposta_inserida=="D":
            _=3

        resposta_inserida=((tuple(alternativas))[_][1])

        if resposta_inserida==resposta:
            acertos+=1

        os.system("cls")
    return acertos

acertos=pergunta(perguntas)


# for pergunta in perguntas:
#     print(tuple(pergunta.values()))

print(f"Parabéns, você acertou {acertos} de {len(perguntas)} perguntas.") # contagem de acertos
