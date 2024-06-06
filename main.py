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
    lista_pacientes, contador_pacientes_id= leer_pacientes_desde_csv([], 0)
    lista_pacientes_eliminados = cargar_pacientes_eliminados_desde_json ([])
    historial = {}
    pacientes_no_eliminados = []
    paciente_ingresado = False

    while True:

        mostrar_menu()
        opcion = input(" Seleccione una opcion: ")

        if opcion == "1":
            lista_pacientes, contador_pacientes_id, paciente_ingresado  = ingreso_datos_pacientes(lista_pacientes, contador_pacientes_id, paciente_ingresado)
        elif paciente_ingresado == False:
            print("Debe de ingresar un paciente para poder avanzar en el menu.")
            continue
        elif opcion == "2":
            dni_modificar = int(input("Ingrese el DNI del paciente el cual quere modificar: "))
            modificar_paciente(dni_modificar, lista_pacientes, historial)
        elif opcion == "3":
            dni_eliminar = int(input("Ingrese el DNI del paciente a eliminar: "))
            lista_pacientes, lista_pacientes_eliminados = eliminar_paciente(lista_pacientes, dni_eliminar, lista_pacientes_eliminados, pacientes_no_eliminados)
        elif opcion == "4":
            mostrar_pacientes(lista_pacientes)
        elif opcion == "5":
            criterio = input(" Ingrese el criterio de orden: nombre, apellido, altura, grupo sanguineo: " )
            direccion = input(" Ingrese si quiere de forma ascendente o descendente: ")
            ordenar_pacientes(lista_pacientes, criterio, direccion)
        elif opcion == "6":
            buscar_paciente_por_dni(lista_pacientes)
        elif opcion == "7":
            calcular_promedio(lista_pacientes)
        elif opcion == "8":
            print("Saliendo del programa...")
            guardar_pacientes_en_csv(lista_pacientes)
            guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados)
            break
        else:
            print("Opcion no valida, ingrese una opcion del menu. ")

        input("\nPresione Enter para continuar...")
        system("cls")

if __name__ == "__main__":
    main()

