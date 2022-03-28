'''Metal Gear Solid, Driver, Crash Bandicoot, Crash Bandicoot, Warped,
Tekken 3, Crash Bandicoot, Cortex Strikes Back, Final Fantasy VIII, Gran Turismo 2, Final
Fantasy VII e Gran Turismo.'''

import random

jogos = [random.randint(0,0) for n in range(0,10)]
#print(jogos,"\n")

for i in range(0,10):
    for j in range(0,35):
        jogos[i] = jogos[i] + random.randint(1,5)

mgsv = jogos[0]/35
driver = jogos[1]/35
crash1 = jogos[2]/35
crash2 = jogos[3]/35
crash3 = jogos[4]/35
tekken = jogos[5]/35
ff8 = jogos[6]/35
ff7 = jogos[7]/35
gt2 = jogos[8]/35
gt = jogos[9]/35



print('Metal Gear Solid V',round(mgsv, 1),'★\nCrash Bandicoot',round(crash1, 1),'★\nCrash Bandicoot Cortex Strikes Back',round(crash2, 1),'★\nCrash Bandicoot Warped',round(crash3, 1),'★\nTekken 3',round(tekken, 1),'★\nDriver',round(driver, 1),'★\nFinal Fantasy VII', round(ff7, 1), '★\nFinal Fanstasy VIII',round(ff8, 1),'★\nGrand Turismo',round(gt,1),'★\nGrand Turismo 2',round(gt2, 1),'★')