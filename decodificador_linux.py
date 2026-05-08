# Decodificador de Permisos Linux (chmod) 🐧
# Pide un número de 0 a 7 y muestra los permisos que representa.

print("=== Decodificador chmod ===")

try:
    permiso = int(input("Ingrese un número entre 0 y 7: ").strip())
except ValueError:
    print("Error: debe ingresar un número entero entre 0 y 7.")
    raise SystemExit(1)

if permiso < 0 or permiso > 7:
    print("Error: el número debe estar entre 0 y 7.")
    raise SystemExit(1)

lectura = bool(permiso & 4)
escritura = bool(permiso & 2)
ejecucion = bool(permiso & 1)

print("\nPermisos para", permiso)
print("  Lectura:   ", "Sí" if lectura else "No")
print("  Escritura: ", "Sí" if escritura else "No")
print("  Ejecución: ", "Sí" if ejecucion else "No")
