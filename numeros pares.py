print("Calcular Numeros Pares\n\n")
num = int(input("ingresar numero "))

resultado = num % 2

if resultado == 0:
    print("\n\nel numero", num, " es par")
else:
    print("\n\nEl numero ", num, " es impar")
