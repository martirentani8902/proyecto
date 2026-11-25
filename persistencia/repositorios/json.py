from pathlib import Path
from dominio.servidor import Servidor
from app.repositorio import RepositorioServidores
import json

def servidor_a_diccionario(servidor: Servidor) -> dict:
    diccionario = {"nombre": servidor.nombre, 
                   "cpu": servidor.cpu, 
                   "ram":  servidor.ram,
                   "estado": servidor.estado
                    }
    return diccionario

def diccionario_a_servidor(diccionario: dict) -> Servidor:
    servidor = Servidor(diccionario["nombre"], 
                        diccionario["cpu"],
                        diccionario["ram"], 
                        diccionario["estado"])
    return servidor


class RepositorioServidoresJson(RepositorioServidores):

    def __init__(self, ruta: Path):
        self._ruta = ruta

    @property
    def ruta(self):
        return self._ruta

    def guardar(self, servidores: list[Servidor]) -> None:
        lista_diccionarios = []
        for servidor in servidores:
            diccionario = servidor_a_diccionario(servidor)
            lista_diccionarios.append(diccionario)
        self._ruta.parent.mkdir(parents= True, exist_ok=True)
        with open(self._ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)    
        
    def cargar(self) -> list[Servidor]:
        lista_servidores = []
        try:
            with open(self._ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            for diccionario in datos:
                servidor = diccionario_a_servidor(diccionario)
                lista_servidores.append(servidor)
        except FileNotFoundError:
            pass
        return lista_servidores
