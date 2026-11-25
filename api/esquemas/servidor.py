from typing import Literal
from pydantic import BaseModel, ConfigDict, Field
from dominio.estados import EstadoServidor

class ServidorEntrada(BaseModel):
    nombre: str = Field(min_length=1)
    cpu: int = Field(gt=0, strict=True)
    ram: int = Field(gt=0, strict=True)
    estado: EstadoServidor

class ServidorRespuesta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str = Field(min_length=1)
    cpu: int = Field(gt=0, strict=True)
    ram: int = Field(gt=0, strict=True)
    estado: EstadoServidor

class ServidorCambioEntrada(BaseModel):
    nombre: str | None = None
    cpu: int | None = None
    ram: int | None = None
    estado: EstadoServidor | None = None