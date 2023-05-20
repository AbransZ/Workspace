print("Bienvenido a su gestion de dias libres\n\n")

nombre = input("ingrese su nombre\n")
clave = int(input("Ingrese su clave de departamento\n"))
anti = int(input("Ingrese sus años de antiguedad "))

if clave == 1:

    print("Bienvenido Sr/a", nombre,
          " su clave es de nivel servicio al cliente\n\n")

    if anti == 1:
        print("Sr/a", nombre, " Le corresponden 6 dias de vacaciones")
    elif anti >= 2 and anti <= 6:
        print("Sr/a", nombre, " Le corresponden 14 dias de Vacaciones")
    elif anti >= 7:
        print("Sr/a", nombre, " Le corresponden 20 dias de vacaciones")
    else:
        print("Sr/a", nombre, " No cumple con el tiempo suficiente para obtener vacaciones el minimo es 1 año entero laborado")
elif clave == 2:

    print("Bienvenido Sr/a", nombre, " su clave es de nivel Logistica\n\n")

    if anti == 1:
        print("Sr/a", nombre, " Le corresponden 7 dias de vacaciones")
    elif anti >= 2 and anti <= 6:
        print("Sr/a", nombre, " Le corresponden 15 dias de Vacaciones")
    elif anti >= 7:
        print("Sr/a", nombre, "Le corresponden 22 dias de vacaciones")
    else:
        print("Sr/a", nombre, " No cumple con el tiempo suficiente para obtener vacaciones el minimo es 1 año entero laborado")
elif clave == 3:

    print("Bienvenido Sr/a", nombre, "su clave es de nivel Gerencia\n\n")

    if anti == 1:
        print("Sr/a", nombre, " Le corresponden 10 dias de vacaciones")
    elif anti >= 2 and anti <= 6:
        print("Sr/a", nombre, " Le corresponden 20 dias de Vacaciones")
    elif anti >= 7:
        print("Sr/a", nombre, " Le corresponden 30 dias de vacaciones")
    else:
        print("Sr/a", nombre, " No cumple con el tiempo suficiente para obtener vacaciones el minimo es 1 año entero laborado")
else:
    print("Disculpe Sr/a", nombre, " su Clave es invalida")
