numero= (input("Insira um número: "))

try:
    numero_float=float(numero)
    print(f"O dobro de {numero} é {numero_float * 2:.0f}")
except:
    print("Isso não é um número")