"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------
from herramientas import check_password

#ejemplo de funcion
def revisar_menu(menu: list) -> None:
    """
    Muestra el menú de comidas, con el precio. También permite seleccionar un item del menú para agregarlo al “carrito”.
    """
    print("Menú de Comidas:")
    for index, item in enumerate(menu):
        print(index + 1, item['nombre'], "- Precio:", item['precio'], "- Calorías:", item['kcal'])
    seleccion = input("Seleccione un item para agregar al carrito (o presione Enter para volver): ")
    if seleccion.isdigit() and 0 < int(seleccion) <= len(menu):
        return int(seleccion) - 1
    return None

def revisar_carrito(carrito: list) -> None:
    """
    Muestra el carrito de comidas seleccionadas.
    """
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Carrito de Compras:")
        for index, item in enumerate(carrito):
            print(index + 1, item['nombre'], "- Precio:", item['precio'], "- Calorías:", item['kcal'])

def pagar(carrito: list) -> None:
    """
    Muestra el costo total y cantidad de ítems del carrito. Luego sugiere la propina (10%).
    """
    total = sum(item['precio'] for item in carrito)
    print("Total a pagar:", total)
    print("Propina sugerida (10%):", total * 0.1)
    decision = input("Aceptar el pago (1) o Seguir Comprando (2): ")
    if decision == "1":
        print("Pago aceptado. Gracias por su compra.")
        carrito.clear()
    else:
        print("Continúe comprando.")

def quitar_item_carrito(carrito: list) -> None:
    """
    Saca un objeto del carrito.
    """
    revisar_carrito(carrito)
    seleccion = input("Seleccione el número del item a quitar: ")
    if seleccion.isdigit() and 0 < int(seleccion) <= len(carrito):
        carrito.pop(int(seleccion) - 1)
        print("Item removido del carrito.")

def buscar_item_carrito_nombre(carrito: list, nombre: str) -> None:
    """
    Se debe buscar un item en el carrito según el nombre.
    """
    resultados = [item for item in carrito if nombre.lower() in item['nombre'].lower()]
    if resultados:
        print("Items encontrados:")
        for item in resultados:
            print(item['nombre'], "- Precio:", item['precio'], "- Calorías:", item['kcal'])
    else:
        print("No se encontraron items con ese nombre.")

def buscar_item_carrito_ingredientes(carrito: list, ingredientes: list) -> None:
    """
    Se debe buscar un item en el carrito, según los ingredientes del ítem.
    """
    resultados = [item for item in carrito if any(ing.lower() in item['ingredientes'] for ing in ingredientes)]
    if resultados:
        print("Items encontrados:")
        for item in resultados:
            print(item['nombre'], "- Precio:", item['precio'], "- Calorías:", item['kcal'])
    else:
        print("No se encontraron items con esos ingredientes.")

def filtrar_items_alergia(menu: list, alergias: list) -> None:
    """
    Se muestran los ítem que NO tengan el o los ingredientes que le causen alergia al usuario.
    """
    resultados = [item for item in menu if not any(alg.lower() in item['ingredientes'] for alg in alergias)]
    if resultados:
        print("Items seguros:")
        for item in resultados:
            print(item['nombre'], "- Precio:", item['precio'], "- Calorías:", item['kcal'])
    else:
        print("No se encontraron items seguros.")

def buscar_item(menu: list, palabra: str) -> None:
    """
    Se debe buscar un ítem que contenga, en alguna parte, la palabra ingresada por el usuario.
    """
    resultados = [item for item in menu if palabra.lower() in item['nombre'].lower()]
    if resultados:
        print("Items encontrados:")
        for item in resultados:
            print(item['nombre'], "- Precio:", item['precio'], "- Calorías:", item['kcal'])
    else:
        print("No se encontraron items.")

