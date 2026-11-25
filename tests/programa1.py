from servidores.modelos import Servidor
import prueba
from pathlib import Path

RUTA = Path("datos/servidores.json")

servidor1 = Servidor("web-01", 2, "activo")
servidor2 = Servidor("db-01", 8, "activo")

servidores = [servidor1, servidor2]

prueba.guardar_servidores(RUTA, servidores)


