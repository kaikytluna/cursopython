alunos={"Sarah" : 10,
        "Kaiky" : 10,
}

# for chave, valor in list(alunos.items()):
#     print(chave, valor)
alunos.setdefault("idade", "indefinido") # setar um padrão
print(alunos["idade"])