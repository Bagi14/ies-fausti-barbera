print("Bienvenido a la gasolinera Python")
print("¿Que desea Hacer?")
dinero=int(input("cuanto dinero tienes"))
print("1 Repostar Gasolina 1,50 L")
print("2 Comprar un lavado de coche 8$")
print("3 Añadir dinero ")
opc=input("selecciona una opcion 1 ,2 0 3")
if opc == "1":
    gasolina = float(input("cuanta gasolina quieres: "))
    litros = 1.5 * gasolina

    if litros > dinero:
        print("no hay suficiente dinero")
    else:
        dinero = dinero - litros
        print("Repostaje realizado")
elif opc == "2":
    if dinero < 8:
        print("no hay suficiente dinero")
    else:
        dinero = dinero - 8
        print("lavado comenzado ")
elif opc == "3":
    ff=float(input("cuanto dinero quieres añadir"))
    dinero = dinero + ff
    print("dinero añadido correctamente")
else:
    print("opcion no valida")
print("su saldo actual es",dinero)
print("gracias por venir")
      

    


