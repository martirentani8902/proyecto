from pathlib import Path
from config import (TIPO_REPOSITORIO, RUTA_JSON, DATABASE_URL)
from app.servicio_servidores import ServicioServidores
from persistencia.repositorios.json import RepositorioServidoresJson
from persistencia.repositorios.postgres import RepositorioServidoresPostgres

def obtener_repositorio():
    if TIPO_REPOSITORIO == "json":
        return RepositorioServidoresJson(RUTA_JSON) 

    elif TIPO_REPOSITORIO == "postgres":
        if not DATABASE_URL:
                raise ValueError("DATABASE_URL no configurada")
        return RepositorioServidoresPostgres(DATABASE_URL)
        
    raise ValueError("Tipo de repositorio desconocido")

def obtener_servicio() -> ServicioServidores:
    repositorio = obtener_repositorio()
    return ServicioServidores(repositorio)


