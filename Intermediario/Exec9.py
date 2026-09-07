import os

perguntas=perguntas = [
    {
        'Pergunta': 'Qual é o maior planeta do Sistema Solar?',
        'Opções': ['Terra', 'Marte', 'Júpiter', 'Vênus'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Quantos dias tem uma semana?',
        'Opções': ['5', '6', '7', '8'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['São Paulo', 'Brasília', 'Rio de Janeiro', 'Salvador'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual animal é conhecido como o rei da selva?',
        'Opções': ['Tigre', 'Leão', 'Elefante', 'Urso'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Quantos lados tem um triângulo?',
        'Opções': ['2', '3', '4', '5'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual é o maior oceano do planeta?',
        'Opções': ['Atlântico', 'Índico', 'Pacífico', 'Ártico'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é o resultado de 10 + 15?',
        'Opções': ['20', '25', '30', '35'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual destes é um continente?',
        'Opções': ['Brasil', 'Europa', 'Amazonas', 'Japão'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual gás os seres humanos precisam respirar para sobreviver?',
        'Opções': ['Oxigênio', 'Hélio', 'Hidrogênio', 'Gás carbônico'],
        'Resposta': 0
    },
    {
        'Pergunta': 'Quantos meses existem em um ano?',
        'Opções': ['10', '11', '12', '13'],
        'Resposta': 2
    }
]
perguntas1 = [
    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['São Paulo', 'Brasília', 'Rio de Janeiro', 'Salvador'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Quanto é 12 * 8?',
        'Opções': ['86', '96', '108', '88'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual destes é um tipo de dado do Python?',
        'Opções': ['string', 'character', 'decimal', 'letter'],
        'Resposta': 0
    },
    {
        'Pergunta': 'Qual planeta é conhecido como Planeta Vermelho?',
        'Opções': ['Vênus', 'Júpiter', 'Marte', 'Mercúrio'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual método adiciona um item ao final de uma lista?',
        'Opções': ['add()', 'insert()', 'append()', 'push()'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual destes animais é um mamífero?',
        'Opções': ['Tubarão', 'Golfinho', 'Cobra', 'Tartaruga'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Quanto é 144 / 12?',
        'Opções': ['10', '11', '12', '14'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual estrutura é usada para repetir um código enquanto uma condição for verdadeira?',
        'Opções': ['if', 'for', 'while', 'def'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual destes é usado para armazenar pares de chave e valor em Python?',
        'Opções': ['Lista', 'Tupla', 'Set', 'Dicionário'],
        'Resposta': 3
    },
    {
        'Pergunta': 'Qual função é usada para receber uma entrada do usuário em Python?',
        'Opções': ['input()', 'print()', 'get()', 'read()'],
        'Resposta': 0
    }
]




alternativas=("A","B","C","D")
opçoes={
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
}
pontos=0
resposta_inserida=""

dificuldade_escolhida=""


while True:

    for pergunta in perguntas:
        i=0
        print(pergunta['Pergunta'])
        answer=pergunta['Resposta']
        for alternativa in pergunta['Opções']:
            print(f"{alternativas[i]})",alternativa)
            i+=1

            # resposta_inserida="C"
        while len(resposta_inserida) != 1 :
            resposta_inserida=input("Insira sua resposta: ").upper()
            if len(resposta_inserida)>1:
                print(f"\033[31mInsira apenas um caracter. \033[m")
                continue

            if len(resposta_inserida)==0:
                print(f"\033[31mInsira ao menos um caracter. \033[m")
                continue
            
            if resposta_inserida not in alternativas:
                print(f"\033[31mInsira uma das alternativas \033[m")
                resposta_inserida=""
                continue

        index_resposta_inserida=opçoes[str(resposta_inserida)]
        os.system("cls")
        i=0
        if index_resposta_inserida==int(answer): # resposta correta
            print(pergunta['Pergunta'])
            for alternativa in pergunta['Opções']:
                if i==int(answer):
                    print(f"\033[32m{alternativas[i]}) {alternativa} \033[m")
                    i+=1
                    pontos+=1
                    continue
                print(f"{alternativas[i]})",alternativa)
                i+=1
            print()
            print("Parabéns, você acertou! +1 ponto.")
            print()
            input("Próxima pergunta?")
            os.system("cls")

        if index_resposta_inserida!=int(answer):
            print(pergunta['Pergunta'])
            for alternativa in pergunta['Opções']:
                if i==int(answer):
                    print(f"\033[32m{alternativas[i]}) {alternativa} \033[m")
                    i+=1
                    continue
                if i==index_resposta_inserida:
                    print(f"\033[31m{alternativas[i]}) {alternativa} \033[m")
                    i+=1
                    continue
                print(f"{alternativas[i]})",alternativa)
                i+=1    
            print()
            print(f"\033[31mQue pena, você errou. \033[m")
            print()
            input("Próxima pergunta?")
            os.system("cls")
        resposta_inserida=""

    print(f"Parabéns, você acertou {pontos} de {len(perguntas)} perguntas.")
    print(f"E teve uma média de {pontos*10}%")
    break








    # sair=input("Deseja sair?")
    # break



# print(f"\033[32mTexto! \033[m") # cor verde no texto
# print(f"\033[31mTexto! \033[m") # cor vermelha no texto