import json

def menu():
    print("1.- Ingresar ficha del paciente")
    print("2.- Buscar ficha por rut")
    print("3.- Buscar medicamentos por rut")
    print("4.- Eliminar ficha del paciente")
    print("5.- Listar pacientes atendidos")
    print("6.- Salir")
    op = int(input("Ingrese una opción válida (1/6): "))
    return op


def ingresar_paciente():
    pacientes = []

    while True:
        print("Ingrese los datos del nuevo paciente:")
        nombre_completo=input("Ingrese el nombre completo del paciente ")
        rut=input("Ingrese el rut del paciente ")
        sexo=input("Ingrese el sexo del paciente ")
        diagnostico=input("Ingrese el diagnostico del paciente ")
        print("Ingrese los medicamentos recetados al paciente. Tipea 'FIN' para terminar")

        medicamentos = []
        while True:
            medicamento=input("-Medicamento: ")
            if medicamento.lower() == "fin":
                break
            medicamentos.append(medicamento)

        paciente = {
            'nombre_completo': nombre_completo,
            'rut': rut,
            'sexo': sexo,
            'diagnostico': diagnostico,
            'medicamentos_recetados': medicamentos
        }

        pacientes.append(paciente)

        continuar=input("¿Desea ingresar otro paciente? (S/N): ")
        with open('datos.json', 'w') as archivo:
            json.dump(pacientes, archivo, indent=4)
        if continuar.lower() != 's':
            break

    return pacientes

