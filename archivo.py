import csv
import json

def leer_pacientes_desde_csv(lista_pacientes, contador_pacientes_id):
    """
    Lee los datos de los pacientes desde un archivo CSV y los agrega a una lista.

    Args:
        lista_pacientes (list): Lista que almacenará los pacientes leídos.
        contador_pacientes_id (int): Contador para el ID de los pacientes.

    Returns:
        tuple: Una tupla con la lista actualizada de pacientes y el nuevo contador de ID.
    """

    try:
        with open('pacientes.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                paciente_id = int(row["id"])
                if paciente_id > contador_pacientes_id:
                    contador_pacientes_id = paciente_id + 1
                paciente = {
                    "id": paciente_id,
                    "nombre": row["nombre"],
                    "apellido": row["apellido"],
                    "dni": row["dni"],
                    "grupo sanguineo": row["grupo sanguineo"],
                    "peso": float(row["peso"]),
                    "altura": row["altura"],
                    "edad": row["edad"]
                }
                lista_pacientes.append(paciente)
            contador_pacientes_id += 1 
    except FileNotFoundError:
        print("Archivo pacientes.csv no encontrado. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al leer el archivo pacientes.csv: {e}")
    return lista_pacientes, contador_pacientes_id


def guardar_pacientes_en_csv(lista_pacientes):
    """
    Guarda la lista de pacientes en un archivo CSV.

    Args:
        lista_pacientes (list): Lista de pacientes a guardar.
    """

    try:
        with open('pacientes.csv', mode='w', newline='') as file:
            fieldnames = ["id", "nombre", "apellido", "dni", "grupo sanguineo", "peso", "altura", "edad"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for paciente in lista_pacientes:
                writer.writerow(paciente)
        print("Datos guardados correctamente en pacientes.csv")
    except Exception as e:
        print(f"Error al guardar en el archivo pacientes.csv: {e}")


def guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados):
    """
    Guarda la lista de empleados eliminados en un archivo JSON.

    Args:
        lista_empleados_eliminados (list): Lista de empleados eliminados a guardar.
    """
        
    try:
        with open('Bajas.json', mode='w') as file:
            json.dump(lista_pacientes_eliminados, file, indent=4)
        print("Datos guardados correctamente en Bajas.json")
    except Exception as e:
        print(f"Error al guardar en el archivo Bajas.json: {e}")

def cargar_pacientes_eliminados_desde_json(lista_pacientes_eliminados):
    """
    Carga los datos de los empleados eliminados desde un archivo JSON.

    Args:
        lista_empleados_eliminados (list): Lista que almacenará los empleados eliminados leídos.

    Returns:
        list: Lista actualizada de empleados eliminados.
    """

    try:
        with open('Bajas.json', mode='r') as file:
            lista_pacientes_eliminados = json.load(file)
        print("Datos cargados correctamente desde Bajas.json")
    except FileNotFoundError:
        print("Archivo Bajas.json no encontrado. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al cargar los empleados eliminados desde el archivo JSON: {e}")
    return lista_pacientes_eliminados