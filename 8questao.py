import random

########################################## 1 DISPUTA ###########################################

loki_comeu = random.randint(1,100) #gerando a quantidade de comida ingerada pelos competidores
volstagg_comeu = random.randint(1,100)
vitorias = 0    #vitorias de Loki

while loki_comeu == volstagg_comeu:
    volstagg_comeu = random.randint(1,100)  # para evitar empates se os valores forem iguais eles são gerados novamente

if loki_comeu > volstagg_comeu:
    print("Loki venceu a primeira disputa, comendo",loki_comeu,"Kg, contra",volstagg_comeu,"Kg de Volstagg\n")
    vitorias = vitorias + 1

else:
    print("loki perdeu a primeira disputa, comendo",loki_comeu,"Kg, contra",volstagg_comeu,"Kg de Loki\n")

########################################## 2 DISPUTA ###########################################

disparos_loki = [random.randint(0,60) for n in range(0,10)] #gerando os disparos dos competidores
disparos_frandral = [random.randint(0,60) for n in range(0,10)]

pontos_loki = 0
pontos_frandral = 0
acertos_loki = 0
acertos_frandral = 0

while pontos_loki == pontos_frandral:
    for i in disparos_loki:
        if i < 51:
            pontos_loki = pontos_loki + i
            acertos_loki = acertos_loki + 1

    for i in disparos_frandral:
        if i < 51:
            pontos_frandral = pontos_frandral + i
            acertos_frandral = acertos_frandral + 1


if pontos_loki < pontos_frandral:
    print("Loki venceu a segunda disputa com",acertos_loki,"acertos somando",pontos_loki,"pontos contra",pontos_frandral,"pontos de Frandral\n")
    vitorias = vitorias + 1

else:
    print("Loki perdeu a segunda desputa com",acertos_loki,"acertos somando",pontos_loki,"pontos contra", pontos_frandral,"pontos de Frandral\n")

########################################## 3 DISPUTA ###########################################

if random.randint(0,1) == 1: #1 loki ganha 0 loki perde
    print("loki venceu a terceira disputa na batalha de polegar contra Hogun\n")
    vitorias = vitorias + 1

else:
    print("Loki perdeu a terceira disputa na batalha de polegar contra Hogun\n")

########################################## 4 DISPUTA ###########################################

par_loki = False
par_valquiria = False


while par_loki == False and par_valquiria == False:
    num1_loki = random.randint(1,20)
    num2_loki = random.randint(1,20)
    num1_valquiria = random.randint(1,20)
    num2_valquiria = random.randint(1,20)

    if num1_loki == num2_loki:
        par_loki = True

    elif num1_valquiria == num2_valquiria:
        par_valquiria = True

if par_loki == True:
    print("Loki venceu a quarta disputa, tirando os numeros", num1_loki, num2_loki,"enquanto valquiria tirou", num1_valquiria, num2_valquiria)
    vitorias = vitorias + 1

else:
    print("Loki perdeu a quarta disputa, tirando os numeros", num1_loki, num2_loki,"enquanto valquiria tirou", num1_valquiria, num2_valquiria)

########################################## 5 DISPUTA ###########################################
golpes_loki = 0
golpes_sif = 0

print("Loki fara 2 ataques\n")
for i in range(0,3):
    ataque = random.randint(1,20)
    defesa = random.randint(1,20)

    if (ataque % 2 == 0 and defesa % 2 != 0) or (ataque % 2 != 0 and defesa % 2 == 0):
        print("Loki tirou", ataque,"e Lady Sif tirou", defesa,". Com isso loki acerta um golpe em Lady Sif")
        golpes_loki = golpes_loki + 1

    else:
        print("Loki tirou", ataque,"e Lady Sif tirou", defesa,". Com isso loki erra um golpe em Lady Sif que se esquiva")

print("\nVez de Lady Sif atacar\n")
for i in range(0,3):
    ataque = random.randint(1,20)
    defesa = random.randint(1,20)

    if (ataque % 2 == 0 and defesa % 2 != 0) or (ataque % 2 != 0 and defesa % 2 == 0):
        print("Lady Sif tirou", ataque,"e Loki tirou", defesa,". Com isso Lady Sif acerta um golpe em Loki")
        golpes_sif = golpes_sif + 1

    else:
        print("Lady Sif tirou", ataque,"e Loki tirou", defesa,". Com isso Lady Sif erra um golpe em Loki que se esquiva")

print("\n")

if golpes_sif < golpes_loki:
    print("Assim sendo Loki vence a quinta disputa contra Lady Sif acertando",golpes_loki,"e levando", golpes_sif,"\n")
    vitorias = vitorias + 1

else:
    print("Assim sendo Loki perdeu a quinta disputa contra Lady Sif acertando",golpes_loki,"e levando",golpes_sif,"\n")


if vitorias > 2:
    print("Somando as disputas Loki fica com",vitorias,"vitorias e é nomeado protetor")

elif vitorias == 2:
    print("E com apenas 2 vitorias Loki perd... Esperem é chegada a noticia de que em razão do fimbulwinter esse ano 2 vitorias bastaram. Assim Loki vence e é nomeado protetor")

else:
    print("Somando as disputas Loki fica com",vitorias,"vitorias e não é nomeado protetor")