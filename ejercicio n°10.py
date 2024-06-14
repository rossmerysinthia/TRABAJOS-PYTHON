
numero = int(input("introduce la altura del triangulo (entero positivo):"))
for i in range(1, numero + 1):
    for j in range(i, 0 , -2):
        print(j, end=" ")
    print("")