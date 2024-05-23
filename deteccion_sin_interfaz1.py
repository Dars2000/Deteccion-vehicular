import subprocess
from subprocess import Popen
import io
from PIL import Image
import torch
import requests
import time
import threading

segundos = 1000

def obtener_segundos(num_detecciones):
    if num_detecciones > 30:
        return 50
    elif num_detecciones > 20:
        return 35
    elif num_detecciones > 10:
        return 30
    elif num_detecciones > 5:
        return 20
    elif num_detecciones > 2:
        return 15
    elif num_detecciones > 0:
        return 10
    else:
        return 0

def analyzePng(pngBytes, model):
    global segundos
    img = Image.open(io.BytesIO(pngBytes))
    model.classes = [2, 3, 7]  # Person, car, motorcycle, truck
    results = model(img)
    
    df = results.pandas().xyxy[0]
    df = df[df["confidence"] >= 0.4]
    num_new_detections = df.shape[0]
    
    print(f"Nuevas detecciones: {num_new_detections}")
    segundos = obtener_segundos(num_new_detections)
    print(f"Segundos: {segundos}")
    
    # Enviar los segundos a la API
    r = requests.post(f"http://192.168.95.190:5030/escribir_deteccion1?s={segundos}")

def detector():
    global segundos
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
    
    while True:
        try:
            ffmpeg_command = ["ffmpeg", "-rtsp_transport", "tcp", "-i", "rtsp://admin:prueba123@192.168.95.187/doc/page/preview.asp",
                              "-f", "image2pipe", "-c:v", "png", "-vf", "fps=2", "pipe:1"]
            
            pipe = Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)
            start = True
            currentPngBytes = bytes([])

            while pipe.poll() is None:
                readBytes = pipe.stdout.read(10**4)
                foundStartMarker = False

                for index in range(len(readBytes) - 8):
                    if (readBytes[index] == 137 and readBytes[index+1] == 80 and
                        readBytes[index+2] == 78 and readBytes[index+3] == 71 and
                        readBytes[index+4] == 13 and readBytes[index+5] == 10 and
                        readBytes[index+6] == 26 and readBytes[index+7] == 10):
                        foundStartMarker = True
                        if not start:
                            currentPngBytes += readBytes[:index]
                            analyzePng(currentPngBytes, model)
                            currentPngBytes = bytes([])
                        start = False
                        currentPngBytes += readBytes[index:]
                        break
                
                if not foundStartMarker:
                    currentPngBytes += readBytes

            print("Killing Pipeline")
            pipe.kill()
        
        except Exception as e:
            print(f"Error: {e}")
            print("Reintentando conexión en 5 segundos...")
            time.sleep(5)

def resultado():
    global segundos
    return segundos

if __name__ == '__main__':
    thread_detector = threading.Thread(target=detector)
    thread_resultado = threading.Thread(target=resultado)

    thread_detector.start()
    thread_resultado.start()

    thread_detector.join()
    thread_resultado.join()
