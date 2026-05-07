
ingresos = float(input("Ingrese sus ingresos mensuales: "))
edad = int(input("Ingrese su edad: "))


if ingresos > 3000 and edad > 25:
    print("Préstamo aprobado")
elif 1500 <= ingresos <= 3000 and edad >= 18:
    print("Aprobado con aval")
else:
    print("Préstamo rechazado")