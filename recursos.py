import csv

def leer_pacientes_desde_csv(lista_pacientes, contador_pacientes_id):
    """
    Lee los datos de los pacientes desde un archivo CSV y los carga en una lista de pacientes.

    Args:
        lista_pacientes (list): La lista de pacientes existente.
        contador_pacientes_id (int): El contador de ID de pacientes.

    Returns:
        tuple: Una tupla que contiene la lista de pacientes actualizada y el nuevo contador de ID de pacientes.
    
    Raises:
        FileNotFoundError: Si no se encuentra el archivo "pacientes.csv".
        csv.Error: Si ocurre un error al leer el archivo CSV.
        Exception: Para cualquier otro error inesperado durante la ejecución.        

    """    
    try:
        with open("pacientes.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                paciente_id = int(row["id"])
                if paciente_id > contador_pacientes_id:
                    contador_pacientes_id = paciente_id +1
                paciente = {
                        "id": paciente_id,
                        "nombre": row["nombre"],
                        "apellido": row["apellido"],
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
        print("Archivo pacientes.csv no encontrado. Se iniciara con una lista vacia.")
    except csv.Error as e:
        print(f"Error al leer el archivo pacientes.csv: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return lista_pacientes, contador_pacientes_id