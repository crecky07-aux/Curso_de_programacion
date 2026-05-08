# Colisión de cajas
# Pide coordenadas inferiores y superiores de dos rectángulos.
# Determina si se chocan (superponen) en el plano.

print("=== Colisión de cajas ===")
print("Ingrese las coordenadas del primer rectángulo:")

try:
    r1_x1 = float(input("  x inferior izquierdo 1: ").strip())
    r1_y1 = float(input("  y inferior izquierdo 1: ").strip())
    r1_x2 = float(input("  x superior derecho 1: ").strip())
    r1_y2 = float(input("  y superior derecho 1: ").strip())

    print("\nIngrese las coordenadas del segundo rectángulo:")
    r2_x1 = float(input("  x inferior izquierdo 2: ").strip())
    r2_y1 = float(input("  y inferior izquierdo 2: ").strip())
    r2_x2 = float(input("  x superior derecho 2: ").strip())
    r2_y2 = float(input("  y superior derecho 2: ").strip())
except ValueError:
    print("Error: por favor ingrese valores numéricos para las coordenadas.")
    raise SystemExit(1)

if not (r1_x1 < r1_x2 and r1_y1 < r1_y2):
    print("Error: el primer rectángulo tiene coordenadas inválidas.")
    raise SystemExit(1)
if not (r2_x1 < r2_x2 and r2_y1 < r2_y2):
    print("Error: el segundo rectángulo tiene coordenadas inválidas.")
    raise SystemExit(1)

# Cruce de coordenadas usando and, <, >
no_colision_horizontal = (r1_x2 <= r2_x1) or (r2_x2 <= r1_x1)
no_colision_vertical = (r1_y2 <= r2_y1) or (r2_y2 <= r1_y1)

if no_colision_horizontal or no_colision_vertical:
    print("Los rectángulos NO se superponen.")
else:
    print("Los rectángulos SE superponen.")
