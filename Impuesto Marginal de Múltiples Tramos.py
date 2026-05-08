# Impuesto Marginal de Múltiples Tramos 💸
# Calcula el impuesto real en tramos: 0-10k(0%), 10-30k(15%), 30-60k(25%), >60k(35%).

print("=== Impuesto Marginal ===")

try:
    ingreso = float(input("Ingrese el ingreso imponible: ").strip())
except ValueError:
    print("Error: ingrese un valor numérico válido para el ingreso.")
    raise SystemExit(1)

if ingreso < 0:
    print("Error: el ingreso no puede ser negativo.")
    raise SystemExit(1)

impuesto = 0.0
tramo = 0.0
restante = ingreso

# Primer tramo: 0-10k a 0%
if restante > 10000:
    tramo = 10000
    restante -= tramo
else:
    tramo = restante
    restante = 0.0
impuesto += tramo * 0.0

# Segundo tramo: 10-30k a 15%
if restante > 20000:
    tramo = 20000
    restante -= tramo
else:
    tramo = restante
    restante = 0.0
impuesto += tramo * 0.15

# Tercer tramo: 30-60k a 25%
if restante > 30000:
    tramo = 30000
    restante -= tramo
else:
    tramo = restante
    restante = 0.0
impuesto += tramo * 0.25

# Cuarto tramo: monto restante > 60k a 35%
tramo = restante
impuesto += tramo * 0.35

print(f"\nIngreso imponible: ${ingreso:,.2f}")
print(f"Impuesto total:     ${impuesto:,.2f}")
print(f"Ingreso neto:       ${ingreso - impuesto:,.2f}")