def modificar_item_menu(menu: list, password: str) -> None:
    """
    Se debe preguntar por la contraseña, luego se selecciona un item del Menu y se modifican sus datos.
    """
    if not check_password(password):
        print("Contraseña incorrecta.")
        return
    revisar_menu(menu)
    seleccion = input("Seleccione el número del item a modificar: ")
    if seleccion.isdigit() and 0 < int(seleccion) <= len(menu):
        index = int(seleccion) - 1
        nuevo_nombre = input("Nuevo nombre para " + menu[index]['nombre'] + " (dejar vacío para no cambiar): ")
        nuevo_precio = input("Nuevo precio para " + menu[index]['nombre'] + " (dejar vacío para no cambiar): ")
        nuevas_kcal = input("Nuevas calorías para " + menu[index]['nombre'] + " (dejar vacío para no cambiar): ")
        nuevos_ingredientes = input("Nuevos ingredientes para " + menu[index]['nombre'] + " separados por coma (dejar vacío para no cambiar): ")
        
        if nuevo_nombre:
            menu[index]['nombre'] = nuevo_nombre
        if nuevo_precio:
            menu[index]['precio'] = int(nuevo_precio)
        if nuevas_kcal:
            menu[index]['kcal'] = float(nuevas_kcal)
        if nuevos_ingredientes:
            menu[index]['ingredientes'] = nuevos_ingredientes.split(',')

def agregar_item_menu(menu: list, password: str) -> None:
    """
    Se debe preguntar por la contraseña, luego se agrega un item al menú con todos los datos necesarios.
    """
    if not check_password(password):
        print("Contraseña incorrecta.")
        return
    nombre = input("Nombre del nuevo item: ")
    precio = int(input("Precio del nuevo item: "))
    kcal = float(input("Calorías del nuevo item: "))
    ingredientes = input("Ingredientes del nuevo item separados por coma: ").split(',')
    menu.append({'nombre': nombre, 'precio': precio, 'kcal': kcal, 'ingredientes': ingredientes})
    print("Item agregado al menú.")

def guardar_carrito(carrito: list, usuario: str) -> None:
    """
    Se guarda el carrito y el dueño del carrito en un archivo que sea “<nombre_usuario>.carrito”
    """
    with open(usuario + ".carrito", 'w') as file:
        for item in carrito:
            file.write(item['nombre'] + ';' + str(item['precio']) + ';' + str(item['kcal']) + ';' + ','.join(item['ingredientes']) + '\n')
    print("Carrito guardado.")

def cargar_carrito(usuario: str) -> list:
    """
    Se carga el carrito del usuario, si no existe el archivo, se inicia el programa de forma normal.
    """
    carrito = []
    try:
        with open(usuario + ".carrito", 'r') as file:
            for line in file:
                nombre, precio, kcal, ingredientes = line.strip().split(';')
                carrito.append({
                    'nombre': nombre,
                    'precio': int(precio),
                    'kcal': float(kcal),
                    'ingredientes': ingredientes.split(',')
                })
        print("Carrito cargado.")
    except FileNotFoundError:
        print("No se encontró un carrito guardado.")
    return carrito

def calcular_calorias(carrito: list) -> float:
    """
    Entrega el total de calorías de los ítems del carrito del usuario.
    """
    return sum(item['kcal'] for item in carrito)
def revisar_menu(menu: list) -> int:
    """
    Muestra el menú de comidas, con el precio. También permite seleccionar un item del menú para agregarlo al “carrito”.
    """
    print("Menú de Comidas:")
    for index, item in enumerate(menu):
        print(index + 1, item['nombre'], "- Precio:", item['precio'], "- Calorías:", item['kcal'])
    while True:
        seleccion = input("Seleccione un item para agregar al carrito (o presione Enter para volver): ")
        if seleccion == "":
            return None
        if seleccion.isdigit() and 0 < int(seleccion) <= len(menu):
            return int(seleccion) - 1
        print("Selección inválida. Por favor ingrese un número válido.")

def quitar_item_carrito(carrito: list) -> None:
    """
    Saca un objeto del carrito.
    """
    revisar_carrito(carrito)
    while True:
        seleccion = input("Seleccione el número del item a quitar: ")
        if seleccion.isdigit() and 0 < int(seleccion) <= len(carrito):
            carrito.pop(int(seleccion) - 1)
            print("Item removido del carrito.")
            return
        print("Selección inválida. Por favor ingrese un número válido.")

def obtener_opcion_usuario() -> str:
    """
    Solicita al usuario una opción del menú y asegura que sea un valor válido.
    """
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit() and 0 <= int(opcion) <= 13:
            return opcion
        print("Opción no válida, intente de nuevo.")



