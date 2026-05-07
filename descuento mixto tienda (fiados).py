
categoria = input("ingrese la categoría del producto (Electronica o Ropa): ").strip().lower().replace("é", "e")
cantidad = int(input("ingrese la cantidad comprada: "))
precio_unitario = float(input("ingrese el precio unitario: "))

subtotal = cantidad * precio_unitario

descuento = 0
if categoria == "electronica" and cantidad >= 3:
    descuento = subtotal * 0.10
elif categoria == "ropa" and cantidad >= 5:
    descuento = subtotal * 0.15

total = subtotal - descuento

print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Total a pagar: ${total:.2f}")
