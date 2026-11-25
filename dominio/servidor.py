from dominio import validaciones
from dominio import excepciones
from dominio.estados import EstadoServidor

class Servidor:
    def __init__(self, nombre, cpu, ram, estado):
            if validaciones.es_nombre_valido(nombre):
                self._nombre = nombre
                self.cpu = cpu
                self.ram = ram
                try:
                    self._estado = EstadoServidor(estado.lower())
                except ValueError:
                    raise excepciones.EstadoInvalido("Estado invalido")
                else:
                    return None

    def __eq__(self, otro):
        if not isinstance(otro, Servidor):
            return NotImplemented
        return self.nombre == otro.nombre

    def __str__(self):
        return (f"Nombre: {self._nombre}\nCPU: {self._cpu}\nEstado: {self._estado}\n")

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def cpu(self) -> int:
        return self._cpu

    @cpu.setter
    def cpu(self, numero: int) -> None:
        try:
            validaciones.es_cpu_valida(numero)
        except excepciones.DatoNoEsNumerico:
            try:
                num = int(numero)
            except ValueError:
                raise ValueError("La CPU debe ser un numero entero")
            else:
                if num > 0:
                    self._cpu = num
                else:
                    raise excepciones.EsNumeroNegativo("La CPU no puede ser negativa")
        else:
            self._cpu = numero

    @property
    def ram(self) -> int:
        return self._ram

    @ram.setter
    def ram(self, numero: int) -> None:
        try:
            validaciones.es_ram_valida(numero)
        except excepciones.DatoNoEsNumerico:
            try:
                num = int(numero)
            except ValueError:
                raise excepciones.DatoNoEsNumerico("La RAM tiene que ser un numero")
            else:
                if num > 0:
                    self._ram = num
                else:
                    raise excepciones.EsNumeroNegativo("La cantidad de RAM no puede ser negativa")
        else:
            self._ram = numero

    def cambiar_nombre(self, nombre) -> None:
        if nombre.strip != "":
            if not nombre.isdigit():
                self._nombre = nombre
            else:
                raise excepciones.DatoNoEsString("El nombre no puede ser un numero")     
        else:
            raise excepciones.NombreVacio("El nombre no puede estar vacio")
    
    def desactivar(self) -> None:
        self._estado = "inactivo"

    def activar(self) -> None:
        self._estado = "activo"

    def poner_en_mantemiento(self) -> None:
        self._estado = "mantenimiento"

    def cambiar_estado(self, estado: str) -> None:
        if isinstance(estado, str):
            match estado:
                case "activo":
                    self.activar()
                case "inactivo":
                    self.desactivar()
                case "mantenimiento":
                    self.poner_en_mantemiento()
                case _:
                    raise excepciones.EstadoInvalido
        else:
            raise excepciones.DatoNoEsString
