




nota = input("Dame tu calificacion: ")

notaParcial = int(nota[-1])

if notaParcial >= 6:

    nota = int(nota)
    notaFinal = nota + 10 - notaParcial
    print(f"Tu calificacion final es {notaFinal}")
else:
    print("Tu calificacion no amerita redondeo")
   


