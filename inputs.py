def validar_dni(dni: str) -> bool:
    if "." in dni:
        return False
    try:
        dni = str(int(dni)) 
        dni = "0" * (8 - len(dni)) + dni  
        return 4000000 <= int(dni) <= 99999999
    except ValueError:
        return False

def validar_altura(altura: int) -> bool:
    try:
        altura_int = int(altura)
        return 30 <= altura_int <= 230
    except ValueError:
        return False

def validar_peso(peso: float) -> bool:
    peso = peso.replace(",", ".")
    try:
        peso_float = float(peso)
        return 10.0 <= peso_float <= 300.0
    except ValueError:
        return False
    
def validar_grupo_sanguineo(sangre: str) -> bool:
    
    sangre = sangre.replace(" ", "").upper()
    grupo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-"]
    return sangre in grupo_sanguineo

def validar_nombre_apellido(nombre_completo: str):
    nombre_completo = nombre_completo.capitalize()
    if nombre_completo.isalpha() or "'" in nombre_completo:
        if nombre_completo == nombre_completo.capitalize() and len(nombre_completo) <= 20:
            return True
    return False

def validar_edad(edad: int) -> bool:
    try:
        edad_int = int(edad)
        return 1 <= edad_int <= 120
    except ValueError:
        return False

