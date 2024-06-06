from funciones import *
from archivo import *
from inputs import *

def crear_paciente(id: int, nombre, apellido, dni, grupo_sanguineo, peso, altura, edad):
    diccionario_paciente = {
        "id" : id,
        "nombre" : nombre,
        "apellido" : apellido,
        "dni": dni,
        "grupo_sanguineo" : grupo_sanguineo,
        "peso" : peso,
        "altura": altura,
        "edad": edad
    }
    return diccionario_paciente

def cargar_paciente(lista_pacientes, contador_pacientes_id):
    if lista_pacientes is None:
        
    
        datos_paciente = ingreso_datos_pacientes()

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

def mostrar_pacientes(lista_pacientes):
    if lista_pacientes:
        print(f"print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Grupo Sanguineo":<20} {"Peso":<10}' {"Altura":< 10} {"Edad":< 10}")
        for paciente in lista_pacientes:
            print(f"{paciente["id"]:<10} {paciente["nombre"]:<20} {paciente["apellido"]:<20} {paciente["dni"]:<10} {paciente["grupo sanguineo"]:<20} {paciente["peso"]:<10} {paciente["altura"]} {paciente["edad"]}")          

def mostrar_un_paciente(un_paciente):
    print(f"print(f'{"ID":<10} {"Nombre":<20} {"Apellido":<20} {"DNI":<10} {"Grupo Sanguineo":<20} {"Peso":<10}' {"Altura":< 10} {"Edad":< 10}")
    print(f"{un_paciente["id"]:<10} {un_paciente["nombre"]:<20} {un_paciente["apellido"]:<20} {un_paciente["dni"]:<10} {un_paciente["grupo sanguineo"]:<20} {un_paciente["peso"]:<10} {un_paciente["altura"]} {un_paciente["edad"]}")


def deshacer_ultimo_cambio(dni, lista_pacientes, historial):
    if dni in historial and historial[dni]:
        ultimo_cambio = historial[dni].pop()
        for paciente in lista_pacientes:
            if paciente["dni"] == dni:
                paciente.update(ultimo_cambio)
        print("Ultimo cambio deshecho exitosamente")
    else:
        print("No hay cambios que deshacer.")


def modificar_paciente(dni, lista_pacientes, historial):
    paciente_encontrado = False
    for paciente in lista_pacientes:
        if paciente ["dni"] == dni:
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

        opciones = {"1": "Nombre", "2": "Apellido", "3": "DNI", "4": "Grupo Sanguineo", "5": "Peso", "6": "Altura", "7": "Edad"}

        if opciones in opciones:
            campo = opciones[opcion]
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}")

            if campo == "nombre" or campo == "apellido":
                if validar_nombre_apellido(nuevo_valor):
                    paciente[campo] = nuevo_valor
                paciente[campo] = nuevo_valor
            elif campo == "dni":
                if validar_dni(nuevo_valor):
                    paciente[campo] = nuevo_valor
                paciente["dni"] = nuevo_valor
            elif campo == "grupo sanguineo":
                if validar_grupo_sanguineo(nuevo_valor):
                    paciente[campo] = nuevo_valor
            elif campo == "peso":
                if validar_peso(nuevo_valor):
                    paciente[campo] = float(nuevo_valor)
            elif campo == "altura":
                if validar_altura(nuevo_valor):
                    paciente[campo] = int(nuevo_valor)
                else:
                    print("Seleccion invalida")
            elif campo == "edad":
                if validar_edad(nuevo_valor):
                    paciente[campo] = int(nuevo_valor)
                else:
                    print("Seleccion invalida")
        else:
            print("Opcion no valida")
        break
    if paciente_encontrado is False:
        print("Paciente no encontrado")
        return
    
    print("¿Desea deshacer el ultimo cambio?")
    print("1. Si")
    print("2. No")
    opcion_deshacer = int(input("Ingresa el numero de la opcion: "))
    if opcion_deshacer == 1:
        deshacer_ultimo_cambio(dni, lista_pacientes, historial)
    elif opcion_deshacer == 2:
        print("Continuar...")
        

def ordenar_pacientes(lista_pacientes, criterio, direccion, orden, orden_inverso):
    paciente= len(lista_pacientes)
    criterios_validos = "nombre", "apellido", "altura", "grupo sanguineo"
    if criterio != criterios_validos:
        print("Solo puede ordenar por: nombre, apellido, altura o grupo sanguineo")

    for i in range(paciente - 1):
        for j in range(0, paciente - i - 1):
            if lista_pacientes[j][criterio] > lista_pacientes[j + 1][criterio]:
                lista_pacientes[j], lista_pacientes[j + 1] = lista_pacientes[j + 1], lista_pacientes[j]
            elif lista_pacientes[j]["id"] > lista_pacientes[j + 1]["id"]:
                lista_pacientes[j], lista_pacientes[j + 1] = lista_pacientes[j + 1], lista_pacientes[j]

    if direccion == "descendente":
        for i in range(len(lista_pacientes) -1, -1, -1):
            orden_inverso.append(lista_pacientes[i])
        mostrar_pacientes(orden_inverso)
    if direccion == "ascendente":
        for i in range(len(lista_pacientes)):
            orden.append(lista_pacientes[i])
        mostrar_pacientes(orden)

def eliminar_paciente(lista_pacientes, dni, paciente_eliminado, paciente_no_eliminado):
    paciente_encotrado = False
    for paciente in lista_pacientes:
        if paciente["dni"] == dni:
            confirmacion = input(f"Esta seguro de eliminar al paciente con el numero de DNI {dni}? s/n")
            if confirmacion.lower() == "s":
                paciente["eliminado"] = True
                print(f"Paciente con DNI {dni} eliminado")
                paciente_eliminado.append(paciente)
            else:
                print("Eliminacion cancelada")
            paciente_encotrado = True
        else:
            paciente_no_eliminado.append(paciente)
                
    if paciente_encotrado is False:
        print("Paciente no encontrado")
    return paciente_no_eliminado, paciente_eliminado

def buscar_paciente_por_dni(lista_pacientes):
    dni = input("Ingrese el DNI del paciente")
    for paciente in lista_pacientes:
        if paciente["dni"] == dni:
            mostrar_un_paciente(paciente) 
            return
    print("Paciente no encontrado...")  

def calcular_promedio(lista_pacientes):
    print("Elija el promedio que desea calcular: ")
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    opcion = input("Ingrese el numero de la opcion: ")

    if len(lista_pacientes) == 0:
        return 0
    if opcion == "Edad":
        suma_edad = sum(int(paciente["edad"]) for paciente in lista_pacientes)
        promedio_edad = suma_edad / len(lista_pacientes)
        return promedio_edad
    elif opcion == "Altura":
        suma_altura = sum(int(paciente["altura"])for paciente in lista_pacientes)
        promedio_altura = suma_altura / len(lista_pacientes)
        return promedio_altura
    elif opcion == "Peso":
        suma_peso = sum(int(paciente["peso"]) for paciente in lista_pacientes)
        promedio_peso = sum(int(paciente["peso"]) for paciente in lista_pacientes)
        return promedio_peso
    else:
        print("Opcion no valida, debe seleccionar entre: Edad, Altura o Peso")