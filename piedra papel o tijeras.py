
jugador1 = input("Jugador 1, elige: piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige: piedra, papel o tijera: ").lower()


if jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "papel" and jugador2 == "piedra") or \
     (jugador1 == "tijera" and jugador2 == "papel"):
    print("Gana Jugador 1")
else:
    print("Gana Jugador 2")