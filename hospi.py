from funciones import menu, ingresar_paciente, buscar_paciente, buscar_medicamento, eliminar_paciente, listar_pacientes
import json, os
import numpy as np

matriz = np.empty((50, 7), dtype=object)

if os.path.exists('usuarios.json'):
    with open('usuarios.json', 'r') as file:
        json_usuarios = json.load(file)

    for i, usuario in enumerate(json_usuarios):
        matriz[i, 0] = usuario['nombre_completo']
        matriz[i, 1] = usuario['rut']
        matriz[i, 2] = usuario['sexo']
        matriz[i, 3] = usuario['edad']
        matriz[i, 4] = usuario['fono']
        matriz[i, 5] = usuario['diagnostico']
        matriz[i, 6] = usuario['medicamento']

while True:
    op = menu()

    match op:
        case 1:
            matriz=ingresar_paciente(matriz) 
            #captura y actualiza la matriz global
        case 2:
            print()
            rut_input=input("Ingrese el rut del paciente que desea buscar ")
            buscar_paciente(rut_input, matriz)
        case 3:
            print()
            rut_input=input("Ingresa el rut del paciente ")
            buscar_medicamento(rut_input, matriz)
        case 4:
            print()
            rut_input=input("Ingresa el rut del paciente que deseas eliminar ")
            matriz=eliminar_paciente(rut_input, matriz)
        case 5:
            listar_pacientes(matriz)
        case 6:
            print("Has elegido salir. Adiós!")
            break
        case _:
            print("Opción no valida")

diccionario_pacientes = []

for paciente in matriz:
    if None in paciente:
        continue
    
    paciente_dict = {
    "nombre_completo": paciente[0],
    "rut": paciente[1],
    "sexo": paciente[2],
    "edad": paciente[3],
    "fono": paciente[4],
    "diagnostico": paciente[5],
    "medicamento": paciente[6]
    }
    diccionario_pacientes.append(paciente_dict)                                

with open('usuarios.json', 'w') as file:
    json.dump(diccionario_pacientes, file, indent=4)

print("Datos de pacientes guardados en usuarios.json exitosamente.")



    