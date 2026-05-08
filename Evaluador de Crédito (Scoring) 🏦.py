# Evaluador de Crédito (Scoring) 🏦
# Pide ingresos, deudas, edad y morosidad. Ajusta puntos y decide aprobar o denegar.

print("=== Evaluador de Crédito ===")

try:
    ingresos = float(input("Ingrese ingresos mensuales: ").strip())
    deudas = float(input("Ingrese el monto de deudas: ").strip())
    edad = int(input("Ingrese la edad: ").strip())
    morosidad = int(input("Ingrese cantidad de moras en el historial: ").strip())
except ValueError:
    print("Error: ingrese valores numéricos válidos para ingresos, deudas, edad y morosidad.")
    raise SystemExit(1)

if ingresos < 0 or deudas < 0 or edad <= 0 or morosidad < 0:
    print("Error: los valores no pueden ser negativos y la edad debe ser mayor a cero.")
    raise SystemExit(1)

puntos = 50

# Evaluación de ingresos
if ingresos >= 3000:
    puntos += 30
if 2000 <= ingresos < 3000:
    puntos += 20
if 1000 <= ingresos < 2000:
    puntos += 10
if ingresos < 1000:
    puntos -= 10

# Evaluación de deudas
if deudas == 0:
    puntos += 20
if 0 < deudas <= 1000:
    puntos += 5
if 1000 < deudas <= 5000:
    puntos -= 10
if deudas > 5000:
    puntos -= 25

# Evaluación de edad
if 25 <= edad <= 65:
    puntos += 20
if edad < 25:
    puntos -= 10
if edad > 65:
    puntos -= 15

# Evaluación de morosidad
if morosidad == 0:
    puntos += 15
if 1 <= morosidad <= 2:
    puntos -= 10
if morosidad > 2:
    puntos -= 30

print("\n=== Resultado de Scoring ===")
print(f"Puntos totales: {puntos}")

if puntos >= 60:
    print("Crédito aprobado.")
else:
    print("Crédito denegado.")
