
base = int(input("Digite a base da potencia: "))
expoente = int(input("Digite o expoente da potencia: "))
resp = base

for i in range(0,expoente):
    resp = resp + (resp*base) - base

print(resp)