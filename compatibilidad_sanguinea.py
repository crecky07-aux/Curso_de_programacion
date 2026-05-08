# Compatibilidad Sanguínea 🩸
# Pide grupo y factor de donante y receptor.
# Determina si la transfusión es segura usando if-elif anidados.

print("=== Compatibilidad Sanguínea ===")
print("Grupos disponibles: A, B, AB, O")
print("Factores disponibles: +, -")

grupo_donante = input("Ingrese el grupo del donante: ").strip().upper()
factor_donante = input("Ingrese el factor del donante (+/-): ").strip()
grupo_receptor = input("Ingrese el grupo del receptor: ").strip().upper()
factor_receptor = input("Ingrese el factor del receptor (+/-): ").strip()

valid_grupos = {"A", "B", "AB", "O"}
valid_factores = {"+", "-"}

if grupo_donante not in valid_grupos:
    print("Grupo de donante inválido.")
    raise SystemExit(1)
if grupo_receptor not in valid_grupos:
    print("Grupo de receptor inválido.")
    raise SystemExit(1)
if factor_donante not in valid_factores:
    print("Factor del donante inválido.")
    raise SystemExit(1)
if factor_receptor not in valid_factores:
    print("Factor del receptor inválido.")
    raise SystemExit(1)

compatible = False

# Compatibilidad ABO mediante if-elif anidados
if grupo_donante == "O":
    compatible = True
elif grupo_donante == "A":
    if grupo_receptor == "A" or grupo_receptor == "AB":
        compatible = True
    else:
        compatible = False
elif grupo_donante == "B":
    if grupo_receptor == "B" or grupo_receptor == "AB":
        compatible = True
    else:
        compatible = False
elif grupo_donante == "AB":
    if grupo_receptor == "AB":
        compatible = True
    else:
        compatible = False

# Compatibilidad Rh con condición adicional
if compatible:
    if factor_receptor == "+":
        compatible = True
    else:
        if factor_donante == "-":
            compatible = True
        else:
            compatible = False

print("\n=== Resultado ===")
if compatible:
    print("Transfusión segura: compatible.")
else:
    print("Transfusión NO segura: incompatibilidad detectada.")
