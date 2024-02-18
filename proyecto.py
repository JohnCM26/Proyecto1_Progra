# # Proyecto
almacenDatos = [] # Aquí se guardara el registro de los usuarios

print('Sistema de aerolinea')
print('-' * 40)
print()

inicio = True # Inicio de menú principal
opcion = 0
while inicio:
    print('Seleccione una opción del menú:')
    print('1. Registrar usuario')
    print('2. Consultar usuario')
    print('3. Salir del programa')
    opcion = int(input('Su opción es: '))
    print('-' * 40)
    if opcion == 3:
        print('Salio del programa\nVuelva pronto')
        inicio = False

    while opcion != 3:
        if opcion == 1: # Apartado de ingreso de usuario
            print('Registro de usuario')
            print()
            print('- Digite si es empleado o cliente -')
            print('Si desea pasar al menú principal digite "X"')
            user = input('- ').upper()
            if user == "X":
                opcion = 3
                print()
            else:
                fullName = input('Digite su nombre completo: ')
                iD = int(input('Digite su cedula: '))
                print(f'Se registro el usuario con exito')
                print('-' * 40)                
                
        elif opcion == 2:
            print('Consultar por usuario')
            print('Si desea pasar al menú principal digite "X"')
            