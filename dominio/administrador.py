import excepciones
from dominio.servidor import Servidor
from persistencia.repositorios import json
from validaciones import es_nombre_valido, es_servidor
from pathlib import Path
from copy import copy
from app.repositorio import RepositorioServidores


class administrador:
    def __init__(self, repositorio: RepositorioServidores):
        self.repositorio = repositorio

    @property
    def repositorio(self):
        return copy(self.repositorio)

    def cargar_servidores(self, servidores: list[Servidor]) -> None:
        if isinstance(servidores, list[Servidor]):
            self.repositorio.guardar(servidores)

    def agregar_servidor(self, servidor):
        if isinstance(servidor, Servidor):
            if servidor in self.repositorio.cargar():
                raise excepciones.ServidorYaEstaEnLista("El servidor ya esta en la lista")
            else:
                self.repositorio.agregar(servidor)
        else:
            raise TypeError("El objeto pasado no es un servidor")

    def eliminar_servidor(self, nombre):
        if es_nombre_valido(nombre):
            for indice, servidor in enumerate(self.repositorio.cargar()):
                if servidor.nombre == nombre:
                    self._servidores.pop(indice)
                    break
            else:
                raise excepciones.ServidorNoEncontrado("No se encontro el servidor", nombre)

    def buscar_servidor(self, nombre):
        for servidor in self.repositorio.cargar():
            if servidor.nombre == nombre:
                return servidor
        raise excepciones.ServidorNoEncontrado("Servidor no encontrado")

    def obtener_servidores_activos(self):
        lista_activos = []
        for servidor in self._servidores:
            if servidor.estado == "activo":
                lista_activos.append(servidor)
        return lista_activos

    def mostrar_inventario(self):
        for servidor in self._servidores:
            print(servidor)

    

