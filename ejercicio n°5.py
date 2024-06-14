
edad = int(input("ingrese su edad: "))
if edad < 4:
    precio = 0
elif 4 <= 18:
    precio = 10
else:
    precio = 20
print("el precio de la entrada es", precio, "soles.")