from typing import Literal, Annotated
from fastapi import APIRouter, Depends, Query, Path, status, HTTPException
from pydantic import BaseModel, Field, ConfigDict
from persistencia.repositorios.json import servidor_a_diccionario
from app.servicio_servidores import ServicioServidores
from dominio.servidor import Servidor
from dominio import excepciones
from dominio.estados import EstadoServidor
from api.dependencias import obtener_servicio
from api.esquemas.servidor import (ServidorRespuesta, ServidorEntrada, ServidorCambioEntrada)
import json

router = APIRouter(prefix="/servidores")

@router.get("/", response_model=list[ServidorRespuesta])
def listar_servidores(servicio: ServicioServidores = Depends(obtener_servicio), 
                      estado: Annotated[
                          EstadoServidor | None, 
                          Query(description="Filtrar servidores por estado")
                          ] = None
                        ):
    if estado is None:
        return servicio.listar_servidores()
    elif estado == "activo":
        return servicio.listar_servidores_activos()
    elif estado == "inactivo":
        return servicio.listar_servidores_inactivos()
    elif estado == "mantenimiento":
        return servicio.listar_servidor_mantenimiento()
    else:
        raise HTTPException(
            status_code = 422,
            detail = f"El estado {estado} no existe"
        )

@router.post("/", status_code=status.HTTP_201_CREATED)
def agregar_servidor(datos: ServidorEntrada, 
                     servicio: ServicioServidores = Depends(obtener_servicio)
                     ):
    try:
        servidor = Servidor(datos.nombre, datos.cpu, datos.ram, datos.estado)
    except(excepciones.NombreVacio, 
           ValueError, 
           excepciones.EsNumeroNegativo, 
           excepciones.DatoNoEsNumerico,
           excepciones.EstadoInvalido
           ) as error:
        raise HTTPException (
            status_code = 422,
            detail = str(error)
        )
    else:
        try:
            servicio.agregar_servidor(servidor)
        except excepciones.ServidorYaEstaEnLista:
            raise HTTPException(
                status_code = 409,
                detail = "El servidor ya esta registrado"
            )
        else:
            return {"mensaje": "Servidor creado"}

@router.get("/{nombre}", response_model=ServidorRespuesta)
def buscar_servidor(nombre: Annotated[str, Path(min_length=1)], servicio: ServicioServidores = Depends(obtener_servicio), 
                    ):
    try:
        servidor = servicio.buscar_servidor(nombre)
    except excepciones.ServidorNoEncontrado as error:
        raise HTTPException(
            status_code = 404,
            detail = str(error)
        )
    return servidor

@router.delete("/{nombre}")
def eliminar_servidor(nombre: Annotated[str, Path(min_length=1)],
                      servicio: ServicioServidores = Depends(obtener_servicio)
                    ):
    try:
        servicio.eliminar_servidor(nombre)
    except (excepciones.ServidorNoEncontrado):
        raise HTTPException(
            status_code = 404,
            detail = f"El servidor {nombre} no fue encontrado"
        )
    except excepciones.NombreVacio:
        raise HTTPException(
            status_code = 400,
            detail = "El nombre del servidor esta vacio"
        )
    else:
        return {"mensaje": "Servidor eliminado correctamente"}

@router.patch("/{nombre}", status_code=204)
def modificar_servidor(
    nombre: Annotated[
        str,
        Path(min_length=1, description="Nombre del servidor")
    ],
    datos: ServidorCambioEntrada,
    servicio: ServicioServidores = Depends(obtener_servicio)
):
    try:
        servicio.modificar_servidor(
            nombre_servidor=nombre,
            nuevo_nombre=datos.nombre,
            nueva_cpu=datos.cpu,
            nueva_ram=datos.ram,
            nuevo_estado=datos.estado
        )

    except excepciones.ServidorDuplicado:
        raise HTTPException(
            status_code=409,
            detail=f"Ya hay un servidor con nombre {datos.nombre}"
        )

    except excepciones.ServidorNoEncontrado:
        raise HTTPException(
            status_code = 404,
            detail = f"El servidor {nombre} no fue encontrado"
        )

    except (
        excepciones.DatoNoEsString,
        excepciones.NombreVacio,
        excepciones.DatoNoEsNumerico,
        excepciones.EsNumeroNegativo,
        excepciones.EstadoInvalido
    ) as error:
        raise HTTPException(
            status_code=422,
            detail=str(error) or "Datos inválidos"
        )






