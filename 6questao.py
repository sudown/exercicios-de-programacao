#6 – Fazer um programa que gere 5 palpites para apostar na megasena
import random

contador = 0

while contador < 5:
    dezenas = [random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60)] #gera uma lista com as dezenas
    while 6 > (len(set(dezenas))): #mede o tamnho da lista descartando numeros iguais, ou seja se tiver 2 numeros iguais ele conta como apenas 1
        dezenas = [random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60)]
        
    print(dezenas[0], dezenas[1], dezenas[2], dezenas[3], dezenas[4], dezenas[5])
    contador = contador + 1
