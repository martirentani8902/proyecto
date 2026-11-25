from enum import StrEnum

class EstadoServidor(StrEnum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    MANTENIMIENTO = "mantenimiento"