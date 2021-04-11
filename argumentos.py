'''
argumentos.py
script en Python que implemente un procedimiento para imprimir un menú
genérico. El procedimiento deberá recibir el título del menú como
primer argumento, seguido de las opciones a imprimir y finalmente un
parámetro con nombre para el mensaje de error en caso de una opción
no válida.
'''

def menu(titulo, *args, **kwargs):
    print(f'                        {titulo}')
    for i in range(len(args)):
        print(f'{i+1}) {args[i]}')
    opc = int(input('Selecciona una opción: '))
    if 1 <= opc <= len(args):
        print(f'Seleccionaste la opción {args[opc-1]}')
    else:
        print('Opción no válida')
        if 'error' in kwargs:
            print(f'{kwargs["error"]}')

menu('Operaciones aritméticas', 'Suma', 'Resta', 'Multiplicación', 
error='No existe tal operación')

print('Nos vemos...')
