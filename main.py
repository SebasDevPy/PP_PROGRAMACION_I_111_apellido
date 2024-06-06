from pacientes import *

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Ingresar paciente")
    print("2. Modificar paciente")
    print("3. Eliminar paciente")
    print("4. Mostrar todos los pacientes")
    print("5. Ordenar pacientes")
    print("6. Buscar paciente por DNI")
    print("7. Calcular promedio")
    print("8. Salir")

def main():
    lista_pacientes, contador_pacientes_id= leer_pacientes_desde_csv([], 0)
    lista_pacientes_eliminados = cargar_paciente_eliminado_desde_json ([])
    historial = {}
    orden_inverso = []
    orden = []
    pacientes_no_eliminados = []

    while True:

        mostrar_menu()
        opcion = input(" Seleccione una opcion: ")

        if opcion == "1":
            lista_pacientes, contador_pacientes_id = ingreso_datos_pacientes(lista_pacientes, contador_pacientes_id)
        elif opcion == "2":
            dni_modificar = int(input("Ingrese el DNI del paciente el cual quere modificar: "))
            modificar_paciente(dni_modificar, lista_pacientes, historial)
        elif opcion == "3":
            dni_eliminar = int(input("Ingrese el DNI del paciente a eliminar: "))
            eliminar_paciente(lista_pacientes, dni_eliminar)

