from archivo import *
from validaciones import *
from funcion_paciente import *

def crear_paciente(id: int, nombre, apellido, dni, grupo_sanguineo, peso, altura, edad):
    diccionario_paciente = {
        "id" : id,
        "nombre" : nombre,
        "apellido" : apellido,
        "dni": dni,
        "grupo_sanguineo" : grupo_sanguineo,
        "peso" : peso,
        "altura": int(altura),
        "edad": edad
    }
    return diccionario_paciente

def cargar_paciente(lista_pacientes, contador_pacientes_id, nombre, apellido, edad, altura, peso, grupo_sanguineo,
                    dni):
    try:
        if lista_pacientes is None:
            lista_pacientes = []

        datos_paciente, validacion = ingreso_datos_pacientes(lista_pacientes, nombre, apellido, edad, altura, peso,
                                                             grupo_sanguineo, dni)

        if validacion:
            nuevo_paciente = crear_paciente(
                contador_pacientes_id,
                datos_paciente["nombre"],
                datos_paciente["apellido"],
                datos_paciente["dni"],
                datos_paciente["grupo_sanguineo"],
                datos_paciente["peso"],
                datos_paciente["altura"],
                datos_paciente["edad"]
            )

            lista_pacientes.append(nuevo_paciente)
            contador_pacientes_id += 1
            guardar_pacientes_en_csv(lista_pacientes)

        return lista_pacientes, contador_pacientes_id
    except Exception as e:
        print(f"Error en cargar_paciente: {e}")
        return None, contador_pacientes_id
  
def mostrar_pacientes(lista_pacientes):
    print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Grupo Sanguineo":<20} {"Peso":<10} {"Altura":<10} {"Edad":<10}')
    for paciente in lista_pacientes:
       print(f'{paciente["id"]:<10} {paciente["nombre"]:<20} {paciente["apellido"]:<20} {paciente["dni"]:<10} {paciente["grupo_sanguineo"]:<20} {paciente["peso"]:<10} {paciente["altura"]:<10} {paciente["edad"]:<10}')


def mostrar_un_paciente(un_paciente):
    print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Grupo Sanguineo":<20} {"Peso":<10} {"Altura":<10} {"Edad":<10}')
    print(f'{un_paciente["id"]:<10} {un_paciente["nombre"]:<20} {un_paciente["apellido"]:<20} {un_paciente["dni"]:<10} {un_paciente["grupo_sanguineo"]:<20} {un_paciente["peso"]:<10} {un_paciente["altura"]:<10} {un_paciente["edad"]:<10}')


def deshacer_ultimo_cambio(dni, lista_pacientes, historial):
    if dni in historial:
        ultimo_cambio = historial[dni].pop()
        for paciente in lista_pacientes:
            if paciente["dni"] == dni:
                paciente.update(ultimo_cambio)
        print("Último cambio deshecho exitosamente.")
    else:
        print("No hay cambios que deshacer.")


def modificar_paciente(dni, lista_pacientes, historial):
    paciente_encontrado = False
    dni = str(dni)
    pacientes_con_mismo_dni = [paciente for paciente in lista_pacientes if paciente["dni"] == dni]
    
    if len(pacientes_con_mismo_dni) == 0:
        print("No se encontraron pacientes con el DNI especificado.")
        return

    for paciente in pacientes_con_mismo_dni:
        paciente_encontrado = True
        historial[dni] = historial.get(dni, [])
        historial[dni].append(paciente)

        print(f"Paciente encontrado: {paciente_encontrado}")
        mostrar_un_paciente(paciente)
        print("Que campo desea modificar")
        print("1. Nombre")
        print("2. Apellido")
        print("3. DNI")
        print("4. Grupo Sanguineo")
        print("5. Peso")
        print("6. Altura")
        print("7. Edad")
        opcion = input("Ingrese el numero de la opcion: ")

        opciones = {"1": "Nombre", "2": "Apellido", "3": "DNI", "4": "Grupo Sanguineo", "5": "Peso",
                    "6": "Altura", "7": "Edad"}

        if opcion in opciones:
            campo = opciones[opcion]
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")

            if campo.lower() == "grupo sanguineo":
                if validar_grupo_sanguineo(nuevo_valor):
                    print("Modificando grupo sanguíneo...")
                    paciente["grupo_sanguineo"] = nuevo_valor.upper()  
                else:
                    print("Grupo sanguíneo inválido.")

            if campo.lower() == "nombre" or campo.lower() == "apellido":
                if validar_nombre_apellido(nuevo_valor):
                    paciente[campo.lower()] = nuevo_valor.title()
                else:
                    print("Nombre o apellido invalido.")
            elif campo.lower() == "dni":
                if validar_dni(nuevo_valor):
                    paciente[campo.lower()] = str(nuevo_valor)
                else:
                    print("DNI invalido.")

            elif campo.lower() == "peso":
                if validar_peso(nuevo_valor):
                    paciente[campo.lower()] = float(nuevo_valor)
                else:
                    print("Peso invalido.")
            elif campo.lower() == "altura":
                if validar_altura(nuevo_valor):
                    paciente[campo.lower()] = int(nuevo_valor)
                else:
                    print("Altura invalida.")
            elif campo.lower() == "edad":
                if validar_edad(nuevo_valor):
                    paciente[campo.lower()] = int(nuevo_valor)
                else:
                    print("Edad invalida.")

            deshacer = input("¿Desea deshacer el último cambio? (s/n): ")
            if deshacer.lower() == "s":
                deshacer_ultimo_cambio(dni, lista_pacientes, historial)
        else:
            print("Opcion no valida, ingrese un numero del 1 al 7")

        continuar = input("¿Desea editar otro campo? (s/n): ")
        if continuar.lower() != "s":
            return

    if len(pacientes_con_mismo_dni) == 0:
        print("Paciente no encontrado")

    print("¿Desea deshacer el ultimo cambio?")
    print("1. Si")
    print("2. No")
    opcion_deshacer = input("Ingresa el numero de la opcion: ")
    if opcion_deshacer == "1":
        deshacer_ultimo_cambio(dni, lista_pacientes, historial)
    elif opcion_deshacer == "2":
        print("Continuar...")

        
