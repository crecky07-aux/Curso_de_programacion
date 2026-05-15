a = int(input("Número 1: "))
b = int(input("Número 2: "))
while b != 0:
    a, b = b, a % b
print(f"MCD: {a}")