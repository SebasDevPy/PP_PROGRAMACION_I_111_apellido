def validar_dni(dni:int) -> bool:
    if dni is None:
        return False
    return dni.isdigit() and len(dni) == 8 and 4000000 <=int(dni) <= 99999999
        

def validar_altura(altura: int) -> bool:
    altura = altura.isdigit() and 30 <= int(altura) <= 230

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
    nombre_completo = nombre_completo.isalpha() and nombre_completo[0].issuper() and len(nombre_completo) <= 20

def validar_edad(edad: int):
    edad = edad.isdigit() and 1 <= int(edad) <= 120


