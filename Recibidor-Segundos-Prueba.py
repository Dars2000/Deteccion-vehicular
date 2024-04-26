import json
import time
import requests


x = requests.get('http://localhost:5030/leer')

print(x.text)
