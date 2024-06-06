from inputs import *

def ingreso_datos_pacientes(lista_pacientes, paciente_ingresado):
    nuevo_id = len(lista_pacientes)

    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        if validar_nombre_apellido(nombre):
            break
        print("El nombre debe comenzar con mayúscula y contener solo letras (máx. 20 caracteres).")

    while True:
        apellido = input("Ingrese el apellido del paciente: ")
        if validar_nombre_apellido(apellido):
            break
        print("El apellido debe comenzar con mayúscula y contener solo letras (máx. 20 caracteres).")

    while True:
        edad = input("Ingrese la edad del paciente: ")
        if validar_edad(edad):
            break
        print("La edad del paciente debe ser un número entre 1 y 120.")

    while True:
        altura = input("Ingrese la altura del paciente en cm: ")
        if validar_altura(altura):
            break
        print("La altura del paciente debe ser un número entre 30 y 230.")

    while True:
        peso = input("Ingrese el peso del paciente: ")
        if validar_peso(peso):
            break
        print("El peso del paciente debe ser un número entre 10.0 y 300.0.")

    while True:
        grupo_sanguineo = input("Ingrese el grupo sanguíneo del paciente: ")
        if validar_grupo_sanguineo(grupo_sanguineo):
            break
        print("El grupo sanguíneo del paciente debe ser A+, A-, B+, B-, AB+, AB-, 0+ o 0-.")

    while True:
        dni = input("Ingrese el DNI del paciente: ")
        if validar_dni(dni):
            break
        print("El DNI del paciente debe ser un número de 8 dígitos entre 4000000 y 99999999.")

    paciente = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "edad": int(edad),
        "altura": int(altura),
        "peso": float(peso),
        "dni": dni,
        "grupo_sanguineo": grupo_sanguineo
    }

    lista_pacientes.append(paciente)
    paciente_ingresado = True

    return lista_pacientes, paciente_ingresado
