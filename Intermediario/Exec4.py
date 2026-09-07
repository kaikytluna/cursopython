# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# valor=int(input("Insira um valor: "))

# def double(valor):
#     return valor*2

# def triple(valor):
#     return valor*3

# def quadruple(valor):
#     return valor*4


# dobro=double(valor)
# triplo=triple(valor)
# quadruplo=quadruple(valor)

# print(f"O Dobro do seu número é {dobro}")
# print(f"O Triplo do seu número é {triplo}")
# print(f"O Quadruplo do seu número é {quadruplo}")

def multiplicar(multiplicador):
    def multiplo(numero):
        return numero * multiplicador
    return multiplo

dobro=multiplicar(2)
triplo=multiplicar(3)
quadruplo=multiplicar(4)

print(dobro(2))
print(triplo(3))
print(quadruplo(4))