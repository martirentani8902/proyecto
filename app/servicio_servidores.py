from dominio.servidor import Servidor
from app.repositorio import RepositorioServidores
from dominio.administrador import Administrador
from dominio import excepciones
from dominio.estados import EstadoServidor

class ServicioServidores:
    def __init__(self, repositorio: RepositorioServidores):
        self._repositorio = repositorio


    def agregar_servidor(self, servidor: Servidor) -> None:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        admin.agregar_servidor(servidor)
        self._repositorio.guardar(admin.obtener_servidores())

    def eliminar_servidor(self, nombre: str) -> None:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        admin.eliminar_servidor(nombre)
        self._repositorio.guardar(admin.obtener_servidores())

    def buscar_servidor(self, nombre: str) -> Servidor:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        return admin.buscar_servidor(nombre)

    def existe_servidor(self, nombre: str) -> bool:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        return admin.existe_servidor(nombre)

    def listar_servidores(self) -> list[Servidor]:
        return self._repositorio.cargar()

    def listar_servidores_activos(self) -> list[Servidor]:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        return admin.obtener_servidores_activos()

    def listar_servidores_inactivos(self) -> list[Servidor]:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        return admin.obtener_servidores_inactivos()

    def listar_servidor_mantenimiento(self) -> list[Servidor]:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        return admin.obtener_servidores_mantenimiento()

    def modificar_servidor(self, nombre_servidor: str, 
                           nuevo_nombre: str | None = None,
                           nueva_cpu: int | None = None,
                           nueva_ram: int | None = None,
                           nuevo_estado: EstadoServidor | None = None
                        ) -> None:
        inventario = self._repositorio.cargar()
        admin = Administrador(inventario)
        servidor = admin.buscar_servidor(nombre_servidor)
        for otro_servidor in admin.obtener_servidores():
            if otro_servidor is not servidor:
                if otro_servidor.nombre == nuevo_nombre:
                    raise excepciones.ServidorDuplicado
        if nuevo_nombre is not None:
            servidor.cambiar_nombre(nuevo_nombre)
        if nueva_cpu is not None:
            servidor.cpu = nueva_cpu
        if nueva_ram is not None:
            servidor.ram = nueva_ram
        if nuevo_estado is not None:
            servidor.cambiar_estado(nuevo_estado.value)
        servidores = admin.obtener_servidores()
        self._repositorio.guardar(servidores)

