# Reloj con Adición de Segundos ⏱️
# Pide HH:MM:SS y segundos a sumar. Calcula la nueva hora exacta en formato 24h sin bucles.

print("=== Reloj con Adición de Segundos ===")

hora_str = input("Ingrese la hora actual (HH:MM:SS): ").strip()
segundos_sumar_str = input("Ingrese segundos a sumar: ").strip()

try:
    partes = hora_str.split(":")
    if len(partes) != 3:
        raise ValueError
    horas = int(partes[0])
    minutos = int(partes[1])
    segundos = int(partes[2])
    segundos_sumar = int(segundos_sumar_str)
except ValueError:
    print("Error: formato inválido. Use HH:MM:SS y un entero para segundos.")
    raise SystemExit(1)

if not (0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59):
    print("Error: la hora debe ser HH entre 0 y 23, MM y SS entre 0 y 59.")
    raise SystemExit(1)

segundos_totales = horas * 3600 + minutos * 60 + segundos + segundos_sumar
segundos_totales_mod = segundos_totales % 86400

nuevas_horas = segundos_totales_mod // 3600
nuevos_minutos = (segundos_totales_mod % 3600) // 60
nuevos_segundos = segundos_totales_mod % 60

print(f"\nHora nueva: {nuevas_horas:02d}:{nuevos_minutos:02d}:{nuevos_segundos:02d}")
