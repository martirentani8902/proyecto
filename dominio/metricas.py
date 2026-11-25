from dominio.servidor import Servidor
from dominio import excepciones
from dominio.administrador import Administrador

def calcular_cpu_activa(admin):
    lista_activos = admin.obtener_servidores_activos()
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
        raise excepciones.ListaVacia

