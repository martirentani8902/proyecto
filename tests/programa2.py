import prueba
from servidores.modelos import Servidor
from pathlib import Path

RUTA = Path("datos/servidores.json")

lista_servidores = prueba.cargar_servidores(RUTA)

lista_servidores[0].desactivar()

prueba.guardar_servidores(RUTA, lista_servidores)





