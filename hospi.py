from funciones import menu, ingresar_paciente

while True:
    op = menu()

    match op:
        case 1:
            lista_pacientes=ingresar_paciente()
        case 2:
            print("Buscar ficha")
        case 3:
            print("Buscar medicamentos")
        case 4:
            print("Eliminar ficha")
        case 5:
            print("Listar pacientes")
        case 6:
            print("Has elegido salir. Adiós!")
            break
        case _:
            print("Opción no valida")
            
    