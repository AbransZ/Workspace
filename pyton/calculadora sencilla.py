nombre = input("Hola ingrese su nombre: \n")

print("Bienvenido: ", nombre)

op = (input("¿Que operacion desea realizar?\n"))


if op == "suma":

    num1 = int(input("Ingrese primer numero:\n"))
    num2 = int(input("Ingrese segundo numero:\n"))

    print("El resultado es: ", num1+num2)

elif op == "resta":

    num1 = int(input("Ingrese primer numero:\n"))
    num2 = int(input("Ingrese segundo numero:\n"))

    print("El resultado es: ", num1-num2)

elif op == "multiplicacion":

    num1 = int(input("Ingrese primer numero:\n"))
    num2 = int(input("Ingrese segundo numero:\n"))

    print("El resultado es: ", num1*num2)

elif op == "divicion":

    num1 = int(input("Ingrese primer numero:\n"))
    num2 = int(input("Ingrese segundo numero:\n"))

    print("El resultado es: ", num1/num2)

elif op == "division entera":

    num1 = int(input("Ingrese primer numero:\n"))
    num2 = int(input("Ingrese segundo numero:\n"))

    print("El resultado es: ", num1//num2)

elif op == "modulo" or "resto":

    num1 = int(input("Ingrese primer numero:\n"))
    num2 = int(input("Ingrese segundo numero:\n"))

    print("El resultado es: ", num1 % num2)
