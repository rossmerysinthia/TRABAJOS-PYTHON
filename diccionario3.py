#Podemos iterar a través de los elementos de un diccionario utilizando un bucle for. El bucle for itera a través de las claves por defecto, pero podemos acceder a los valores utilizando las claves:
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
for clave in estudiantes:
    print(clave, estudiantes[clave])
    
#Esto imprimirá cada clave y su valor en una línea separada:
Juan = 16
Ana = 18
Luis = 17

#También podemos utilizar el método items() para obtener una lista de tuplas clave:valor y luego iterar a través de ellas:
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
for clave, valor in estudiantes.items():
    print(clave, valor)
    