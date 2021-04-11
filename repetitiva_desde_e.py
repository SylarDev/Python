'''
repetitiva_desde_e.py
script en Python que muestre un cronómetro en formato de 24 horas.
El despliegue seguirá el formato h:m:s. El cronómetro deberá iniciar
en 0:0:0 y podrá llegar hasta 23:59:59. Implementar retardos de
1 segundo y limpieza de pantalla de forma tal que sólo se vea un
tiempo en pantalla.
'''
import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system('clear')
            print(f'{hora}:{minuto}:{segundo}')
            time.sleep(1)
