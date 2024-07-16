def get_password () -> str:
	"""
		Entrega la contraseña guardad en el archivo 'password.pwd'
		Solo funciona si password.pwd tiene una linea de texto. Lee la primera linea y la devuelve sin saltos de linea.
	"""
	file = open('password.pwd','r')
	password = file.readline().replace('\n','')
	file.close()
	return password

def check_password (password:str) -> bool:
	"""
		Verifica que la 'password' que se ingresa corresponda a la contraseña guardada en el archivo 'password.pwd'
	"""
	if (password == get_password()):
		return True
	return False

def load_items (file_name:str) -> list[dict]:
	"""
		Lee un archivo .csv y convierte el contenido en un diccionario.
		El formato del diccionario es:
			nombre : str,
			precio : int,
			kcal : float,
			ingredientes : list[str]
	"""
	file = open(file_name,'r')
	menu = []
	llaves = file.readline().replace('\n','').split(';')
	while(True):
		valores = file.readline().replace('\n','').split(';')
		if (valores == ['']):
			break
		menu.append({
			llaves[0]:valores[0], #nombre
			llaves[1]:int(valores[1]), #precio
			llaves[2]:float(valores[2]), #kcal
			llaves[3]:str(valores[3]).split(','), #ingredientes
			#mas llaves deben ser agregadas a mano
		})


	file.close()
	
	return menu
	
var = load_items('menu.csv')

def validar_seleccion (sel, lista:list) -> bool:
	if (str(sel).isnumeric()):
		if (int(sel) in range(len(lista)+1)):
			return True
	return False
