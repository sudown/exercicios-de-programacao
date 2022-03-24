import random

motos = random.randint(1,400)
carros = random.randint(1,400-motos)
onibus = (400-motos-carros)

print("Numeros do dia do estacionamento")
print(f"Numero de motos: {motos} com receita de: {motos*4:,.2f}")
print(f"Numero de carros: {carros} com receita de: {carros*8:,.2f}")
print(f"Numero de onibus: {onibus} com receita de: {onibus*20:,.2f}")
print(f"Receita totoal: {motos*4 + carros*8 + onibus*20:,.2f} R$")
