from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from config import BASE_DIR
from api.routers.servidores import router as servidores_router

RUTA_FRONTEND = BASE_DIR / "frontend"

app = FastAPI()

app.include_router(servidores_router)

app.mount(
    "/frontend",
    StaticFiles(directory=RUTA_FRONTEND),
    name="frontend"
)

@app.get("/", include_in_schema=False)
def pagina_principal():

    return FileResponse(
        RUTA_FRONTEND / "index.html"
    )