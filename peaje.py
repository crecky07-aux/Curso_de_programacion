vehiculo = input("Ingrese tipo de vehículo (automovil, motocicleta, camion): ").lower() #variable
hora_pico= input("¿Es hora pico? (si/no): ").lower() #variable

precio = 0 #precio base para peaje

if vehiculo == "automovil":
    precio = 5

elif vehiculo == "motocicleta":
    precio = 2

elif vehiculo == "camion":
    precio = 10

else:
    precio = -1   

if precio == -1:
    print("Error: vehiculo no valido.")

else:
    
    if hora_pico == "si":
        total = precio + (precio * 0.20)
    else:
        total = precio
    
    print(f"El total a pagar por el {vehiculo} es: ${total}")

