print("Comprarador de numeros")

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("\n\nIngrese el segundo numero"))
num3 = int(input("\n\nIngrese el tercer numero"))

if num1 > num2 and num1 > num3:
    print("\n\nEl numero ", num1, " es mayor entre los 3 numeros")
elif num2 > num1 and num2 > num3:
    print("\n\nEl numero ", num2, " es mayor entre los 3 numeros")
else:
    print("\n\nEl numero ", num3, " es mayor entre los 3 numeros")
