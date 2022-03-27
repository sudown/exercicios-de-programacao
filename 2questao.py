
from ast import expr_context


while True:
    try:
        base = int(input("Digite a base da potencia: "))
        expoente = int(input("Digite o expoente da potencia: "))
        resp = base
        break
    except ValueError:
        print("Digite apenas numeros")
    except KeyboardInterrupt:
        print("Goodbye friend")
        exit()

for i in range(1,abs(expoente)):
    resp = resp*base    #resp = base^expoente

if expoente < 0:    #se 
    resp = 1 / resp  #resp = 1 / resp 'anterior'

if expoente == 0: #qualquer numero elevado a 0 da 1
    resp = 1

print("Resposta igual:",resp)