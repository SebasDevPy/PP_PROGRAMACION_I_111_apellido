from archivo import *
from pacientes import *
from os import system

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Ingresar paciente")
    print("2. Modificar paciente")
    print("3. Eliminar paciente")
    print("4. Mostrar todos los pacientes")
    print("5. Ordenar pacientes")
    print("6. Buscar paciente por DNI")
    print("7. Calcular promedio")
    print("8. Guardar y Salir")

def main():
    lista_pacientes, contador_pacientes_id = leer_pacientes_desde_csv([], 0)
    lista_pacientes_eliminados = cargar_pacientes_eliminados_desde_json([])
    historial = {}
    pacientes_ingresados = False

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_pacientes, pacientes_ingresados = ingreso_datos_pacientes(lista_pacientes, pacientes_ingresados)
        elif not pacientes_ingresados:
            print("Debe ingresar al menos un paciente para continuar.")
        elif opcion == "2":
            dni_modificar = input("Ingrese el DNI del paciente que desea modificar: ")
            modificar_paciente(dni_modificar, lista_pacientes, historial)
        elif opcion == "3":
            dni_eliminar = input("Ingrese el DNI del paciente que desea eliminar: ")
            if dni_eliminar.isdigit():
                lista_pacientes_eliminados = eliminar_paciente(lista_pacientes, dni_eliminar, lista_pacientes_eliminados)
                guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados)
                lista_pacientes = [paciente for paciente in lista_pacientes if not paciente.get("eliminado")]
                guardar_pacientes_en_csv(lista_pacientes)
            else:
                print("DNI inválido. Debe ser un número.")
        elif opcion == "4":
            mostrar_pacientes(lista_pacientes)
        elif opcion == "5":        
            direccion = input("Ingrese 'ascendente' o 'descendente': ")
            ordenar_pacientes(lista_pacientes, direccion)
        elif opcion == "6":
            buscar_paciente_por_dni(lista_pacientes)
        elif opcion == "7":
            calcular_promedio(lista_pacientes)
        elif opcion == "8":
            print("Guardando datos y saliendo del programa...")
            guardar_pacientes_en_csv(lista_pacientes)
            guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

        input("\nPresione Enter para continuar...")
        system("cls")

if __name__ == "__main__":
    main()

