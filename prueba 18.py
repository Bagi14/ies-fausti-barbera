nombre = input("¿Cual es tu nombre? ")
print("Hola", nombre , "Bienvienido al banco")
saldo = float(input("¿Cual es tu saldo? "))
decision = input("¿Que quieres hacer?(ingresar,sacar o pedir un prestamo)")
if decision == "ingresar" :
    sum = float(input("¿cuanto dinero quieres ingresar?"))
    ingr = saldo + sum
    print ("Ahora tienes", str (ingr) , "€")
elif decision == "sacar" :
    sac = float(input("¿Cuanto dinero quieres sacar?"))
    if sac > saldo:
        print ("No se puede realizar esa operacion")
        print ("adios")
    else:
        saca = (saldo - sac)
        print ("Se ha realizado la operación exitosamente")
        print ("ahora dispone de", str (saca), "€ en su cuenta" )
elif decision == "pedir un prestamo":
    prestamo = float(input("¿De cuánto dinero quieres el préstamo? "))
    saldo = saldo + prestamo
    print("Préstamo concedido.")
    print("Ahora dispone de", str(saldo), "€ en su cuenta")
else :
    print ("su saldo es de", str (saldo), "€" ,"/n", "Adios netanyahu" )
