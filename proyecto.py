# # Proyecto
saveData = [] # Almacen de registro de usuarios
saveCliente = [] # Almacén de registro de cliente
saveEmpleado = [] # Almacén de registro de empleado
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Sistema de aerolinea')
print('-' * 40)
start = True # Inicio de menú principal
option = 0 # Se declara la variable en 0, para el menú
ticketCode = 0 # Se declara la variable en 0, para mostrar el numero de tiquete

while start: 
    print('Seleccione una opción del menú:')
    print('1. Registro de usuario')
    print('2. Consulta de usuario')
    print('3. Venta de boletos')
    print('4. Salir del programa')
    option = int(input('Su opción es: '))
    print('-' * 40)
    if option == 4:
        print('Salio del programa\nVuelva pronto')
        start = False # Salida del menú principal

    while option != 4: # Salida de menú submenús
        if option == 1: # Apartado de ingreso de usuario
            print('Registro de usuario')
            print('Si desea pasar al menú principal digite "X"')
            print('Digite si es empleado o cliente')
            user = input('- ').upper()
            if user == "X":
                option = 4
                print('-' * 40)
            else:
                if user == 'CLIENTE':
                    fullName = input('Digite su nombre completo: ')
                    iD = int(input('Digite su cedula: '))
                    mail = input('Digite su correo electronico: ')
                    print(user)
                    print(f'Se registro el usuario con exito')
                    print('-' * 40)                
                elif user == 'EMPLEADO':
                    fullName = input('Digite su nombre completo: ')
                    iD = int(input('Digite su cedula: '))
                    mail = input('Digite su correo electrónico: ')
                    print(user)
                    print(f'Se registro el usuario con exito')
                    print('-' * 40)
                else:
                    print('Parametro incorrecto, vuelva a intentar')
                    print('-' * 40)

        elif option == 2: # Apartado de Consulta de usuario
            print('Consultar por usuario')
            print('Si desea pasar al menú principal digite "X"')
            searchId = input('Digite cedula para buscar el usuario: ').upper()
            if searchId == "X":
                option = 4
                print('-' * 40)
            else:
                print(searchId)
        
        elif option == 3: # Apartado de venta de boletos
            print('Venta de boletos')
            print('Si desea pasar al menú principal digite "X"')
            origen = input('Digite de donde esta partiendo: ').upper()
            if origen == 'X':
                option = 4
                print('-' * 40)
            else:
                ticketCode += 1
                destino = input('Digite a donde va: ').upper()
                fecha = input('Digite la fecha en la que va a viajar: ')
                print(seats)
                space = input('Selecione un espacio: ')
                print('Boleto vendido')
                print('-' * 40)
                print('Aquí tiene su factura')
                print(f'Codigo de boleto: {ticketCode}')
                print(f'Origen: {origen}')
                print(f'Destino: {destino}')
                print('Precio: 50$')
     
                print('-' * 40)

        
        else:
            print('Opcion incorrecta\nintente de nuevo')
            option = 4
            print('-' * 40)
