from pathlib import Path
from app.servicio_servidores import ServicioServidores
from persistencia.repositorios.json import RepositorioServidoresJson

def obtener_servicio() -> ServicioServidores:
    ruta = Path("datos/servidores.json")
    repositorio = RepositorioServidoresJson(ruta)
    return ServicioServidores(repositorio)
