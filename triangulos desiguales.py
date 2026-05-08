# Desigualdad Triangular y Pitágoras 📐
# Pide 3 lados y verifica si forman un triángulo válido.
# Si es válido, clasifica en acutángulo, rectángulo u obtusángulo.

print("=== Triángulos Desiguales ===")

try:
    a = float(input("Ingrese el lado a: ").strip())
    b = float(input("Ingrese el lado b: ").strip())
    c = float(input("Ingrese el lado c: ").strip())
except ValueError:
    print("Error: ingrese valores numéricos válidos para los lados.")
    raise SystemExit(1)

if a <= 0 or b <= 0 or c <= 0:
    print("Error: los lados deben ser mayores que cero.")
    raise SystemExit(1)

# Identificar el mayor lado para aplicar Pitágoras correctamente
if a >= b and a >= c:
    mayor = a
    otro1 = b
    otro2 = c
elif b >= a and b >= c:
    mayor = b
    otro1 = a
    otro2 = c
else:
    mayor = c
    otro1 = a
    otro2 = b

# Verificar la desigualdad triangular estricta
if not (otro1 + otro2 > mayor):
    print("Los lados NO forman un triángulo válido.")
    raise SystemExit(0)

# Clasificación mediante Pitágoras y potencias
cuadrado_mayor = pow(mayor, 2)
cuadrado_otros = pow(otro1, 2) + pow(otro2, 2)

if cuadrado_mayor == cuadrado_otros:
    tipo = "Rectángulo"
elif cuadrado_mayor < cuadrado_otros:
    tipo = "Acutángulo"
else:
    tipo = "Obtusángulo"

print(f"Los lados {a}, {b}, {c} forman un triángulo válido.")
print(f"Clasificación: {tipo}.")
