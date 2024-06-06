def validar_dni(dni: int) -> bool:
    if dni is None:
        return False
    if dni.isdigit() and len(dni) == 8:
        dni = "0" * (8 - len(dni)) + dni
        return 4000000 <= int(dni) <= 99999999
    return False
        

def validar_altura(altura: int) -> bool:
    if altura.isdigit() == False:
        return False
    altura_int = int(altura) 
    return 30<= altura_int <= 230

def validar_peso(peso: float) -> bool:
    try:
        peso_float = float(peso)
        return 10.0 <= peso_float <= 300.0
    except ValueError:
        return False
    
def validar_grupo_sanguineo(sangre: str) -> bool:
    grupo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-"]
    return sangre in grupo_sanguineo

def validar_nombre_apellido(nombre_completo: str):
    return nombre_completo.isalpha() and nombre_completo[0].isupper() and len(nombre_completo) <= 20

def validar_edad(edad: int):
    if edad.isdigit() == False:
        return False
    edad_int = int(edad)
    return 1 <= edad_int <= 120


