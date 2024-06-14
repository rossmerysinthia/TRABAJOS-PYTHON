
frase = input("introduce una frase: ")
letra = input("introduce la letra: ")
contador = 0
for i in frase:
    if i == frase:
          contador += 1
print("LA LETRA", letra, "APARECE" , contador, "VECES EN LA FRASE", frase)
#print("la letra ´%s´ aparece %2i veces en la frase ´%s´," % (letra contador, frase))