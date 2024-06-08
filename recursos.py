import csv

def convertir_primera_letra_mayuscula(palabra):
    if len(palabra) > 0:
        return palabra[0].upper() + palabra[1:].lower()
    return palabra

def leer_pacientes_desde_csv(lista_pacientes, contador_pacientes_id):
    try:
        with open("pacientes.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                paciente_id = int(row["id"])
                if paciente_id > contador_pacientes_id:
                    contador_pacientes_id = paciente_id +1
                paciente = {
                    "id": paciente_id,
                    "nombre": convertir_primera_letra_mayuscula(row["nombre"]),
                    "apellido": convertir_primera_letra_mayuscula(row["apellido"]),
                    "dni": str(row["dni"]),
                    "grupo_sanguineo": row["grupo_sanguineo"].replace(" ", "_").lower(),  
                    "peso": float(row["peso"]),
                    "altura": row["altura"],
                    "edad": row["edad"]
                }
                lista_pacientes.append(paciente)
            contador_pacientes_id += 1
        print("Datos cargados correctamente desde pacientes.csv")   
    except FileNotFoundError:
        print("Archivo pacientes.csv no encontrado. Se iniciará con una lista vacía.")
    except csv.Error as e:
        print(f"Error al leer el archivo pacientes.csv: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return lista_pacientes, contador_pacientes_id