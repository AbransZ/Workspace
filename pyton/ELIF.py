
valor1 = int(input("Ingrese el valor base \n"))
valor2 = int(input("Ingrese la potencia \n"))

potencia = pow(valor1, valor2)

if potencia >=20:
    
        print("el resultado de la potencia es: ", str(potencia))
        
elif potencia>=50:
        
        print("El resultado de la potencia es mayor a 50 y su valor es: ", str(potencia))
       
else:
                print("El resultado es Menor del valor 20 y 50 su valor es: ", str(potencia))