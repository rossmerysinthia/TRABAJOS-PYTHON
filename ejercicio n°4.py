

nombre = input("¿como te llamas? ")
genero = input("¿cusl es tu sexo (M o H)? ")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
        if nombre.lower() > "n":
            grupo = "A"
        else:
            grupo = "B"
print("tu grupo es " + grupo)