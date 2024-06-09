from validaciones import *

def validar_datos_paciente(nombre, apellido, edad, altura, peso, grupo_sanguineo, dni):
    """
    Valida los datos de un paciente.

    Args:
        nombre (str): El nombre del paciente.
        apellido (str): El apellido del paciente.
        edad (int): La edad del paciente.
        altura (int): La altura del paciente en centímetros.
        peso (float): El peso del paciente en kilogramos.
        grupo_sanguineo (str): El grupo sanguineo del paciente.
        dni (int): El numero de DNI del paciente.

    Returns:
        tuple: Una tupla que contiene booleanos indicando si cada dato es válido, y el número de DNI modificado si es valido.
    Raises:
        ValueError: Si el argumento nombre_completo es una cadena vacia o None.
   
    """
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
    """
    Crea un diccionario con los datos de un paciente.

    Args:
        id (int): El ID del paciente.
        nombre (str): El nombre del paciente.
        apellido (str): El apellido del paciente.
        dni (str): El numero de DNI del paciente.
        grupo_sanguineo (str): El grupo sanguineo del paciente.
        peso (float): El peso del paciente.
        altura (int): La altura del paciente.
        edad (int): La edad del paciente.

    Returns:
        dict: Un diccionario con los datos del paciente.
    Raises:
        TypeError: Si alguno de los argumentos no tiene el tipo de dato esperado.
    """
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
    """
    Valida y registra los datos de un nuevo paciente.

    Args:
        lista_pacientes (list): La lista de pacientes existente.
        nombre (str): El nombre del paciente.
        apellido (str): El apellido del paciente.
        edad (int): La edad del paciente.
        altura (int): La altura del paciente.
        peso (float): El peso del paciente.
        grupo_sanguineo (str): El grupo sanguineo del paciente.
        dni (int): El numero de DNI del paciente.

    Returns:
        tuple: Una tupla que contiene el diccionario del paciente y un booleano indicando si el ingreso fue exitoso.
    Raises:
        TypeError: Si alguno de los argumentos no tiene el tipo de dato esperado.        

    """
    try:
        nombre_valido, apellido_valido, edad_valida, altura_valida,peso_valido, grupo_sanguineo_valido, dni_valido, dni_modificado = validar_datos_paciente(nombre, apellido, edad, altura, peso, grupo_sanguineo, dni)

        if nombre_valido and apellido_valido and edad_valida and altura_valida and peso_valido and grupo_sanguineo_valido and dni_valido:
            nuevo_id = len(lista_pacientes) +1
            paciente = crear_paciente(nuevo_id, nombre, apellido, dni_modificado, grupo_sanguineo, peso, altura, edad)
            return paciente, True
        else:
            return None, False
    except Exception as e:
        print(f"Se ha producido un error: {e}")
        return None, False

