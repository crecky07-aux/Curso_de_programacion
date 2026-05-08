# Piedra, Papel, Tijera, Lagarto, Spock 🖖
# Simula el juego expandido y evalúa quién gana entre dos jugadores.

print("=== Piedra, Papel, Tijera, Lagarto, Spock ===")
print("Opciones válidas: piedra, papel, tijera, lagarto, spock")

jugador1 = input("Jugador 1 elige: ").strip().lower()
jugador2 = input("Jugador 2 elige: ").strip().lower()

opciones = {"piedra", "papel", "tijera", "lagarto", "spock"}
if jugador1 not in opciones or jugador2 not in opciones:
    print("Error: opción inválida. Use piedra, papel, tijera, lagarto o spock.")
    raise SystemExit(1)

if jugador1 == jugador2:
    resultado = "Empate"
else:
    gana_j1 = (
        (jugador1 == "tijera" and (jugador2 == "papel" or jugador2 == "lagarto")) or
        (jugador1 == "papel" and (jugador2 == "piedra" or jugador2 == "spock")) or
        (jugador1 == "piedra" and (jugador2 == "lagarto" or jugador2 == "tijera")) or
        (jugador1 == "lagarto" and (jugador2 == "spock" or jugador2 == "papel")) or
        (jugador1 == "spock" and (jugador2 == "tijera" or jugador2 == "piedra"))
    )
    resultado = "Jugador 1 gana" if gana_j1 else "Jugador 2 gana"

print("\n=== Resultado ===")
print(f"Jugador 1: {jugador1}")
print(f"Jugador 2: {jugador2}")
print(resultado)
