import json
import numpy as np
global matriz

def menu():
    print("¿Qué opción desea realizar?")
    print("1.- Ingresar ficha del paciente")
    print("2.- Buscar ficha del paciente")
    print("3.- Buscar medicamentos recetados")
    print("4.- Eliminar ficha del paciente")
    print("5.- Listar pacientes ingresados")
    print("6.- Para salir y actualizar pacientes")
    op = int(input("Ingrese una opción válida (1/6): "))
    return op


def es_numero(valor):
    return isinstance(valor, (int, float))


def ingresar_paciente(matriz):
    while True:
        fila_vacia = None

        for i in range(matriz.shape[0]):
            if matriz[i][0] is None or matriz[i][0] == "":
                fila_vacia = i
                break

        if fila_vacia is None:
            print("No hay filas vacías para ingresar nuevos pacientes.")
            return matriz  # Retorna matriz sin cambios si no hay filas vacías
        
        print()
        nombre_completo = input("Ingrese el nombre completo del paciente: ")
        rut = input("Ingrese el rut del paciente: ")
        sexo = input("Ingrese el sexo del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        fono = input("Ingrese el fono del paciente: ")
        diagnostico = input("Ingrese el diagnóstico del paciente: ")
        medicamento = input("Ingrese el medicamento recetado: ")
        
        if nombre_completo == "" or rut == "" or sexo == "" or edad == "" or fono == "" or diagnostico == "" or medicamento == "":
            print("Error: Todos los campos deben ser ingresados. No se permiten campos vacíos.")
            print("Por favor, vuelva a intentarlo.")
            continue  # Vuelve al inicio del bucle para pedir los datos nuevamente
        
        # Ingresar los datos del paciente en la fila vacía encontrada
        matriz[fila_vacia] = [nombre_completo, rut, sexo, edad, fono, diagnostico, medicamento]
        print()
        print("Paciente ingresado con éxito en la fila", fila_vacia)

        respuesta = input("¿Desea ingresar otro paciente? (si/no): ")
        print()
        if respuesta.lower() != 'si':
            break

    return matriz  # Retorna la matriz global modificada


def buscar_paciente(rut, matriz):
    encontrado=False
    for paciente in matriz:
        if paciente[1] == rut:
            encontrado=True
            print()
            print("Datos del paciente:")
            print(f"Nombre completo: {paciente[0]}")
            print(f"RUT: {paciente[1]}")
            print(f"Sexo: {paciente[2]}")
            print(f"Edad: {paciente[3]}")
            print(f"Fono: {paciente[4]}")
            print(f"Diagnóstico: {paciente[5]}")
            print(f"Medicamento: {paciente[6]}")
            print()

    if not encontrado:
        print(f"No se encontró ningún paciente con el RUT {rut}")
        print()


def buscar_medicamento(rut, matriz):
    encontrado=False
    for paciente in matriz:
        if paciente[1] == rut:
            encontrado=True
            print()
            print(f"El medicamento recetado para el paciente {paciente[0]} es {paciente[6]}")
            print()

    if not encontrado:
        print(f"No se encontró ningún paciente con el RUT {rut}")
        print()


def eliminar_paciente(rut, matriz):
    encontrado = False
    nombre_paciente = None

    for i in range(matriz.shape[0]):
        if matriz[i, 1] == rut:
            encontrado = True
            nombre_paciente = matriz[i, 0]  # matriz[i, 0] es el campo del nombre en la matriz
            print(f"Eliminando paciente {nombre_paciente} con rut {rut}")
            matriz = np.delete(matriz, i, axis=0)
            print("Paciente eliminado correctamente.")
            print()
            break

    if not encontrado:
        print(f"No se encontró ningún paciente con el RUT {rut}")
        print()
    else:
        return matriz
    

def listar_pacientes(matriz):
    print()
    print("Listado de pacientes:")
    print()
    for paciente in matriz:
        if paciente[0] is not None and paciente[0] != "":
            print(f"{paciente[0]}, {paciente[1]}, {paciente[2]}, {paciente[3]}, {paciente[4]}, {paciente[5]}, {paciente[6]}")
            print()
        else:
            break



