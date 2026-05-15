num = int(input("Ingrese un número: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")
else:
    print("No es primo")