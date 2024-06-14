edad = int(input("cual es tu edad: "))
ingresos = float(input("cuales son tus ingresos mensuales: "))
if edad > 18 and ingresos >= 2000:
    print("tienes que pagar impuestos")
else:
    print("no tienes que pagar impuestos")
    