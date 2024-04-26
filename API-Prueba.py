import uvicorn
from fastapi import FastAPI

segundos = 10

app = FastAPI(
    title="Segundos",
    version="0.0.1",
    # openapi_url=""
)

@app.post("/escribir")
def EscribirSegundos(s: int):
    global segundos
    segundos = s

@app.get("/leer")
def LeerSegundos():
    global segundos
    return segundos

if __name__ == "__main__":
    uvicorn.run("segundos_api:app", host="localhost", port=5030, log_level="info", reload=True)