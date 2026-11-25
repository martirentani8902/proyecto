from servidores import operaciones
from servidores.modelos import Servidor
from servidores import excepciones

def calcular_cpu_activa(servidores):
    lista_activos = operaciones.obtener_servidores_activos(servidores)
    suma = 0
    for servidor in lista_activos:
        suma += servidor.cpu
    return suma

def contar_servidores(servidores):
    if len(servidores) > 0: 
        inventario = {}
        inventario["total"] = 0
        inventario["activos"] = 0
        inventario["inactivos"] = 0
        for servidor in servidores:
            inventario["total"] += 1
            if servidor.estado == "activo":
                inventario["activos"] += 1
            else:
                inventario["inactivos"] += 1
        return inventario
    else:
        raise excepciones.ListaVacia("No hay servidores")

