

print("Bienvenido a una aventura en Gielinor. Tus decisiones llevarán la historia por distintos caminos.")

respuesta1 = input("Escuchas un grito: el rey está en peligro. ¿CORRES a Varrock? SI o NO: ").strip().lower().replace("í", "i")
if respuesta1 == "si":
    respuesta2 = input("Llegas al castillo y ves goblins en el patio. ¿LUCHAS contra ellos? SI o NO: ").strip().lower().replace("í", "i")
    if respuesta2 == "si":
        respuesta3 = input("Derrotas a los goblins y encuentras un pasadizo secreto. ¿ENTRAS? SI o NO: ").strip().lower().replace("í", "i")
        if respuesta3 == "si":
            respuesta4 = input("El pasadizo te lleva a una sala de reliquias. ¿TOMAS la espada antigua? SI o NO: ").strip().lower().replace("í", "i")
            if respuesta4 == "si":
                respuesta5 = input("Escuchas pasos. ¿TE ESCONDES o TE MOSTRAS? SI o NO: ").strip().lower().replace("í", "i")
                if respuesta5 == "si":
                    respuesta6 = input("Un mago pasa cerca de tu escondite. ¿LO SIGUES hasta la torre? SI o NO: ").strip().lower().replace("í", "i")
                    if respuesta6 == "si":
                        print("Descubres un hechizo antiguo y salvas al rey con nueva magia.")
                    elif opcion6 == "no":
                        print("Sales sigiloso y llevas la espada al rey. Su reino se fortalece.")
                    else:
                        print("Opción no válida. El mago te ve y te obligan a pelear.")
                elif opcion5 == "no":
                    print("Te muestras y revelas tu presencia. El rey agradece tu valor inmediato.")
                else:
                    print("Opción no válida. El silencio te delata.")
            elif opcion4 == "no":
                print("Dejas la espada y buscas otra salida. Evitas la trampa y el rey escapa.")
            else:
                print("Opción no válida. La decisión se pierde en la oscuridad.")
        elif opcion3 == "no":
            opcion4 = input("Vuelves al patio y el rey te observa. ¿LE HABLAS directamente? SI o NO: ").strip().lower().replace("í", "i")
            if opcion4 == "si":
                opcion5 = input("El rey te pide escolta. ¿LO ACOMPAÑAS fuera del castillo? SI o NO: ").strip().lower().replace("í", "i")
                if opcion5 == "si":
                    opcion6 = input("Hay una emboscada afuera. ¿DEFIENDES al rey? SI o NO: ").strip().lower().replace("í", "i")
                    if opcion6 == "si":
                        print("Sacrificas tus fuerzas por el rey y te conviertes en guardián eterno.")
                    elif opcion6 == "no":
                        print("Dejas que el rey escape sin ti. Sobrevives, pero con culpa.")
                    else:
                        print("Opción no válida. Los guardias toman la decisión por ti.")
                elif opcion5 == "no":
                    print("Te quedas a proteger el castillo. El rey huye y vuelves a reconstruir la defensa.")
                else:
                    print("Opción no válida. El rey duda mientras hablas.")
            elif opcion4 == "no":
                print("Guardas silencio y actúas en secreto. El gato real te observa.")
            else:
                print("Opción no válida. El momento pasa.")
        else:
            print("Opción no válida. El pasadizo se cierra.")
    elif opcion2 == "no":
        opcion3 = input("Te alejas del castillo y ves una aldea cercana. ¿AYUDAS a los aldeanos? SI o NO: ").strip().lower().replace("í", "i")
        if opcion3 == "si":
            opcion4 = input("Los aldeanos te ofrecen comida y un mapa. ¿LO ACEPTAS? SI o NO: ").strip().lower().replace("í", "i")
            if opcion4 == "si":
                opcion5 = input("El mapa muestra un túnel hacia Varrock. ¿LO SIGUES? SI o NO: ").strip().lower().replace("í", "i")
                if opcion5 == "si":
                    opcion6 = input("El túnel es peligroso. ¿AVANZAS con cuidado? SI o NO: ").strip().lower().replace("í", "i")
                    if opcion6 == "si":
                        print("Llegas a Varrock sano y salvas al rey desde otro camino.")
                    elif opcion6 == "no":
                        print("El túnel se derrumba. Escapas justo a tiempo, pero pierdes la misión.")
                    else:
                        print("Opción no válida. La oscuridad te golpea.")
                elif opcion5 == "no":
                    print("Decides quedarte con los aldeanos. Construyes una aldea segura lejos del conflicto.")
                else:
                    print("Opción no válida. El mapa se pierde.")
            elif opcion4 == "no":
                print("Rechazas la ayuda y te conviertes en un viajero solitario.")
            else:
                print("Opción no válida. La aldea te mira confundida.")
        elif opcion3 == "no":
            print("Sigues tu camino solo. El reino queda sin tu apoyo.")
        else:
            print("Opción no válida. La aldea no entiende.")
    else:
        print("Opción no válida. El castillo espera tu elección.")
elif opcion1 == "no":
    opcion2 = input("Decides no ir a Varrock. ¿BUSCAS al rey en otro lugar? SI o NO: ").strip().lower().replace("í", "i")
    if opcion2 == "si":
        opcion3 = input("Lo buscas en la campiña. ¿ENTRAS en la cueva iluminada? SI o NO: ").strip().lower().replace("í", "i")
        if opcion3 == "si":
            opcion4 = input("Dentro hay un anciano con una espada rota. ¿LE PREGUNTAS por el rey? SI o NO: ").strip().lower().replace("í", "i")
            if opcion4 == "si":
                opcion5 = input("Te dice que el rey está oculto. ¿LO SIGUES? SI o NO: ").strip().lower().replace("í", "i")
                if opcion5 == "si":
                    opcion6 = input("Llegas a un campamento secreto. ¿LIBERAS al rey? SI o NO: ").strip().lower().replace("í", "i")
                    if opcion6 == "si":
                        print("Libera al rey y recibe una recompensa real. Tu decisión protagonista cambia el reino.")
                    elif opcion6 == "no":
                        print("Te retiras. El anciano te recuerda que no todos nacen para héroes.")
                    else:
                        print("Opción no válida. El campamento te detecta.")
                elif opcion5 == "no":
                    print("Decides no seguir al anciano. Tu aventura se convierte en leyenda perdida.")
                else:
                    print("Opción no válida. La duda te detiene.")
            elif opcion4 == "no":
                print("Ignoras al anciano y sales. El rey sigue en peligro.")
            else:
                print("Opción no válida. El anciano se aleja.")
        elif opcion3 == "no":
            print("No entras en la cueva. El reino necesita a alguien más valiente.")
        else:
            print("Opción no válida. La campiña queda en silencio.")
    elif opcion2 == "no":
        print("Te vas sin actuar. El reino sigue su destino sin ti.")
    else:
        print("Opción no válida. Debes responder SI o NO.")
else:
    print("Opción no válida. Responde con SI o NO.")
