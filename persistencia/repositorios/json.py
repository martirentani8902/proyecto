from dominio.servidor import Servidor
from pathlib import Path
import json

def servidor_a_diccionario(servidor: Servidor) -> dict:
    diccionario = {"nombre": servidor.nombre, "cpu": servidor.cpu, "estado": servidor.estado}
    return diccionario

def diccionario_a_servidor(diccionario: dict) -> Servidor:
    servidor = Servidor(diccionario["nombre"], diccionario["cpu"], diccionario["estado"])
    return servidor

def guardar(ruta: Path, servidores: list[Servidor]) -> None:
    lista_diccionarios = []
    for servidor in servidores:
        diccionario = servidor_a_diccionario(servidor)
        lista_diccionarios.append(diccionario)
    ruta.parent.mkdir(parents= True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)    
    
def cargar(ruta: Path) -> list[Servidor]:
    lista_servidores = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        for diccionario in datos:
            servidor = diccionario_a_servidor(diccionario)
            lista_servidores.append(servidor)
    except FileNotFoundError:
        pass
    return lista_servidores

def agregar(ruta: Path, servidor: Servidor) -> None:
    if isinstance(servidor, Servidor):
        with open(ruta, "r", encoding="utf-8") as archivo:
            lista_servidores = json.load(archivo)
        diccionario = servidor_a_diccionario(servidor)
        lista_servidores.append(diccionario)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_servidores, archivo, indent=4, ensure_ascii=False)
    else:
        raise ValueError("El dato no es un servidor")