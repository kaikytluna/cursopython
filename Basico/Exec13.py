# frase="Eu ainda amo ela."
frase=input("Digite sua frase: ")

i=0
qnt_mais_vzs=0
letra_mais_vzs=""

'''dá pra colocar todas as letras que aparecem mais vezes usando listas
mas nao aprendi ainda'''

while i<len(frase):
    letra_atual=frase[i]
    if letra_atual in letra_mais_vzs:
        i+=1
        continue

    qnt_atual=(frase.count(letra_atual))

    if letra_atual==" ":
        i+=1
        continue

    if qnt_mais_vzs<qnt_atual:
        qnt_mais_vzs=qnt_atual
        letra_mais_vzs=letra_atual

    i+=1

print(f'A letra que apareceu mais foi "{letra_mais_vzs}", que apareceu {qnt_mais_vzs}x na frase.')
