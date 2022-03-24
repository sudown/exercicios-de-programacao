from email.contentmanager import raw_data_manager
import random

velocistas = ["jesse quick","barry allen","wally west","dr whells","jay garrick","max mercury"]
velocidade = random.randint(1,10)

print("O vencedor foi, ",velocistas[random.randint(0,5)], " com ",velocidade," flashs de velocidade ou ",velocidade*300000,"Km/s")