import calendar

mes=input("Insira o mês(1-12):")

while mes not in range(1,13):
    print("Mês incorreto, insira um número de 1 a 12")
    mes=(input("Insira o mês(1-12):"))


ano=int(input("Insira o ano:"))

# while mes is not int:
#     print("Mês incorreto, insira um número de 1 a 12")
#     mes=int(input("Insira o mês(1-12):"))



print()
print(calendar.month(ano,mes))
