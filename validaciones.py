def validar_dni(dni: int) -> tuple[bool, str]:
    try:
        if "." in str(dni):
            return False, None
        dni = int(dni)
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
    try:
        altura_int = int(altura)
        return 30 <= altura_int <= 230
    except ValueError:
        return False

def validar_peso(peso: float) -> bool:
    try:
        peso = peso.replace(",", ".")
        peso_float = float(peso)
        return 10.0 <= peso_float <= 300.0
    except ValueError:
        return False
    
def validar_grupo_sanguineo(sangre: str) -> bool: 
    try:
        sangre = sangre.strip()
        sangre = sangre.replace(" ", "").upper()
        grupo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-"]
        return sangre in grupo_sanguineo
    except Exception as e:
        print(f"Error en validar_grupo_sanguineo: {e}")
        return False

def validar_nombre_apellido(nombre_completo: str):
    try:
        if nombre_completo.isalpha() or "'" in nombre_completo:
            if nombre_completo == nombre_completo.capitalize() and len(nombre_completo) <= 20:
                return True
        return False
    except Exception as e:
        print(f"Error en validar_nombre_apellido: {e}")
        return False

def validar_edad(edad: int) -> bool:
    try:
        edad_int = int(edad)
        return 1 <= edad_int <= 120
    except ValueError:
        return False
