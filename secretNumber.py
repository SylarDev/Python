


import random
import time


numeroSecreto = random.randint(1, 1000)

print("Acabo de elegir un numero entre el 1 y el 1000. /n eres capas de adivinarlo?")
print(numeroSecreto)
numero = int(input("Ingresa tu numero: "))

if numero == numeroSecreto:
    print("Logro desbloqueado: Adivino mistico")
    time.sleep(3)
    print("Follow the white rabbit or diee")
    
else: print("Tu numero no es el correcto, sigue participando...")





    