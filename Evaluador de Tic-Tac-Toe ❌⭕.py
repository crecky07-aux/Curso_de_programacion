# Evaluador de Tic-Tac-Toe ❌⭕
# Usa 9 variables para un tablero y una sola mega-condición para saber si X ganó.

print("=== Evaluador de Tic-Tac-Toe ===")
print("Ingrese cada celda del tablero: X, O o espacio vacío.")

x1 = input("Celda 1: ").strip().upper()
x2 = input("Celda 2: ").strip().upper()
x3 = input("Celda 3: ").strip().upper()
x4 = input("Celda 4: ").strip().upper()
x5 = input("Celda 5: ").strip().upper()
x6 = input("Celda 6: ").strip().upper()
x7 = input("Celda 7: ").strip().upper()
x8 = input("Celda 8: ").strip().upper()
x9 = input("Celda 9: ").strip().upper()

valid_values = {"X", "O", ""}
for i, value in enumerate([x1, x2, x3, x4, x5, x6, x7, x8, x9], start=1):
    if value not in valid_values:
        print(f"Valor inválido en celda {i}. Use X, O o deje vacío.")
        raise SystemExit(1)

x_gano = (
    (x1 == "X" and x2 == "X" and x3 == "X") or
    (x4 == "X" and x5 == "X" and x6 == "X") or
    (x7 == "X" and x8 == "X" and x9 == "X") or
    (x1 == "X" and x4 == "X" and x7 == "X") or
    (x2 == "X" and x5 == "X" and x8 == "X") or
    (x3 == "X" and x6 == "X" and x9 == "X") or
    (x1 == "X" and x5 == "X" and x9 == "X") or
    (x3 == "X" and x5 == "X" and x7 == "X")
)

print("\n=== Resultado ===")
if x_gano:
    print("X ganó.")
else:
    print("X no ganó.")
