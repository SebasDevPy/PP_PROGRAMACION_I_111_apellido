from inputs import *

def ingreso_datos_pacientes(lista_pacientes, contador_pacientes_id):
    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        if validar_nombre_apellido(nombre) == False:
            print("El nombre debe comenzar con mayúscula, solo se permiten letras (no más de 20)")
            print("Ingreso inválido")
            continue
        
        apellido = input("Ingrese el apellido del paciente: ")
        if validar_nombre_apellido(apellido) == False:
            print("El apellido debe comenzar con mayúscula, solo se permiten letras (no más de 20)")
            continue

        edad = input("Ingrese la edad del paciente: ")
        if validar_edad(edad) == False:
            print("La edad del paciente debe ser entre 1 y 120")
            continue

        altura = input("Ingrese la altura del paciente en cm: ")
        if validar_altura(altura) == False:
            print("La altura debe ser entre 30 y 230 cm")
            continue

        peso = input("Ingrese el peso del paciente: ")
        if validar_peso(peso) == False:
            print("El peso del paciente debe ser entre 10.0 y 300.0 kg")
            continue

        grupo_sanguineo = input("Ingrese el grupo sanguíneo del paciente: ")
        if validar_grupo_sanguineo(grupo_sanguineo) == False:
            print("El grupo sanguíneo debe ser: A, B, AB, 0 + o -")
            continue

        dni = input("Ingrese el DNI del paciente: ")
        if validar_dni(dni) == False:
            print("El DNI debe tener 8 dígitos y estar entre 4000000 y 99999999")
            continue
        
        break

    paciente = {
        "id": contador_pacientes_id,
        "nombre": nombre,
        "apellido": apellido,
        "edad": int(edad),
        "altura": int(altura),
        "peso": float(peso),
        "dni": dni,
        "grupo_sanguineo": grupo_sanguineo
    }
    
    lista_pacientes.append(paciente)
    contador_pacientes_id += 1

    return lista_pacientes, contador_pacientes_id
