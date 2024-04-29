import uvicorn
from fastapi import FastAPI
import threading

app = FastAPI(
    title="Segundos",
    version="0.0.1",
)

segundos = None
lock = threading.Lock()
actualizacion_reciente = False

def reset_segundos():
    global segundos
    global lock
    global actualizacion_reciente
    lock.acquire()
    if not actualizacion_reciente:
        segundos = None
    actualizacion_reciente = False
    lock.release()

def start_reset_timer():
    threading.Timer(2, reset_segundos).start()

@app.post("/escribir")
def escribir_segundos(s: int):
    global segundos
    global lock
    global actualizacion_reciente
    lock.acquire()
    segundos = s
    actualizacion_reciente = True
    lock.release()

@app.get("/leer")
def leer_segundos():
    global segundos
    global lock
    global actualizacion_reciente
    lock.acquire()
    s = segundos
    actualizacion_reciente = True
    lock.release()
    start_reset_timer()
    return s

if __name__ == "__main__":
    uvicorn.run("API-Prueba:app", host="localhost", port=5030, log_level="info", reload=True)
