# Simulador de Compuertas Lógicas 🔌
# Pide dos booleanos y una compuerta (XOR, NAND, NOR, XNOR).
# Ejecuta la operación solo usando and, or, not.

print("=== Simulador de Compuertas Lógicas ===")

try:
    valor1 = input("Ingrese el primer valor (True/False): ").strip().capitalize()
    valor2 = input("Ingrese el segundo valor (True/False): ").strip().capitalize()
    puerta = input("Ingrese la compuerta (XOR, NAND, NOR, XNOR): ").strip().upper()

    if valor1 not in {"True", "False"} or valor2 not in {"True", "False"}:
        raise ValueError
    a = True if valor1 == "True" else False
    b = True if valor2 == "True" else False
except ValueError:
    print("Error: ingrese valores booleanos válidos (True/False) y una compuerta válida.")
    raise SystemExit(1)

if puerta not in {"XOR", "NAND", "NOR", "XNOR"}:
    print("Error: compuerta inválida. Use XOR, NAND, NOR o XNOR.")
    raise SystemExit(1)

# Operaciones usando solo and, or, not
and_result = a and b
or_result = a or b
not_a = not a
not_b = not b

if puerta == "XOR":
    resultado = (a or b) and not (a and b)
elif puerta == "NAND":
    resultado = not (a and b)
elif puerta == "NOR":
    resultado = not (a or b)
else:  # XNOR
    resultado = not ((a or b) and not (a and b))

print("\n=== Resultado ===")
print(f"A = {a}")
print(f"B = {b}")
print(f"Compuerta = {puerta}")
print(f"Salida = {resultado}")
