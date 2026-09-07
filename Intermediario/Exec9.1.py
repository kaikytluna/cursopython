import os

perguntas = [
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

dict1=[
    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['São Paulo', 'Brasília', 'Rio de Janeiro', 'Salvador'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Quantos dias tem uma semana?',
        'Opções': ['5', '6', '7', '8'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual planeta é conhecido como Planeta Vermelho?',
        'Opções': ['Vênus', 'Marte', 'Júpiter', 'Mercúrio'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Quantos lados tem um triângulo?',
        'Opções': ['2', '3', '4', '5'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual animal é conhecido como o rei da selva?',
        'Opções': ['Tigre', 'Leão', 'Elefante', 'Gorila'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual é o maior oceano do mundo?',
        'Opções': ['Atlântico', 'Índico', 'Pacífico', 'Ártico'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Quanto é 10 × 5?',
        'Opções': ['40', '45', '50', '55'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual destes animais é um mamífero?',
        'Opções': ['Cobra', 'Tubarão', 'Golfinho', 'Galinha'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Quantos meses existem em um ano?',
        'Opções': ['10', '11', '12', '13'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é a estrela mais próxima da Terra?',
        'Opções': ['Sirius', 'Sol', 'Vega', 'Betelgeuse'],
        'Resposta': 1
    }
]
dict2 = [
    {
        'Pergunta': 'Quem pintou a Mona Lisa?',
        'Opções': ['Van Gogh', 'Leonardo da Vinci', 'Picasso', 'Michelangelo'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual é o maior país do mundo em território?',
        'Opções': ['China', 'Estados Unidos', 'Canadá', 'Rússia'],
        'Resposta': 3
    },
    {
        'Pergunta': 'Qual é o símbolo químico do ouro?',
        'Opções': ['Ag', 'Au', 'Fe', 'Go'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Em que continente fica o Egito?',
        'Opções': ['Ásia', 'Europa', 'África', 'Oceania'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é o maior órgão do corpo humano?',
        'Opções': ['Coração', 'Fígado', 'Pele', 'Pulmão'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é a capital da Austrália?',
        'Opções': ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é o idioma mais falado no mundo considerando falantes nativos?',
        'Opções': ['Inglês', 'Espanhol', 'Mandarim', 'Hindi'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual planeta possui os anéis mais famosos do Sistema Solar?',
        'Opções': ['Marte', 'Saturno', 'Urano', 'Netuno'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Em que ano o Brasil declarou sua independência?',
        'Opções': ['1500', '1789', '1822', '1889'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é o maior deserto quente do mundo?',
        'Opções': ['Saara', 'Atacama', 'Gobi', 'Kalahari'],
        'Resposta': 0
    }
]
dict3 = [
    {
        'Pergunta': 'Qual é o elemento químico de número atômico 26?',
        'Opções': ['Cobre', 'Ferro', 'Zinco', 'Níquel'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual civilização construiu Machu Picchu?',
        'Opções': ['Maias', 'Astecas', 'Incas', 'Egípcios'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é a capital da Mongólia?',
        'Opções': ['Astana', 'Ulan Bator', 'Tbilisi', 'Bishkek'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual é o processo pelo qual as plantas produzem seu alimento?',
        'Opções': ['Respiração', 'Fermentação', 'Fotossíntese', 'Transpiração'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Quem escreveu a obra "Dom Quixote"?',
        'Opções': ['Miguel de Cervantes', 'Dante Alighieri', 'William Shakespeare', 'Machado de Assis'],
        'Resposta': 0
    },
    {
        'Pergunta': 'Qual é o menor país do mundo em território?',
        'Opções': ['Mônaco', 'Vaticano', 'Malta', 'San Marino'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual cientista formulou as três leis do movimento?',
        'Opções': ['Albert Einstein', 'Galileu Galilei', 'Isaac Newton', 'Nicolau Copérnico'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual é a unidade básica da vida?',
        'Opções': ['Átomo', 'Molécula', 'Célula', 'Tecido'],
        'Resposta': 2
    },
    {
        'Pergunta': 'Qual país foi o primeiro a enviar um ser humano ao espaço?',
        'Opções': ['Estados Unidos', 'União Soviética', 'China', 'Alemanha'],
        'Resposta': 1
    },
    {
        'Pergunta': 'Qual é o nome da galáxia onde está localizado o Sistema Solar?',
        'Opções': ['Andrômeda', 'Via Láctea', 'Galáxia do Triângulo', 'Sombrero'],
        'Resposta': 1
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
total_perguntas=0
opçoes_dificuldade=[1,2,3]

while True:
    print("Escolha a dificuldade:")
    print(f"\033[32m1 - Fácil \033[m")
    print(f"\033[1;33m2 - Médio \033[m")
    print(f"\033[31m3 - Difícil \033[m")
    dificuldade_escolhida=(input("Selecione a dificuldade:"))

    total_perguntas+=10
    dificuldade_perguntas=None
    int_escolha=None

    if dificuldade_escolhida.isdigit():
        int_escolha=int(dificuldade_escolhida)

    if int_escolha==1:
        dificuldade_perguntas=dict1
    if int_escolha==2:
        dificuldade_perguntas=dict2
    if int_escolha==3:
        dificuldade_perguntas=dict3

    if dificuldade_escolhida=="sair":
        print("Saindo do jogo.")
        break
        

    os.system("cls")
    for pergunta in dificuldade_perguntas:
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

    media=(pontos/total_perguntas)*100
    
    print(f"Parabéns, você acertou {f"\033[32m{pontos}\033[m"} de {f"\033[32m{total_perguntas}\033[m"} perguntas.")

    if media>=70:
        print(f"E teve uma média de {f"\033[32m{media}% \033[m"}")
    if 30<media<70:
        print(f"E teve uma média de {f"\033[33m{media}% \033[m"}")
    if media<=30:
        print(f"E teve uma média de {f"\033[31m{media}% \033[m"}")

    print()
    saida=input("Deseja tentar novamente? [s]im [n]ão:")
    if saida=="s":
        os.system("cls")
        continue
    if saida=="n":
        print()
        print("Saindo do jogo.")
        break
    # break








    # sair=input("Deseja sair?")
    # break



# print(f"\033[32mTexto! \033[m") # cor verde no texto
# print(f"\033[31mTexto! \033[m") # cor vermelha no texto