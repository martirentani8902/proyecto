from servidores import excepciones
from servidores.servidor import Servidor

def es_nombre_valido(nombre):
    if isinstance(nombre, str):
        nombre = nombre.strip()
        if nombre != '':
            try:
                numero = int(nombre)
            except ValueError:
                return True
            else:
                raise ValueError("El nombre no puede ser un numero")
        else:
            raise excepciones.NombreVacio("El nombre esta vacio")
    else:
        raise TypeError("El dato ingresado no es un nombre")
