from archivo import *
from validaciones import *
from funcion_paciente import *

def cargar_paciente(lista_pacientes, contador_pacientes_id, nombre, apellido, edad, altura, peso, grupo_sanguineo,
                    dni):
    """
    Carga un nuevo paciente a la lista de pacientes.

    Args:
        lista_pacientes (list): La lista de pacientes existente.
        contador_pacientes_id (int): El contador de ID para asignar a un nuevo paciente.
        nombre (str): El nombre del paciente.
        apellido (str): El apellido del paciente.
        edad (int): La edad del paciente.
        altura (int): La altura del paciente en centímetros.
        peso (float): El peso del paciente en kilogramos.
        grupo_sanguineo (str): El grupo sanguineo del paciente.
        dni (int): El numero de DNI del paciente.

    Returns:
        tuple: Una tupla que contiene la lista de pacientes actualizada y el nuevo contador de ID.
    Raises:
        TypeError: Si alguno de los argumentos no tiene el tipo de dato esperado.
    """    
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
            paciente_id = contador_pacientes_id 
            contador_pacientes_id += 1          
            guardar_pacientes_en_csv(lista_pacientes)
            print("Paciente ingresado correctamente.")
            
        else:
            print("Datos de paciente no validos. Por favor, verifique e intente nuevamente.")
            
        return lista_pacientes, contador_pacientes_id
    except Exception as e:
        print(f"Error en cargar_paciente: {e}")
        return None, contador_pacientes_id
  
def mostrar_pacientes(lista_pacientes):
    """
    Muestra la lista de pacientes en un formato de tabla.

    Args:
        lista_pacientes (list): La lista de pacientes a mostrar.

    """    
    print("Numero de pacientes en la lista:", len(lista_pacientes))
    print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Grupo Sanguineo":<20} {"Peso":<10} {"Altura":<10} {"Edad":<10}')
    for paciente in lista_pacientes:
        if not paciente.get("eliminado", False):
            print(f'{paciente["id"]:<10} {paciente["nombre"]:<20} {paciente["apellido"]:<20} {paciente["dni"]:<10} {paciente["grupo_sanguineo"]:<20} {paciente["peso"]:<10} {paciente["altura"]:<10} {paciente["edad"]:<10}')

    
def mostrar_un_paciente(un_paciente):
    print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Grupo Sanguineo":<20} {"Peso":<10} {"Altura":<10} {"Edad":<10}')
    print(f'{un_paciente["id"]:<10} {un_paciente["nombre"]:<20} {un_paciente["apellido"]:<20} {un_paciente["dni"]:<10} {un_paciente["grupo_sanguineo"]:<20} {un_paciente["peso"]:<10} {un_paciente["altura"]:<10} {un_paciente["edad"]:<10}')

def deshacer_ultimo_cambio(dni, lista_pacientes, historial):
    """
    Deshace el ultimo cambio realizado en un paciente si el usuario quiere.

    Args:
        dni (str): El numero de DNI del paciente.
        lista_pacientes (list): La lista de pacientes.
        historial (dict): El historial de cambios.

    """    
    if dni in historial:
        ultimo_cambio = historial[dni].pop()
        for paciente in lista_pacientes:
            if paciente["dni"] == dni:
                paciente.update(ultimo_cambio)
        print("Ultimo cambio deshecho exitosamente.")
    else:
        print("No hay cambios que deshacer.")

def modificar_paciente(dni, lista_pacientes, historial):
    """
    Modifica los datos de un paciente y los guarda.

    Args:
        dni (str): El numero de DNI del paciente.
        lista_pacientes (list): La lista de pacientes.
        historial (dict): El historial de cambios.

    """    
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
        continuar = "s"
        while continuar.lower() == "s":
            print("Que campo desea modificar")
            print("1. Nombre")
            print("2. Apellido")
            print("3. DNI")
            print("4. Grupo Sanguineo")
            print("5. Peso")
            print("6. Altura")
            print("7. Edad")
            print("8. Volver atras")
            opcion = input("Ingrese el numero de la opcion: ")

            opciones = {"1": "Nombre", "2": "Apellido", "3": "DNI", "4": "Grupo Sanguineo", "5": "Peso",
                        "6": "Altura", "7": "Edad", "8": "Volver atras"}

            if opcion in opciones:
                campo = opciones[opcion]
                if campo == "Volver atras":
                    break
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
                print("Opcion no valida, ingrese un numero del 1 al 8")

            continuar = input("¿Desea editar otro campo? (s/n): ")
            if continuar.lower() != "s":
                break

    if len(pacientes_con_mismo_dni) == 0:
        print("Paciente no encontrado")

    if continuar.lower() != "s" and deshacer.lower() != "s":
        guardar_cambios = input("Quiere guardar los cambios? s/n: ")
        if guardar_cambios.lower() == "s":
            lista_pacientes[lista_pacientes.index(paciente)] = paciente
            guardar_pacientes_en_csv(lista_pacientes)
        else:
            print("Descartando cambios")
     
def ordenar_pacientes(lista_pacientes, direccion):
    """
    Ordena la lista de pacientes segun un criterio dado.

    Args:
        lista_pacientes (list): La lista de pacientes a ordenar.
        direccion (str): La direccion del orden ("ascendente" o "descendente").

    """    
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
    opcion = input("Ingrese el numero de la opción: ")

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
        guardar_pacientes_en_csv(lista_pacientes)
    else:
        print("Opción no valida.")

