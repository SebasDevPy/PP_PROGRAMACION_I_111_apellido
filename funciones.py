from inputs import *

def ingreso_datos_pacientes():
    while True:
        try:
            nombre = input("Ingrese el nombre del paciente: ")
            if validar_nombre_apellido(nombre):
                break
            print("El nombre debe de comenzar con mayuscula, solo se permiten letras (no mas de 20)")
            
            apellido = input("Ingrese el apellido del paciente: ")
            if validar_nombre_apellido(apellido):
                break
            print("El apellido debe de comenzar con mayuscula, solo se permiten letras (no mas de 20)")

            edad = input("Ingrese la edad del paciente: ")
            if validar_edad(edad):
                break
            print("La edad del paciente debe de ser entre 1 y 120")

            altura = input("Ingrese la altura del paciente en cm: ")
            if validar_altura(altura):
                break
            print("La altura debe de ser entre 30 y 230")

            peso = input("Ingrese el peso del paciente: ")
            if validar_peso(peso):
                break
            print("El peso del paciente debe de ser entre 10.0 y 300.0")

            grupo_sanguineo = input("Ingrese el grupo sanguineo del paciente: ")
            if validar_grupo_sanguineo(grupo_sanguineo):
                break
            print("El grupo sanguineo debe de ser: A, B, AB, 0 + o -")

            dni = input("Ingrese el dni del paciente: ")
            if validar_dni(dni):
                break
            print("El dni debe de tener 8 digitos y estar entre 4000000 y 99999999")
        
        except ValueError:
            print("Ingreso invalido")
    return {
        "nombre": nombre,
        "apellido": apellido,
        "edad": int(edad),
        "altura": int(altura),
        "peso": float(peso),
        "dni": dni,
        "grupo_sanguineo": grupo_sanguineo
    }