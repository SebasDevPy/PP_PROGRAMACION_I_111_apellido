from validaciones import *

def ingreso_datos_pacientes(lista_pacientes, nombre, apellido, edad, altura, peso, grupo_sanguineo, dni):
    try:
        nuevo_id = len(lista_pacientes)
        nombre_valido = validar_nombre_apellido(nombre)
        apellido_valido = validar_nombre_apellido(apellido)
        edad_valida = validar_edad(edad)
        altura_valida = validar_altura(altura)
        peso_valido = validar_peso(peso)
        grupo_sanguineo_valido = validar_grupo_sanguineo(grupo_sanguineo)
        dni_valido, dni_modificado = validar_dni(dni)

        if not nombre_valido:
            return None, False

        if not apellido_valido:
            return None, False

        if not edad_valida:
            return None, False

        if not altura_valida:
            return None, False

        if not peso_valido:
            return None, False

        if not grupo_sanguineo_valido:
            return None, False

        if not dni_valido:
            return None, False

        paciente = {
            "id": nuevo_id,
            "nombre": nombre,
            "apellido": apellido,
            "edad": int(edad),
            "altura": int(altura),
            "peso": float(peso),
            "dni": dni_modificado,
            "grupo_sanguineo": grupo_sanguineo
        }

        return paciente, True

    except Exception as e:
        print(f"Error en ingreso_datos_pacientes: {e}")
        return None, False
