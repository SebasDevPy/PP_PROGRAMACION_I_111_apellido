from inputs import *

def ingreso_datos_pacientes(lista_pacientes, contador_pacientes_id, paciente_ingresado):
    while True:
        nombre = input("Ingrese el nombre del paciente: ")
        while validar_nombre_apellido(nombre) == False:
            print("El nombre debe comenzar con mayúscula y contener solo letras (máx. 20 caracteres).")
            continue

        apellido = input("Ingrese el apellido del paciente: ")
        while  validar_nombre_apellido(apellido) == False:
            print("El apellido debe comenzar con mayúscula y contener solo letras (máx. 20 caracteres).")
            apellido = input("Ingrese nuevamente el apellido del paciente: ")

        edad = input("Ingrese la edad del paciente: ")
        while  validar_edad(edad) == False:
            print("La edad del paciente debe ser un número entre 1 y 120.")
            edad = input("Ingrese nuevamente la edad del paciente: ")

        altura = input("Ingrese la altura del paciente en cm: ")
        while  validar_altura(altura) == False:
            print("La altura del paciente debe ser un número entre 30 y 230.")
            altura = input("Ingrese nuevamente la altura del paciente en cm: ")

        peso = input("Ingrese el peso del paciente: ")
        while  validar_peso(peso) == False:
            print("El peso del paciente debe ser un número entre 10.0 y 300.0.")
            peso = input("Ingrese nuevamente el peso del paciente: ")

        grupo_sanguineo = input("Ingrese el grupo sanguíneo del paciente: ")
        while  validar_grupo_sanguineo(grupo_sanguineo) == False:
            print("El grupo sanguíneo del paciente debe ser A+, A-, B+, B-, AB+, AB-, 0+ o 0-.")
            grupo_sanguineo = input("Ingrese nuevamente el grupo sanguíneo del paciente: ")

        dni = input("Ingrese el DNI del paciente: ")
        while  validar_dni(dni) == False:
            print("El DNI del paciente debe ser un número de 8 dígitos entre 4000000 y 99999999.")
            dni = input("Ingrese nuevamente el DNI del paciente: ")

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

    paciente_ingresado = True  

    return lista_pacientes, contador_pacientes_id, paciente_ingresado
