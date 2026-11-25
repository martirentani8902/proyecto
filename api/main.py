from fastapi import FastAPI
from api.routers.servidores import router as servidores_router

app = FastAPI()

app.include_router(servidores_router)

@app.get("/")
def root():
    return {"message": "Hello World"}