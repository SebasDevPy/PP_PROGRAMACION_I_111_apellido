import csv
import json
from recursos import *

def guardar_pacientes_en_csv(lista_pacientes):
    print("Guardando pacientes en el archivo CSV...")
    try:
        with open("pacientes.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "nombre", "apellido", "dni", "grupo_sanguineo", "peso", "altura", "edad", "eliminado"]  
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for paciente in lista_pacientes:
                paciente["dni"] = str(paciente["dni"])
                paciente["grupo_sanguineo"] = paciente.pop("grupo_sanguineo", "")
                paciente = {key.replace(" ", "_").lower(): value for key, value in paciente.items()}
                writer.writerow(paciente)
        print("Datos guardados correctamente en pacientes.csv")
    except Exception as e:
        print(f"Error al guardar en el archivo pacientes.csv: {e}")

def guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados):
    try:
        with open("Bajas.json", mode="w", encoding="utf-8") as file:
            json.dump(lista_pacientes_eliminados, file, indent=4)
        print("Datos de pacientes eliminados guardados correctamente en Bajas.json")
    except Exception as e:
        print(f"Error al guardar los pacientes eliminados en el archivo JSON: {e}")


def cargar_pacientes_eliminados_desde_json(lista_pacientes_eliminados):
    """
    Carga los datos de los empleados eliminados desde un archivo JSON.

    Args:
        lista_empleados_eliminados (list): Lista que almacenará los empleados eliminados leídos.

    Returns:
        list: Lista actualizada de empleados eliminados.
    """

    try:
        with open("Bajas.json" , mode= "r", encoding= "utf-8") as file:
            lista_pacientes_eliminados = json.load(file)
        print("Datos cargados correctamente desde Bajas.json")
    except FileNotFoundError:
        print("Archivo Bajas.json no encontrado. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al cargar los empleados eliminados desde el archivo JSON: {e}")
    return lista_pacientes_eliminados