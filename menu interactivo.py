while True:
    print("1. Saludar\n2. Sumar 2+2\n3. Ver hora simulada\n4. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        print("Hola")
    elif opcion == "2":
        print(4)
    elif opcion == "3":
        print("12:00")
    elif opcion == "4":
        break
    else:
        print("Inválido")