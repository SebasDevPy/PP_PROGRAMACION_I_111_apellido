def validar_dni(dni: int) -> tuple[bool, str]:
    """
    Valida un numero de DNI.

    Args:
        dni (int): El numero de DNI a validar.

    Returns:
        tuple[bool, str]: Una tupla que indica si el DNI es valido y el numero de DNI formateado.
    
    Raises:
        ValueError: Si el argumento dni no puede ser convertido a entero.

    """


    try:
        
        dni_str = str(dni)
        if not dni_str.isdigit() or len(dni_str) > 8:
            print("El DNI no tiene el formato correcto.")
            return False, None     
        if dni_str == '4000000':
            dni_str = '0' + dni_str
        dni = int(dni_str)
        if dni >= 4000000 and dni <= 99999999:
            dni_str = str(dni)
            if len(dni_str) < 8:
                dni_str = "0" * (8 - len(dni_str)) + dni_str
            return True, dni_str
        else:
            return False, None
    except ValueError:
        return False, None


def validar_altura(altura: int) -> bool:
    """
    Valida la altura de una persona.

    Args:
        altura (int): La altura en centimetros a validar.

    Returns:
        bool: True si la altura es valida, False de lo contrario.
    
    Raises:
        ValueError: Si la conversion de altura a entero falla.
    """
    try:
        altura_int = int(altura)
        return 30 <= altura_int <= 230
    except ValueError:
        return False

def validar_peso(peso: float) -> bool:
    """
    Valida el peso de una persona.

    Args:
        peso (float): El peso en kilogramos a validar.

    Returns:
        bool: True si el peso es valido, False de lo contrario.

    """
    try:
        peso = peso.replace(",", ".")
        peso_float = float(peso)
        return 10.0 <= peso_float <= 300.0
    except ValueError:
        return False
    
def validar_grupo_sanguineo(sangre: str) -> bool: 
    """
    Valida el grupo sanguineo de una persona.

    Args:
        sangre (str): El grupo sanguineo a validar.

    Returns:
        bool: True si el grupo sanguineo es valido, False de lo contrario.

    """
    try:
        grupo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-"]
        return  sangre.strip().replace(" ", "") in grupo_sanguineo
    except Exception as e:
        print(f"Error en validar_grupo_sanguineo: {e}")
        return False

def validar_nombre_apellido(nombre_completo: str):
    """
    Valida un nombre o apellido.

    Args:
        nombre_completo (str): El nombre o apellido a validar.

    Returns:
        bool: True si el nombre o apellido es valido, False de lo contrario.

    """

    try:
        if nombre_completo == "" or nombre_completo is None:
            return False
        if len(nombre_completo) > 20:
            return False
        palabras = nombre_completo.split()
        for palabra in palabras:
            if len(palabra) > 20 == False or palabra[0].isupper() == False or palabra[1:].islower() == False or palabra.isalpha() == False:
                return False
        return True
    except Exception as e:
        print(f"Error en validar_nombre_apellido: {e}")
        return False
    
def validar_edad(edad: int) -> bool:
    """
    Valida la edad de una persona.

    Args:
        edad (int): La edad a validar.

    Returns:
        bool: True si la edad es valida, False de lo contrario.

    """
    try:
        edad_int = int(edad)
        return 1 <= edad_int <= 120
    except ValueError:
        return False

def validar_input(mensaje, validacion, mensaje_error):
    """
    Función para solicitar una entrada al usuario y validarla segun la función de validacion proporcionada.

    Args:
        mensaje (str): El mensaje que se mostrara al solicitar la entrada al usuario.
        validacion (funcion): La funcion de validacion que se aplicara a la entrada del usuario.
        mensaje_error (str): El mensaje que se mostrara si la entrada del usuario no es valida.

    Returns:
        str: La entrada valida del usuario.

    """
    while True:
        entrada = input(mensaje)
        if validacion(entrada):
            return entrada
        else:
            print(mensaje_error)


def validar_input_dos(mensaje, validador, mensaje_error):
    while True:
        entrada = input(mensaje)
        valido, valor = validador(entrada)
        if valido:
            return valor
        else:
            print(mensaje_error)