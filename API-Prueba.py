import uvicorn
from fastapi import FastAPI
import threading

app = FastAPI(
    title="Segundos",
    version="0.0.1",
)

deteccion1 = None
lock_deteccion1 = threading.Lock()
timer_deteccion1 = None

deteccion2 = None
lock_deteccion2 = threading.Lock()
timer_deteccion2 = None

deteccion3 = None
lock_deteccion3 = threading.Lock()
timer_deteccion3 = None

deteccion4 = None
lock_deteccion4 = threading.Lock()
timer_deteccion4 = None

def reset_deteccion1():
    global deteccion1
    with lock_deteccion1:
        deteccion1 = None

def reset_deteccion2():
    global deteccion2
    with lock_deteccion2:
        deteccion2 = None
        
def reset_deteccion3():
    global deteccion3
    with lock_deteccion3:
        deteccion3 = None
        
def reset_deteccion4():
    global deteccion4
    with lock_deteccion4:
        deteccion4 = None

def start_reset_timer_deteccion1():
    global timer_deteccion1
    timer_deteccion1 = threading.Timer(3, reset_deteccion1)
    timer_deteccion1.start()

def start_reset_timer_deteccion2():
    global timer_deteccion2
    timer_deteccion2 = threading.Timer(3, reset_deteccion2)
    timer_deteccion2.start()
    
def start_reset_timer_deteccion3():
    global timer_deteccion3
    timer_deteccion3 = threading.Timer(3, reset_deteccion3)
    timer_deteccion3.start()

def start_reset_timer_deteccion4():
    global timer_deteccion4
    timer_deteccion4 = threading.Timer(3, reset_deteccion4)
    timer_deteccion4.start()

@app.post("/escribir_deteccion1")
def escribir_deteccion1(s: int):
    global deteccion1, timer_deteccion1
    with lock_deteccion1:
        deteccion1 = s
    if timer_deteccion1:
        timer_deteccion1.cancel()
    start_reset_timer_deteccion1()
    return {"message": "Detección 1 actualizada"}

@app.post("/escribir_deteccion2")
def escribir_deteccion2(s: int):
    global deteccion2, timer_deteccion2
    with lock_deteccion2:
        deteccion2 = s
    if timer_deteccion2:
        timer_deteccion2.cancel()
    start_reset_timer_deteccion2()
    return {"message": "Detección 2 actualizada"}

@app.post("/escribir_deteccion3")
def escribir_deteccion3(s: int):
    global deteccion3, timer_deteccion3
    with lock_deteccion3:
        deteccion3 = s
    if timer_deteccion3:
        timer_deteccion3.cancel()
    start_reset_timer_deteccion3()
    return {"message": "Detección 3 actualizada"}

@app.post("/escribir_deteccion4")
def escribir_deteccion4(s: int):
    global deteccion4, timer_deteccion4
    with lock_deteccion4:
        deteccion4 = s
    if timer_deteccion4:
        timer_deteccion4.cancel()
    start_reset_timer_deteccion4()
    return {"message": "Detección 4 actualizada"}

@app.get("/leer_deteccion1")
def leer_deteccion1():
    global deteccion1
    with lock_deteccion1:
        d = deteccion1
    return d

@app.get("/leer_deteccion2")
def leer_deteccion2():
    global deteccion2
    with lock_deteccion2:
        d = deteccion2
    return d

@app.get("/leer_deteccion3")
def leer_deteccion3():
    global deteccion3
    with lock_deteccion3:
        d = deteccion3
    return d

@app.get("/leer_deteccion4")
def leer_deteccion4():
    global deteccion4
    with lock_deteccion4:
        d = deteccion4
    return d

if __name__ == "__main__":
    uvicorn.run("API-Prueba:app", host="192.168.95.190", port=5030, log_level="info", reload=True)
