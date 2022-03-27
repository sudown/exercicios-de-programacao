import random

terras = [random.randint(1,30), random.randint(1,30), random.randint(1,30)]

while len(set(terras)) < 3:
    terras = [random.randint(1,30), random.randint(1,30), random.randint(1,30)]

print("A primeira terra tem", terras[0],"vibros")
print("A segunda terra tem", terras[1],"vibros")
print("A terceira terra tem", terras[2],"vibros")