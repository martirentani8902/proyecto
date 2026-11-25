from typing import Protocol
from dominio.servidor import Servidor

class RepositorioServidores(Protocol):

    def cargar(self) -> list[Servidor]:
        ...

    def guardar(self, servidores: list[Servidor]) -> None:
        ...
