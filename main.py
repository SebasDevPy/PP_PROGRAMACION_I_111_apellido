from validaciones import *
from archivo import *
from pacientes import *
from os import system
from recursos import *

def mostrar_menu(pacientes_ingresados):
    if pacientes_ingresados:
        opciones = [
            "1. Ingresar paciente", "2. Buscar y Modificar paciente", "3. Eliminar paciente", 
            "4. Mostrar todos los pacientes", "5. Ordenar pacientes", 
            "6. Calcular promedio","7 Determinar compatibilidad", "8. Guardar y Salir"
        ]
    else:
        opciones = ["1. Ingresar paciente", "8. Guardar y Salir"]   
    print("\n--- Menu Principal ---\n" + "\n".join(opciones) + "\n")
    
def main():
    try:
        lista_pacientes, contador_pacientes_id = leer_pacientes_desde_csv([], 0)
        lista_pacientes_eliminados = cargar_pacientes_eliminados_desde_json([])
        historial = {}
        pacientes_ingresados = False
         
        while True:
            if pacientes_ingresados:
                mostrar_menu(pacientes_ingresados)
                opcion = input("Seleccione una opcion: ")
            else:
                mostrar_menu(pacientes_ingresados)
                opcion = input("Debe ingresar al menos un paciente antes de utilizar esta opcion. Seleccione una opcion: ")

            match opcion:
                case "1":
                    nombre = validar_input("Ingrese el nombre del paciente: ", validar_nombre_apellido,
                                           "El nombre no puede ser de mas de 20 caracteres y debe comenzar con mayuscula")
                    apellido = validar_input("Ingrese el apellido del paciente: ", validar_nombre_apellido,
                                             "El nombre no puede ser de mas de 20 caracteres y debe comenzar con mayuscula")
                    edad = validar_input("Ingrese la edad del paciente: ", validar_edad, "La edad debe de ser entre 1 y 120 ")
                    altura = validar_input("Ingrese la altura del paciente: ", validar_altura, "La altura debe de ser entre 30 y 230")
                    peso = validar_input("Ingrese el peso del paciente: ", validar_peso, "El peso debe de ser entre 10 y 300")
                    dni = validar_input_dos("Ingrese el DNI del paciente: ", validar_dni, "El DNI debe ir sin puntos, entre 4000000 y 99999999.")
                    grupo_sanguineo = validar_input("Ingrese el grupo sanguineo del paciente: ", validar_grupo_sanguineo,
                                                     "El grupo sanguineo debe de ser: A, B, AB, 0, + o -")

                    lista_pacientes, contador_pacientes_id = cargar_paciente(lista_pacientes, contador_pacientes_id,
                                                                              nombre, apellido, edad, altura, peso, grupo_sanguineo, dni)
                    if lista_pacientes:
                        pacientes_ingresados = True

                case "2":
                    if not pacientes_ingresados:
                        print("Debe ingresar al menos un paciente antes de utilizar esta opción.\n")
                    else:
                        dni_modificar = input("Ingrese el DNI del paciente que desea modificar: ")
                        paciente = buscar_paciente_por_dni(lista_pacientes, dni_modificar)
                        if paciente:
                            modificar_paciente(dni_modificar, lista_pacientes, historial)
                        else:
                            print("Paciente no encontrado.\n")

                case "3":
                    if  pacientes_ingresados == False:
                        print("Debe ingresar al menos un paciente antes de utilizar esta opción.\n")
                    else:
                        dni_eliminar = input("Ingrese el DNI del paciente que desea eliminar: ")
                        if dni_eliminar.isdigit():
                            lista_pacientes, lista_pacientes_eliminados, contador_pacientes_id = eliminar_paciente(lista_pacientes, dni_eliminar,
                                                                                                                    lista_pacientes_eliminados, contador_pacientes_id)
                            guardar_pacientes_en_csv(lista_pacientes)
                            guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados)
                        else:
                            print("DNI invalido. Debe ser un numero.\n")

                case "4":
                    mostrar_pacientes(lista_pacientes)

                case "5":
                    direccion = input("Ingrese 'ascendente' o 'descendente': ")
                    ordenar_pacientes(lista_pacientes, direccion)

                case "6":
                    campo = input("Ingrese el campo del cual desea calcular el promedio (edad, altura, peso): ")
                    if campo in ['edad', 'altura', 'peso']:
                        calcular_promedio(lista_pacientes, campo)
                        
                    else:
                        print("Opción no válida. Debe seleccionar una de las opciones proporcionadas.\n")

                case "7":
                    dni_paciente = input("Ingrese el dni del paciente: ")
                    determinar_compatibilidad(dni_paciente, lista_pacientes)

                case "8":
                    print("Guardando datos y saliendo del programa...\n")
                    guardar_pacientes_en_csv(lista_pacientes)
                    guardar_pacientes_eliminados_en_json(lista_pacientes_eliminados)
                    break

                case _:
                    print("Opcion no valida. Por favor, seleccione una opcion del menu.\n")

            input("\nPresione Enter para continuar...")
            system("cls")

    except Exception as e:
        print(f"Se ha producido un error: {e}\n")

if __name__ == "__main__":
    main()



