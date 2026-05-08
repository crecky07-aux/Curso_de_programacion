# Validación Completa de Fecha 📅
# Pide día, mes y año y verifica si la fecha es real incluyendo meses de 30/31 días y años bisiestos.

print("=== Validación Completa de Fecha ===")

try:
    dia = int(input("Ingrese el día: ").strip())
    mes = int(input("Ingrese el mes: ").strip())
    anio = int(input("Ingrese el año: ").strip())
except ValueError:
    print("Error: ingrese valores enteros para día, mes y año.")
    raise SystemExit(1)

if anio < 1:
    print("Error: el año debe ser positivo.")
    raise SystemExit(1)

if mes < 1 or mes > 12:
    print("Error: el mes debe estar entre 1 y 12.")
    raise SystemExit(1)

# Determinar si es año bisiesto
es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Días por mes con febrero variable
if mes == 2:
    dias_mes = 29 if es_bisiesto else 28
elif mes in {4, 6, 9, 11}:
    dias_mes = 30
else:
    dias_mes = 31

if dia < 1 or dia > dias_mes:
    print(f"Error: la fecha {dia}/{mes}/{anio} no es válida.")
    raise SystemExit(0)

print(f"La fecha {dia}/{mes}/{anio} es válida.")
