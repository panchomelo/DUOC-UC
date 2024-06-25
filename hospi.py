while True:
    print("1.- Ingresar ficha del paciente")
    print("2.- Buscar ficha por rut")
    print("3.- Buscar medicamentos por rut")
    print("4.- Eliminar ficha del paciente")
    print("5.- Listar pacientes atendidos")
    print("6.- Salir")
    op=int(input("Ingrese una opción valida (1/6)"))

    match op:
        case 1:
            print("ingresar ficha")
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
        case _:
            print("Opción no valida")
    