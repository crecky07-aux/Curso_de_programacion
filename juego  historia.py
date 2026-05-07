
print("Bienvenido a OSRS.")

opcion1 = input("Encuentras el Godsword. ¿LO TOMAS? SI o NO: ").strip().lower().replace("í", "i")
if opcion1 == "si":
    opcion2 = input("Vas al Wilderness. ¿ENTRAS? SI o NO: ").strip().lower().replace("í", "i")
    if opcion2 == "si":
        opcion3 = input("Ves un jugador. ¿LO RETAS? SI o NO: ").strip().lower().replace("í", "i")
        if opcion3 == "si":
            opcion4 = input("Duelo comienza. ¿USAS ESPECIAL? SI o NO: ").strip().lower().replace("í", "i")
            if opcion4 == "si":
                opcion5 = input("Rival débil. ¿TE CURAS? SI o NO: ").strip().lower().replace("í", "i")
                if opcion5 == "si":
                    opcion6 = input("Preparado. ¿ATACAS? SI o NO: ").strip().lower().replace("í", "i")
                    if opcion6 == "si":
                        print("Ganas y eres leyenda.")
                    elif opcion6 == "no":
                        print("Te retiras con honor.")
                    else:
                        print("Opción no válida.")
                elif opcion5 == "no":
                    print("Pierdes por falta de cura.")
                else:
                    print("Opción no válida.")
            elif opcion4 == "no":
                print("Pierdes sin especial.")
            else:
                print("Opción no válida.")
        elif opcion3 == "no":
            print("Evitas pelea y sobrevives.")
        else:
            print("Opción no válida.")
    elif opcion2 == "no":
        print("Regresas a Varrock.")
    else:
        print("Opción no válida.")
elif opcion1 == "no":
    print("Sigues sin el Godsword.")
else:
    print("Opción no válida.")
