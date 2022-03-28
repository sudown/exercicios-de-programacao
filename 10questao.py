#S = - 1 - 2 + 3 + 4 - 5 - 6 + 7 + 8 ...

resp = 0
s = [n for n in range(1, 51)]
#print(s)

for i in range(1, 51, 4): #pula os termos de quatro em quatro ja que a cada quatro numeros os sinal deles se mantem
    resp = resp - i     #i-1 necessário porque a primeira posição da lista é 0 ou seja sem o -1 os numeros seriam colocados uma posição a frente da posição que eles deveriam ficar
    s[i-1] = -i
for j in range(2, 51, 4):
    resp = resp - j
    s[j-1] = - j
for k in range(3, 51, 4):
    resp = resp + k
    s[k-1] = k
for l in range(4, 51, 4):
    resp = resp + l
    s[l-1] = l

print(s)
print("A soma dos 50 primeiros termos da",resp)
