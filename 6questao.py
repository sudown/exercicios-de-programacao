#6 – Fazer um programa que gere 5 palpites para apostar na megasena
import random

dezenas = [random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60)]

while 6 > (len(set(dezenas))):
    dezenas = [random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60)]
    
print(dezenas[0], dezenas[1], dezenas[2], dezenas[3], dezenas[4], dezenas[5])
