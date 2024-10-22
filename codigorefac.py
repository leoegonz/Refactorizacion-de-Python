def ingresar_puntuacion_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()

        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post} \n')
                print("Puntuación y comentario guardados correctamente.")
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", 'r') as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("No hay datos guardados todavía.")

def finalizar():
    print('Programa finalizado')
    exit()

def menu():
    while True:
        #print('Seleccione el proceso que desea aplicar:') //cambio de lugar porque esta feo arriba
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora')
        print('3: Finalizar')
        print('Seleccione el proceso que desea aplicar:')

        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                finalizar()
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

# Ejecutar el menú
menu()
