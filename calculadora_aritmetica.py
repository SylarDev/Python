'''
selectiva_multiple_e.py
script en Python que simula una calculadora con las operaciones aritméticas básicas. El menú mostrado será el siguiente:

1) Suma
2) Resta
3) Multiplicación
4) División
5) División Entera
6) Módulo
7) Potencia

Nota: Primero solicita la opción correspondiente a la operación a realizar y posteriormente solicita los dos operandos como datos enteros.
'''


print("1- Suma")
print ("2- Resta")
print ("3- Multiplicación")
print ("4- División")
print("5- División Entera")
print("6- Módulo")
print("7- Potencia")

operacion = int(input("Qué operación deseas realizar? "))

num1= int(input("Ingresa el primer operando: "))
num2= int(input("Ingresa el segundo operando: "))

if operacion == 1:
    print("SUMA")
    resultado = num1 + num2
    print("El resultado de la suma es: ", resultado)

elif operacion == 2:
    print("RESTA")
    resultado = num1 - num2
    print("El resultado de la resta es: ", resultado)
elif operacion == 3:
    print("MULTIPLCACION")
    resultado = num1 * num2
    print("El resultado de la multiplicacion es: ", resultado)
elif operacion == 4:
    print("DIVISION")
    resultado = num1 / num2
    print("El resultado de la division es: ", float(resultado))
elif operacion == 5:
    print("DIVISION ENTERA")
    resultado = num1 // num2
    print("El resultado de la division es: ", resultado)
elif operacion == 6:
    print("MODULO")
    resultado = num1 % num2
    print("El resultado del modulo es: ", resultado)
else:
    operacion == 7
    print("POTENCIA")
    resultado = num1 ** num2
    print("El resultado de la potencia es: ", resultado)

