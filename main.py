import validaciones
from archivo import *
from pacientes import *
from os import system
from recursos import *

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
    try:
        lista_pacientes, contador_pacientes_id = leer_pacientes_desde_csv([], 0)
        lista_pacientes_eliminados = cargar_pacientes_eliminados_desde_json([])
        historial = {}
        pacientes_ingresados = False

        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del paciente: ")
                while validaciones.validar_nombre_apellido(nombre) == False:
                    print("El nombre debe de comenzar con mayuscula y contener maximo 20 caracteres")
                    nombre = input("Ingrese el nombre del paciente: ")

                apellido = input("Ingrese el apellido del paciente: ")
                while validaciones.validar_nombre_apellido(apellido) == False:
                    print("El apellido debe de comenzar con mayuscula y contener maximo 20 caracteres")
                    apellido = input("Ingrese el apellido del paciente: ")

                edad = input("Ingrese la edad del paciente: ")
                while validaciones.validar_edad(edad) == False:
                    print("Error: La edad debe ser un número entre 1 y 120.")
                    edad = input("Ingrese la edad del paciente: ")

                altura = input("Ingrese la altura del paciente: ")
                while  validaciones.validar_altura(altura) == False:
                    print("La altura debe de ser entre 30 y 230")
                    altura = input("Ingrese la altura del paciente: ")

                peso = input("Ingrese el peso del paciente: ")
                while validaciones.validar_peso(peso) == False:
                    print("El peso debe de ser entre 10 y 300")
                    peso = input("Ingrese el peso del paciente: ")

                dni = input("Ingrese el DNI del paciente: ")
                while validaciones.validar_dni(dni) == False:
                    print("El DNI debe de ser entre 4000000 y 99999999.")
                    dni = input("Ingrese el DNI del paciente: ")

                grupo_sanguineo = input("Ingrese el grupo sanguineo del paciente: ")
                while validaciones.validar_grupo_sanguineo(grupo_sanguineo) == False:
                    print("El grupo sanguineo debe de ser: A+, B+, AB+, 0+ A-, B-, AB- o 0-")
                    grupo_sanguineo = input("Ingrese el grupo sanguineo del paciente: ")
                
                lista_pacientes, contador_pacientes_id = cargar_paciente(lista_pacientes, contador_pacientes_id, nombre,
                                                            apellido, edad, altura, peso, grupo_sanguineo, dni)
                
                pacientes_ingresados = True

            elif opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6" or opcion == "7":
                if  pacientes_ingresados == False:
                    print("Debe ingresar al menos un paciente antes de utilizar esta opción.")
                
                else:
                    if opcion == "2":
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
                        dni = input("Ingrese el DNI del paciente a buscar: ")
                        paciente = buscar_paciente_por_dni(lista_pacientes, dni)
                        if paciente:
                            mostrar_un_paciente(paciente)
                        else:
                            print("Paciente no encontrado.")

                    elif opcion == "7":
                        campo = input("Ingrese el campo del cual desea calcular el promedio (edad, altura, peso): ")
                        if campo in ['edad', 'altura', 'peso']:
                            promedio = calcular_promedio(lista_pacientes, campo)
                            print(f"El promedio de {campo} de los pacientes es: {promedio}")
                        else:
                            print("Opción no válida. Debe seleccionar una de las opciones proporcionadas.")

            elif opcion == "8":
                print("Guardando datos y saliendo del programa...")
                guardar_pacientes_en_csv(lista_pacientes)
                guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados)
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")

            input("\nPresione Enter para continuar...")
            system("cls")

    except Exception as e:
        print(f"Se ha producido un error: {e}")

if __name__ == "__main__":
    main()


