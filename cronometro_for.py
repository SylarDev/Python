

import os, time

hora = 23
minutos = 60
segundos = 60

for hor in range(-1, hora, 1):
    hora = hor + 1
    for mini in range(-1, minutos, 1):
        minutos = mini + 1
        for seg in range(0, segundos, 1):
            time.sleep(1)
            print(f"{hora}:{minutos}:{seg}")

            #os.system("clear")
    
print("Listoo")    
