"""
script en Python que implemente un programa para realizar las siguientes
conversiones:
 - segundos a minutos: recibe segundos y devuelve minutos y segundos
 - segundos a horas: recibe segundos y regresa horas, minutos y segundos
 - minutos a segundos: recibe minutos y segundos y regresa segundos
 - minutos a horas: recibe minutos y segundos y regresa horas minutos y
   segundos
Además deberá implementarse un método para imprimir el menú de opciones
y la ejecución del programa debe comenzar desde el procedimiento "main".
El programa debe seguir en ejecución mientras el usuario no decida
salir.
"""



def segundos_a_minutos(segundos):
    minus = segundos / 60
    seg = segundos % 60
    if segundos < 60:
        minus = 0
        
    return minus, seg


def segundos_a_horas(segundos):
    hor = segundos / 3600
    minus = segundos / 60
    seg = segundos % 60
    return hor, minus, seg

def minutos_a_segundos(minutos, segundos):
    minus = minutos * 60
    seg = segundos % 60
    total = minus + seg

    return total

def minutos_a_horas(minutos, segundos):
    hor = minutos / 60
    minus = minutos % 60
    seg = minus % 60
    if minutos == 60 and segundos == 0:
        hor = 1
        minus = 0
    
    
    return hor, minus, seg


SEG_A_MIN = 1
SEG_A_HOR = 2
MIN_A_SEG = 3
MIN_A_HOR = 4 
SALIR = 5

def main():
    print(f"""Operaciones: 
        
        {SEG_A_MIN} Segundos a minutos.
        {SEG_A_HOR} Segundos a horas. 
        {MIN_A_SEG} Minutos a segundos. 
        {MIN_A_HOR} Minutos a horas. 
        {SALIR} Salir
    """)

    opcion = int(input("¿Que operacion deseas realizar?: "))
    while opcion != SALIR:
        if opcion == SEG_A_MIN:
            print("Haz elegido convertir Segundos a minutos...")
            segundos = int(input("Ingresa los segundos: "))
            min, seg = segundos_a_minutos(segundos)
            print(f"Los minutos son: {min} minutos : {seg} segundos")
            
        elif opcion == SEG_A_HOR:
            print("Haz elegido convertir segundos a horas.")
            segundos = int(input("Ingresa los segundos: "))
            hor, min, seg = segundos_a_horas(segundos)
            print(f"Las horas son: {hor:.2f} horas")
            
        elif opcion == MIN_A_SEG:
            print("Haz elegido convertir minutos a segundos.")
            minutos = int(input("Ingresa los minutos: "))
            segundos = int(input("Ingresa los segundos: "))
            seg = minutos_a_segundos(minutos,segundos)
            print(f"Los segundos son: {seg} segundos")
             
        elif opcion == MIN_A_HOR:
             print("Haz elegido convertir minutos a horas.")
             minutos = int(input("Ingresa los minutos: "))
             segundos = int(input("Ingresa los segundos: "))
             hor, min, seg = minutos_a_horas(minutos,segundos)
             print(f"Las horas son: {hor:.0f} horas :{min} minutos :{seg} segundos ")
             
        print(f"""Operaciones: 
        
        {SEG_A_MIN} Segundos a minutos.
        {SEG_A_HOR} Segundos a horas. 
        {MIN_A_SEG} Minutos a segundos. 
        {MIN_A_HOR} Minutos a horas. 
        {SALIR} Salir
        """)

        opcion = int(input("¿Que operacion deseas realizar?: "))


    print("Done...!!!")
    



if __name__ == "__main__":
    main()