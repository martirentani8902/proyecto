from dominio import excepciones
from dominio.servidor import Servidor
from dominio.validaciones import es_nombre_valido
import copy


class Administrador:
    def __init__(self, servidores: list[Servidor]):
        for indice, servidor in enumerate(servidores):
            if not isinstance(servidor, Servidor):
                raise TypeError
            if servidor in servidores[indice+1:]:
                raise ValueError("Servidor duplicado")
        copia = copy.copy(servidores)
        self._servidores = copia

    def obtener_servidores(self) -> list[Servidor]:
        return copy.copy(self._servidores)

    def agregar_servidor(self, servidor: Servidor) -> None:
        if isinstance(servidor, Servidor):
            if servidor in self._servidores:
                raise excepciones.ServidorYaEstaEnLista
            else:
                self._servidores.append(servidor)
        else:
            raise TypeError("Tipo de dato invalido.")

    def eliminar_servidor(self, nombre: str) -> None:
        if es_nombre_valido(nombre):
            for indice, servidor in enumerate(self._servidores):
                if servidor.nombre == nombre:
                    self._servidores.pop(indice)
                    break
            else:
                raise excepciones.ServidorNoEncontrado("El servidor no existe.")

    def buscar_servidor(self, nombre: str) -> Servidor:
        if isinstance(nombre, str):
            if nombre.strip() != '':
                for servidor in self._servidores:
                    if servidor.nombre == nombre:
                        return servidor
                raise excepciones.ServidorNoEncontrado
            else:
                raise ValueError
        else:
            raise TypeError

    def existe_servidor(self, nombre_buscado: str) -> bool:
        for servidor in self._servidores:
            if servidor.nombre == nombre_buscado:
                return True
        return False

    def obtener_servidores_activos(self) -> list[Servidor]:
        lista_activos = []
        for servidor in self._servidores:
            if servidor.estado == "activo":
                lista_activos.append(servidor)
        return lista_activos

    def obtener_servidores_inactivos(self) -> list[Servidor]:
        lista_inactivos = []
        for servidor in self._servidores:
            if servidor.estado == "inactivo":
                lista_inactivos.append(servidor)
        return lista_inactivos

    def obtener_servidores_mantenimiento(self) -> List[Servidor]:
        lista_mantenimiento = []
        for servidor in self._servidores:
            if servidor.estado == "mantenimiento":
                lista_mantenimiento.append(servidor)
        return lista_mantenimiento

    

