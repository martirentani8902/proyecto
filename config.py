import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos"
RUTA_DOMINIO = BASE_DIR / "dominio"
RUTA_PRESENTACION = BASE_DIR / "presentacion"

TIPO_REPOSITORIO = os.getenv("TIPO_REPOSITORIO", "json")

RUTA_JSON = Path(os.getenv("RUTA_JSON", str(BASE_DIR / "datos/servidores.json")))

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")