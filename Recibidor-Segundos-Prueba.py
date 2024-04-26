import json
import time
import requests


x = requests.get('http://192.168.95.189:5030/leer')

print(x.text)