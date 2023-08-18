nombreUsuario = input("Nombre de Usuario: ")
edadUsuario = int(input("Edad de usuario: "))

if  edadUsuario>=0 and edadUsuario <= 15:
    print(f"querido {nombreUsuario}, usted es un niño")
elif edadUsuario >15 and edadUsuario<=28:
    print(f"querido {nombreUsuario}, usted es un joven")
elif edadUsuario>28 and edadUsuario<=60:
    print(f"querido {nombreUsuario}, usted es un adulto")
elif edadUsuario>60 and edadUsuario<=120:
    print(f"querido{nombreUsuario}, usted es un adulto mayor")
else:
    print("Edad invalida")