def eliminar_paciente(lista_pacientes, dni, lista_pacientes_eliminados, contador_pacientes_id):
    """
    Elimina un paciente de la lista de pacientes.

    Args:
        lista_pacientes (list): La lista de pacientes.
        dni (str): El numero de DNI del paciente a eliminar.
        lista_pacientes_eliminados (list): La lista de pacientes eliminados.
        contador_pacientes_id (int): El contador de ID de pacientes.

    Returns:
        tuple: Una tupla que contiene la lista de pacientes actualizada, la lista de pacientes eliminados y el contador de ID de pacientes.

    """    
    if  dni.isdigit() == False:
        print("DNI invalido. Debe ser un numero.")
        return lista_pacientes, lista_pacientes_eliminados

    dni = str(dni)  
    
    paciente_encontrado = False  
    i = 0 
    
    while i < len(lista_pacientes):
        paciente = lista_pacientes[i]
        if paciente["dni"] == dni:
            confirmacion = input(f"¿Esta seguro de eliminar al paciente {paciente['nombre']} {paciente['apellido']} con el numero de DNI {dni}? (s/n): ")
            if confirmacion.lower() == "s":
                paciente["eliminado"] = True 
                print(f"Paciente con DNI {dni} eliminado")
                lista_pacientes_eliminados.append(paciente)
                lista_pacientes.remove(paciente)
                paciente_encontrado = True
                break
            elif confirmacion.lower() == "n":
                print("Eliminacion cancelada.")
                paciente_encontrado = True
                break
            else:
                print("Respuesta no valida. Por favor, ingrese 's' para confirmar o 'n' para cancelar.")
        else:
            i += 1
    if  paciente_encontrado == False:
        print(f"No se encontro ningun paciente con el DNI {dni}.")       
    return lista_pacientes, lista_pacientes_eliminados, contador_pacientes_id
      
def buscar_paciente_por_dni(lista_pacientes, dni):
    """
    Busca un paciente en la lista de pacientes por su número de DNI.

    Args:
        lista_pacientes (list): La lista de pacientes.
        dni (str): El numero de DNI del paciente a buscar.

    Returns:
        dict or None: El diccionario del paciente si se encuentra, None si no se encuentra.
    Raises:
        TypeError: Si alguno de los argumentos no tiene el tipo de dato esperado.
    """    
    for paciente in lista_pacientes:
        if paciente["dni"] == dni:
            return paciente
    return None
      
def calcular_promedio(lista_pacientes, campo):
    """
    Calcula el promedio de un campo especifico en los datos de los pacientes.

    Args:
        lista_pacientes (list): La lista de pacientes.
        campo (str): El campo para el que se calculara el promedio.

    Returns:
        float or None: El promedio del campo especificado.

    """    
    try:
        suma_campo = sum(float(paciente[campo]) for paciente in lista_pacientes)
        promedio = suma_campo / len(lista_pacientes)
        print(f"El promedio de {campo} de los pacientes es: {promedio}")
        return promedio
    except KeyError:
        print(f"Campo '{campo}' no encontrado en los datos de los pacientes.")
        return None
    except ZeroDivisionError:
        print("No hay pacientes en la lista.")
        return None

def determinar_compatibilidad(dni, lista_pacientes):    
    paciente = None

    for s in lista_pacientes:
        if s["dni"] == dni:
            paciente = s
            break

    if paciente is None:
        print("No hay paciente")
        return
    
    grupo_sanguineo = paciente["grupo_sanguineo"]

    if grupo_sanguineo == "0-":
        puede_recibir = ["0-"]
        puede_donar = ["0-", "0+", "A-", "A+", "B+", "B-", "AB+", "AB-"]
    elif grupo_sanguineo == "0+":
        puede_recibir = ["0-", "0+"]
        puede_donar = ["0+", "A+", "B+", "AB+"]
    elif grupo_sanguineo == "A-":
        puede_recibir = ["0-", "A-"]
        puede_donar = ["A+", "A-", "AB+", "AB-"]
    elif grupo_sanguineo == "A+":
        puede_recibir = ["0-", "0+", "A-", "A+"]
        puede_donar = ["AB+", "A+"]
    elif grupo_sanguineo == "B-":
        puede_recibir = ["0-", "B-"]
        puede_donar = ["0-", "B-"]
    elif grupo_sanguineo == "B+":
        puede_recibir = ["0-", "0+", "B-", "B+"]
        puede_donar = ["AB-", "AB+", "B-", "B+"]
    elif grupo_sanguineo == "AB+":
        puede_recibir = ["0-", "0+", "A-", "A+", "B+", "B-", "AB+", "AB-"]
        puede_donar = ["AB+"]
    elif grupo_sanguineo == "AB-":
        puede_recibir =["0-", "A-", "B-", "AB-"]
        puede_donar =["AB+", "AB-"]
    else:
        print("Grupo sanguineo no existente.")
  
    print(f"El paciente con DNI: {dni} y grupo sanguineo {grupo_sanguineo} puede donar a: {puede_donar}")
    print(f"El paciente con DNI: {dni} y grupo sanguineo {grupo_sanguineo} puede recibir de: {puede_recibir}")
     
    donante_posible = [
        pa for pa in lista_pacientes
        if pa["grupo_sanguineo"] in puede_recibir and pa["dni"] != dni
    ][:3]
    if donante_posible:
        print(f"Los primeros tres donantes compatibles son {[paciente["dni"] for paciente in donante_posible]} ")
        indice = 1
        for donante in donante_posible:
            print(f"{indice}. DNI: {donante_posible}, Nombre: {donante["nombre"]}, Apellido:{donante["apellido"]}")
            indice += 1
    else:
        print("No se encontraron donantes. ")