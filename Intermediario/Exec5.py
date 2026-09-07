'''
Crie um programa que permita cadastrar alunos e suas notas.

O programa deve:

Perguntar o nome do aluno.
Perguntar a nota dele.
Armazenar os dados em um dicionário no formato:

alunos = {
    "João": 8.5,
    "Maria": 7.0,
    "Carlos": 9.2
}

O programa deve continuar perguntando novos alunos até que o usuário digite "sair" como nome.

Depois, mostre:
Todos os alunos e suas notas.
A média da turma.
O aluno com a maior nota.
'''
import os

qnt_notas=2
somatorio_notas=0
maior_nota=0
aluno_maior_nota=[]
alunos={"Sarah" : 10,
        "Kaiky" : 10,

}

def media(somatorio_notas):
    resultado = somatorio_notas / len(alunos)
    return resultado

while True:
    os.system("cls")
    nome_aluno=input("Insira o nome do aluno: ").capitalize()

    alunos[nome_aluno]= float(input("Insira a nota do aluno: "))
    qnt_notas+=1

    sair=input("Deseja inserir mais um aluno? [s]im [n]ão : ").lower()

    if sair=='n' or sair=="não" or sair=="nao":
        os.system("cls")
        break
    else:
        continue

for nome, nota in alunos.items():
    print(f"Nome do aluno: {nome}")
    print(f"Nota: {nota}")
    print()

for nota in alunos.values():
    somatorio_notas+=nota
    if nota>maior_nota:
        maior_nota=nota

media_alunos=media(somatorio_notas)


for nome, nota in alunos.items():
    if nota==maior_nota:
        aluno_maior_nota.append(nome)


print(f"A média dos alunos foi: {media_alunos: .2f}")
print()

if len(aluno_maior_nota)==1:
    print(f"O aluno(a) com a maior nota foi {aluno_maior_nota} com nota {maior_nota}")
elif len(aluno_maior_nota)==2:
    print(f"Os alunos com a maior nota foram {' e '.join(aluno_maior_nota)} com nota {maior_nota}")
else:
    print(f"Os alunos com a maior nota foram {', '.join(aluno_maior_nota[:-1])} e {aluno_maior_nota[-1]} com notas {maior_nota}")

