# Clasificación Estricta IPv4
# Pide 4 octetos, valida rango 0-255, clasifica según el primer octeto.

print("=== Clasificador IPv4 ===")

try:
    octeto1 = int(input("Ingrese el primer octeto: ").strip())
    octeto2 = int(input("Ingrese el segundo octeto: ").strip())
    octeto3 = int(input("Ingrese el tercer octeto: ").strip())
    octeto4 = int(input("Ingrese el cuarto octeto: ").strip())
except ValueError:
    print("Error: cada octeto debe ser un número entero.")
    raise SystemExit(1)

if not (0 <= octeto1 <= 255):
    print("Error: el primer octeto debe estar entre 0 y 255.")
    raise SystemExit(1)
if not (0 <= octeto2 <= 255):
    print("Error: el segundo octeto debe estar entre 0 y 255.")
    raise SystemExit(1)
if not (0 <= octeto3 <= 255):
    print("Error: el tercer octeto debe estar entre 0 y 255.")
    raise SystemExit(1)
if not (0 <= octeto4 <= 255):
    print("Error: el cuarto octeto debe estar entre 0 y 255.")
    raise SystemExit(1)

if 0 <= octeto1 <= 127:
    clase = "A"
elif 128 <= octeto1 <= 191:
    clase = "B"
elif 192 <= octeto1 <= 223:
    clase = "C"
elif 224 <= octeto1 <= 239:
    clase = "D"
else:
    clase = "E"

print(f"La dirección IPv4 {octeto1}.{octeto2}.{octeto3}.{octeto4} pertenece a la Clase {clase}.")
