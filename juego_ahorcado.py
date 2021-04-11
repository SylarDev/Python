'''
listas_e.py
script en Python que implemente el clásico juego de "ahorcado".
El juego consiste en que el usuario intente adivinar una palabra
secreta de la cual inicialmente sólo se le muestra la cantidad
de letras que contiene. Para esta versión del juego, el usuario
deberá intentar adivinar el nombre de alguno de los 35 países
con conforman el continente americano.

El juego debe comenzar seleccionando de forma aleatoria el
nombre de alguno de los países; dichos nombres deberán estar
almacenados en una lista. Una vez seleccionado el país, se le
mostrará al usuario una cadena formada por tantos guiones bajos
como letras y espacios en blanco haya en el nombre del país.
por ejemplo si el país es "Cuba", al usuario se le mostraría
"____" (4 guiones bajos).

A partir de ahí el usuario debe intentar adivinar las letras
que conforman el nombre teniendo hasta 5 oportunidades para
fallar. Si el usuario propone una letra y existe en el nombre
del país, entonces todas las ocurrencias de esa letra se
reemplazan en la palabra secreta; por ejemplo para la palabra
"Cuba", si el usuario propusiera la "a" entonces la palabra
secreta se actualizaría para mostrar "___a".

El juego termina si se han descubierto todas las letras del
nombre o el usuario se ha equivocado 6 veces.
'''
import random
import os

paises = ["Antigua y Barbuda", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canada", "Chile",
            "Colombia", "Costa Rica", "Cuba", "Ecuador", "El Salvador", "Estados Unidos", 
            "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", 
            "Paraguay", "Peru", "Republica Dominicana", "San Cristobal y Nieves", "San Vicente y las Granadinas", 
            "Santa Lucia", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]

def menu():
    print("""            Bienvenido al juego del Ahorcado...

            Deberas adivinar el pais de América que te toque...

            Para ello contarás con 5 oportunidades para adivinar la palabra...

            Suerte!!!!
    
    """)
    input("Presiona ENTER para comenzar....")


def paisAleatorio(paises):
    return random.choice(paises)
     

def game():
    pass


def main(pais):
    
    menu()
    print(f"La palabra tiene {len(pais)} letras")
    input()
    






if __name__ == "__main__":
    main(paisAleatorio(paises))
    
