from funciones import *
from herramientas import *

def mostrar_menu_principal(opciones_menu):
    for i, opcion in enumerate(opciones_menu):
        print(i + 1, ". ", opcion, sep="")

def obtener_seleccion(opciones_menu):
    while True:
        seleccion = input(">> ")
        if validar_seleccion(seleccion, opciones_menu):
            return int(seleccion) - 1
        print("Selección inválida. Por favor ingrese un número válido.")

user = {}
menu = load_items('menu.csv')
carrito = []

opciones_menu = [
    "Revisar Menú",
    "Revisar Carrito",
    "Pagar",
    "Quitar Ítem del Carrito",
    "Buscar Ítem en Carrito (por nombre)",
    "Buscar Ítem en Carrito (por ingredientes)",
    "Filtrar Ítems que den Alergia",
    "Buscar Ítem en Menú",
    "Modificar Ítem del Menú",
    "Agregar Ítem al Menú",
    "Guardar Carrito",
    "Cargar Carrito",
    "Calcular Calorías del Carrito"
]
opciones_menu.append("Salir")

while True:
    print("\n--- Menú Principal ---")
    mostrar_menu_principal(opciones_menu)

    seleccion = obtener_seleccion(opciones_menu)

    # HACER ACCIONES ---------------------
    if seleccion == 0:  # Revisar Menú
        seleccion_item = revisar_menu(menu)
        if seleccion_item is not None:
            carrito.append(menu[seleccion_item])
            print(menu[seleccion_item]['nombre'], "agregado al carrito.")
    elif seleccion == 1:  # Revisar Carrito
        revisar_carrito(carrito)
    elif seleccion == 2:  # Pagar
        pagar(carrito)
    elif seleccion == 3:  # Quitar Ítem del Carrito
        quitar_item_carrito(carrito)
    elif seleccion == 4:  # Buscar Ítem en Carrito (por nombre)
        nombre = input("Ingrese el nombre del ítem a buscar: ")
        buscar_item_carrito_nombre(carrito, nombre)
    elif seleccion == 5:  # Buscar Ítem en Carrito (por ingredientes)
        ingredientes = input("Ingrese los ingredientes separados por coma: ").split(',')
        buscar_item_carrito_ingredientes(carrito, ingredientes)
    elif seleccion == 6:  # Filtrar Ítems que den Alergia
        alergias = input("Ingrese los ingredientes que le causan alergia separados por coma: ").split(',')
        filtrar_items_alergia(menu, alergias)
    elif seleccion == 7:  # Buscar Ítem en Menú
        palabra = input("Ingrese la palabra a buscar: ")
        buscar_item(menu, palabra)
    elif seleccion == 8:  # Modificar Ítem del Menú
        password = input("Ingrese la contraseña: ")
        modificar_item_menu(menu, password)
    elif seleccion == 9:  # Agregar Ítem al Menú
        password = input("Ingrese la contraseña: ")
        agregar_item_menu(menu, password)
    elif seleccion == 10:  # Guardar Carrito
        guardar_carrito(carrito, user['nombre'])
    elif seleccion == 11:  # Cargar Carrito
        carrito = cargar_carrito(user['nombre'])
    elif seleccion == 12:  # Calcular Calorías del Carrito
        calorias_totales = calcular_calorias(carrito)
        print("Total de calorías en el carrito:", calorias_totales)
    elif seleccion == len(opciones_menu) - 1:  # Salir
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intente de nuevo.")