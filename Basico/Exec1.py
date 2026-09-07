nome= (input("Insira seu nome: "))
sobrenome= (input("Insira seu sobrenome: "))
idade= (int(input("Insira sua idade: ")))
altura= (float(input("Insira sua altura: ")))

print("Nome: ", nome)
print("Sobrenome: ", sobrenome)
print(f"Você tem {idade} anos.")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
print(f"Você tem {altura} metros. ")