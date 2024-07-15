userReply = input("necesitas enviar un paquete? (Ingresa Si o No)  ")


if userReply == "si":
    print("Podemos ayudarte a enviar tu paquete")
else:
    print("Vuelva cuando necesite enviar un paquete. Gracias.")
    
userReply2 = input("¿Le gustaría comprar sellos, comprar un sobre o hacer una copia? (Ingrese sellos, sobre o copia) ")
    
if userReply2 == "sellos":
    print("Tenemos muchos diseños de sellos para elegir.")
elif userReply2 == "sobre":
    print("Tenemos muchos tamaños de sobres para elegir.")
elif userReply2 == "copia":
    copias = input("¿Cuántas copias quieres? (Ingresa un número)  ")
    print("Aquí hay {} copias".format(copias))
else:
    print("Gracias, por favor venga de nuevo.")