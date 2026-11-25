from typing import Protocol
from dominio.servidor import Servidor

class RepositorioServidores(Protocol):

    def cargar(self) -> list[Servidor]:
        pass

    def guardar(self, servidores: list[Servidor]) -> None:
        pass

    # def agregar(self, servidor: Servidor) -> None:
    #     pass

    # def eliminar(self, nombre: str) -> None:
    #     pass
