secreto = 42
while True:
    intento = int(input("Adivina el número: "))
    if intento == secreto:
        print("¡Acertaste!")
        break