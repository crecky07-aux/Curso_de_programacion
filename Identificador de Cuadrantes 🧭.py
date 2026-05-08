# Identificador de Cuadrantes 🧭
# Pide coordenadas (x, y) y determina el cuadrante o si está sobre los ejes/origen.

print("=== Identificador de Cuadrantes ===")

try:
    x = float(input("Ingrese la coordenada x: ").strip())
    y = float(input("Ingrese la coordenada y: ").strip())
except ValueError:
    print("Error: ingrese valores numéricos para x e y.")
    raise SystemExit(1)

if x == 0.0 and y == 0.0:
    ubicacion = "Origen"
elif x == 0.0 and y != 0.0:
    ubicacion = "Eje Y"
elif y == 0.0 and x != 0.0:
    ubicacion = "Eje X"
elif x > 0.0 and y > 0.0:
    ubicacion = "Cuadrante I"
elif x < 0.0 and y > 0.0:
    ubicacion = "Cuadrante II"
elif x < 0.0 and y < 0.0:
    ubicacion = "Cuadrante III"
elif x > 0.0 and y < 0.0:
    ubicacion = "Cuadrante IV"
else:
    ubicacion = "Ubicación desconocida"

print(f"La coordenada ({x}, {y}) está en: {ubicacion}.")
