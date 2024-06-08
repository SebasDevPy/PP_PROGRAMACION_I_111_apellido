from validaciones import *

def validar_datos_paciente(nombre, apellido, edad, altura, peso, grupo_sanguineo, dni):
    nombre_valido = validar_nombre_apellido(nombre)
    apellido_valido = validar_nombre_apellido(apellido)
    edad_valida = validar_edad(edad)
    altura_valida = validar_altura(altura)
    peso_valido = validar_peso(peso)
    grupo_sanguineo_valido = validar_grupo_sanguineo(grupo_sanguineo)
    dni_valido, dni_modificado = validar_dni(dni)
    
    return (
        nombre_valido, apellido_valido, edad_valida, altura_valida, 
        peso_valido, grupo_sanguineo_valido, dni_valido, dni_modificado
    )

def crear_paciente(id: int, nombre, apellido, dni, grupo_sanguineo, peso, altura, edad):
    diccionario_paciente = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "grupo_sanguineo": grupo_sanguineo,
        "peso": peso,
        "altura": altura,
        "edad": edad
    }
    return diccionario_paciente

def ingreso_datos_pacientes(lista_pacientes, nombre, apellido, edad, altura, peso, grupo_sanguineo, dni):
    try:
        nombre_valido, apellido_valido, edad_valida, altura_valida, peso_valido, grupo_sanguineo_valido, dni_valido, dni_modificado = validar_datos_paciente(nombre, apellido, edad, altura, peso, grupo_sanguineo, dni)

        if nombre_valido and apellido_valido and edad_valida and altura_valida and peso_valido and grupo_sanguineo_valido and dni_valido:
            nuevo_id = len(lista_pacientes)
            paciente = crear_paciente(nuevo_id, nombre, apellido, dni_modificado, grupo_sanguineo, peso, altura, edad)
            return paciente, True
        else:
            return None, False
    except Exception as e:
        print(f"Se ha producido un error: {e}")
        return None, False
