import random


paises = ["Antigua y Barbuda", "Argentina", "Bahamas", "Barbados", "Belice", "Bolivia", "Brasil", "Canada", "Chile",
            "Colombia", "Costa Rica", "Cuba", "Republica Dominicana", "Ecuador", "El Salvador", "Estados Unidos", 
            "Granada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", 
            "Paraguay", "Peru", "San Cristobal y Nieves", "San Vicente y las Granadinas", 
            "Santa Lucia", "Surinam", "Trinidad y Tobago", "Uruguay", "Venezuela"]

palabraAux = random.choice(paises)
palabra = palabraAux.lower()

print(palabra)

print(f"La palabra tiene {len(palabra)} letras...")
contador = 0
oportunidades = 5
letra = input("Adivina una letra: ")
letraRepetida = []

while contador < 4:
    print(palabra)
    if palabra.find(letra) == -1:
        if letra in letraRepetida:
            print("Ya elegiste esa letra...")
        print("La letra no esta en la palabra...")
        contador += 1
        
        #letraRepetida.append(letra)
        print(f"Te quedan {oportunidades - contador} oportunidades...")
        
    elif palabra.find(letra):
        
        if letra in letraRepetida:
            print("Ya elegiste esa letra...")
            contador += 1
            print(f"Te quedan {oportunidades - contador} oportunidades...")
        
        indiceLetra = palabra.index(letra)
        print(f"La letra aparece {palabra.count(letra)} veces")
        print(f"la letra esta en la posicion {indiceLetra}")
        #letraRepetida.append(letra)
        
    letraRepetida.append(letra)
    print(letraRepetida)
    
    letra = input("Adivina otra letra: ")


