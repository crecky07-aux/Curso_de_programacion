# Calculadora Logística 🚚
# Costos base por zona, recargo 50% por peso, tarifa fija por volumen,
# y descuento premium aplicado al final.

zona_costos = {
    "1": 2500,
    "2": 3400,
    "3": 4600,
}

recargo_peso_porcentaje = 0.50
tarifa_volumen = 1200.0
porcentaje_descuento_premium = 0.10

print("=== Calculadora Logística ===")
print("Zonas disponibles:")
print("  1 - Zona local")
print("  2 - Zona regional")
print("  3 - Zona nacional")

zona = input("Ingrese la zona de envío (1, 2 o 3): ").strip()
if zona not in zona_costos:
    print("Zona inválida. Use 1, 2 o 3.")
    raise SystemExit(1)

try:
    peso = float(input("Ingrese el peso en kg: ").strip())
    volumen = float(input("Ingrese el volumen en m3: ").strip())
except ValueError:
    print("Peso o volumen inválido. Ingrese números válidos.")
    raise SystemExit(1)

if peso <= 0 or volumen <= 0:
    print("El peso y el volumen deben ser mayores que cero.")
    raise SystemExit(1)

premium_input = input("¿Cliente premium? (s/n): ").strip().lower()
premium = premium_input in ("s", "si", "sí", "y", "yes")

# Jerarquía estricta de actualización de variables matemáticas
costo_base = zona_costos[zona]
recargo_peso = costo_base * recargo_peso_porcentaje * peso
costo_volumen = volumen * tarifa_volumen
subtotal = costo_base + recargo_peso + costo_volumen

descuento_premium = subtotal * porcentaje_descuento_premium if premium else 0.0
costo_total = subtotal - descuento_premium

print("\n=== Desglose de costos ===")
print(f"Costo base por zona:       ${costo_base:,.2f}")
print(f"Recargo por peso (50%):    ${recargo_peso:,.2f}")
print(f"Tarifa fija por volumen:   ${costo_volumen:,.2f}")
print(f"Subtotal antes de descuento: ${subtotal:,.2f}")
if premium:
    print(f"Descuento premium (10%):   -${descuento_premium:,.2f}")
print(f"Costo total de envío:      ${costo_total:,.2f}")
