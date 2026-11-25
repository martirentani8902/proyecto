from dominio import excepciones
from dominio.estados import EstadoServidor

def es_nombre_valido(nombre: str) -> bool:
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
            raise excepciones.NombreVacio("El nombre esta vacio.")
    else:
        raise excepciones.DatoNoEsString("El dato no es un string")

def es_cpu_valida(numero: int) -> bool:
    if type(numero) is int:
        if numero > 0:
            return True
        else:
            raise excepciones.EsNumeroNegativo("El numero no puede ser negativo")
    else:
        raise excepciones.DatoNoEsNumerico("El dato no es un entero")

def es_ram_valida(numero: int) -> bool:
    if type(numero) is int:
        if numero > 0:
            return True
        else:
            raise excepciones.EsNumeroNegativo("El numero no puede ser negativo")
    else:
        raise excepciones.DatoNoEsNumerico("El dato no es un entero")

def es_estado_valido(estado: str) -> bool:
    if type(estado) is str:
        if estado in EstadoServidor(estado):
            return True
        else:
            raise excepciones.EstadoInvalido("El estado es invalido")
    else:
        raise excepciones.DatoNoEsString("El dato no es un string")
    return type(estado) is str and estado in ESTADOS_SERVIDOR