def ordenar_pacientes(lista_pacientes, direccion):
    opciones = {
        "1": "nombre",
        "2": "apellido",
        "3": "altura",
        "4": "grupo_sanguineo"
    }
    
    print("Seleccione el criterio de orden:")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Altura")
    print("4. Grupo Sanguineo")
    opcion = input("Ingrese el número de la opción: ")

    criterio = opciones.get(opcion)
    
    if criterio:
        paciente = len(lista_pacientes)
        for i in range(paciente - 1):
            for j in range(0, paciente - i - 1):
                if direccion == "ascendente":
                    if str(lista_pacientes[j][criterio]) > str(lista_pacientes[j + 1][criterio]):
                        lista_pacientes[j], lista_pacientes[j + 1] = lista_pacientes[j + 1], lista_pacientes[j]
                elif direccion == "descendente":
                    if str(lista_pacientes[j][criterio]) < str(lista_pacientes[j + 1][criterio]):
                        lista_pacientes[j], lista_pacientes[j + 1] = lista_pacientes[j + 1], lista_pacientes[j]
        mostrar_pacientes(lista_pacientes)
    else:
        print("Opción no válida.")

def eliminar_paciente(lista_pacientes, dni, pacientes_eliminados):
    paciente_encontrado = False 
    if dni.isdigit() == False:
        print("DNI invalido")
        return pacientes_eliminados
    dni = str(dni)

    for paciente in lista_pacientes:
        if paciente["dni"] == dni:
            confirmacion = input(f"¿Está seguro de eliminar al paciente {paciente['nombre']} {paciente['apellido']} con el número de DNI {dni}? s/n: ")
            if confirmacion.lower() == "s":
                paciente["eliminado"] = True 
                print(f"Paciente con DNI {dni} eliminado")
                pacientes_eliminados.append(paciente)
                paciente_encontrado = True
                break
            else:
                print("Eliminación cancelada")
                break
    
    if paciente_encontrado == False:
        print(f"No se encontró ningún paciente con el DNI {dni}.")
    
    return pacientes_eliminados
        
def buscar_paciente_por_dni(lista_pacientes, dni):
    
    for paciente in lista_pacientes:
        if paciente["dni"] == dni:
            return paciente
    return None
      

def calcular_promedio(lista_pacientes, campo):
    print("Elija el promedio que desea calcular: ")
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    opcion = input("Ingrese el numero de la opcion: ")

    if len(lista_pacientes) == 0:
        print("No hay pacientes para calcular el promedio")
        return 0
    if opcion == "1":
        suma_edad = sum(int(paciente["edad"]) for paciente in lista_pacientes)
        promedio_edad = suma_edad / len(lista_pacientes)
        print(f"El promedio de edad de los pacientes es: {promedio_edad}")
    elif opcion == "2":
        suma_altura = sum(int(paciente["altura"])for paciente in lista_pacientes)
        promedio_altura = suma_altura / len(lista_pacientes)
        print(f"El promedio de altura de los pacientes es: {promedio_altura}")
    elif opcion == "3":
        suma_peso = sum(float(paciente["peso"]) for paciente in lista_pacientes)
        promedio_peso = suma_peso / len(lista_pacientes)
        print(f"El promedio del peso de los pacientes es : {promedio_peso}")
    else:
        print("Opcion no valida, debe seleccionar entre: Edad, Altura o Peso")