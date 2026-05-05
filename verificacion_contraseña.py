
contraseña = input("Ingresa tu nueva contraseña: ")

if len(contraseña) >= 9:
    print("Usted tiene una contraseña segura, felicidades :D")
else:
    print("Contraseña insegura. Debe tener al menos 9 caracteres.")