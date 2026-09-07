contador= 1

while contador<=10:
    print(contador)
    contador+=1

    if contador==5:
        print("Vou pular o 5")
        continue

    if contador== 8:
        print(contador)
        break



print("acabou")