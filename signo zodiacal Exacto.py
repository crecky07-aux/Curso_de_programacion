# Signo Zodiacal Exacto ♈
# Pide día y mes, valida valores y determina el signo según límites exactos.

print("=== Signo Zodiacal Exacto ===")

try:
    dia = int(input("Ingrese el día de nacimiento: ").strip())
    mes = int(input("Ingrese el mes de nacimiento (1-12): ").strip())
except ValueError:
    print("Error: ingrese números enteros para día y mes.")
    raise SystemExit(1)

if mes < 1 or mes > 12:
    print("Error: el mes debe estar entre 1 y 12.")
    raise SystemExit(1)

dias_mes = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

if dia < 1 or dia > dias_mes[mes]:
    print(f"Error: el mes {mes} no tiene {dia} días.")
    raise SystemExit(1)

signo = ""

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricornio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Piscis"
else:
    signo = "Desconocido"

print(f"El signo zodiacal para {dia}/{mes} es: {signo}.")
