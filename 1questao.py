
import random

jesse_quick = random.randint(1,10)
barry_allen = random.randint(1,10)
wally_west = random.randint(1,10)
dr_whells = random.randint(1,10)
jay_garrick = random.randint(1,10)
max_mercury = random.randint(1,10)

vencedor1 = ""
vencedor2 = ""
vencedor3 = ""
velocidade1 = ""
velocidade2 = ""
velocidade3 = ""

print("-----------------------------CORRIDA DA DC-----------------------------")
print("-----------------------------PARTICIPANTES-----------------------------\r\n")
print("Jesse Quick, Barry Allen, Barry Allen, Dr. Wells, Jay Garrick e Max Mercury")

#print("                                                           \n                                    ;r                      \n                        ;lyG88G3 ;%T                       \n                      ig@@gAextF!%@;3i                      \n                    v@@8*     ,8@@__U@@l                    \n                   8@@,     _8@@8_^r_-8@8                   \n                  5@@-    _G@@@@@@@;   8@e                  \n                  @@F    _us%@@@@F     ^@@                  \n                  @@i      m@@@R-      _@@                  \n                  V@&    ^@@@@@@@3-    U@P                  \n                   0@%- !%8@@@@E-     S@0                   \n                    j@@j- s@@j-    -i@@j                    \n                     -3G_8@3*;;*iVg@@3-                     \n                       ,gt-x%gg%G5r'                        \n                      ;T                                    \n                                                            \n                                                            \n                                                            ")
print("                                                                                                    \n                                                              :^                                    \n                                                            :Y?.                                    \n                                             .:^^~~^^::.  :Y#7                                      \n                                        :!YPB&@@@@@@@&Y..J@#^                                       \n                                     ^JB@@@@&BG5YYYYY^:J&@P.^J^                                     \n                                   !G@@@&P?^.       .J&@@J ~@@@G!                                   \n                                 ^G@@@B7.         :J&@@&!  .~5@@@G^                                 \n                                ?@@@#7          :J&@@@B:   .. ^P@@@?                                \n                               ?@@@G:         :J&@@@@B!!J5GP~   ?@@@?                               \n                              ^@@@B.        :Y&@@@@@@&@@@@J.     J@@@^                              \n                              5@@@~       :J#@#B@@@@@@@@5:        B@@5                              \n                              #@@#.       :^:.:P@@@@@@G~          Y@@#                              \n                              #@@#.          ~#@@@@@B!            J@@#                              \n                              5@@@^         J@@@@@@G!~!7!.        G@@5                              \n                              ^@@@G       ^B@@@@@@@@@@@5^        7@@@^                              \n                               ?@@@5    .J@@@@@@@@@@&Y:         !@@@?                               \n                                7@@@B~  ^?7!^J@@@@#J.         .Y@@@7                                \n                                 ^G@@@P~.   J@@@#?.         :J#@@G^                                 \n                                   !G@@@7 :G@@B!        .^?G@@@G!                                   \n                                     ^J! !&@G!:7?77??YPB&@@@BJ^                                     \n                                        5@G~ ?#@@@@@@@&#PY!:                                        \n                                      ^GP~   ::^^~~^^:.                                             \n                                     !Y^                                                            \n                                    ^^                                                              \n                                                                                                    ")

print("-----------------------------PRESS START TO BEGIN-----------------------------")

if(True):
    input()

if(jesse_quick > barry_allen): #elege um vencedor
    vencedor1 = "jesse quick"
    velocidade1 = jesse_quick
else:
    vencedor1 = "barry allen"
    velocidade1 = barry_allen

if(wally_west > dr_whells): #elege um vencedor
    vencedor2 = "wally west"
    velocidade2 = wally_west
else:
    vencedor2 = "dr whells"
    velocidade2 = dr_whells

if(jay_garrick > max_mercury):  #elege um vencedor
    vencedor3 = "jay garrick"
    velocidade3 = jay_garrick
else:
    vencedor3 = "max mercury"
    velocidade3 = max_mercury

if(velocidade1 > velocidade2 and velocidade1 > velocidade3):    #compara qual dos 3 foi o mais rapido
    print("O vencedor foi",vencedor1," com", velocidade1," flashs de velocidade, o que da",velocidade1*300000,"Km/s")

elif(velocidade2 > velocidade1 and velocidade2 > velocidade3):
    print("O vencedor foi",vencedor2," com", velocidade2," flashs de velocidade, o que da",velocidade2*300000,"Km/s")

else:
    print("O vencedor foi",vencedor3," com", velocidade3," flashs de velocidade, o que da",velocidade3*300000,"Km/s")

print("Velocidade dos corresdores\r\n")
print("Jesse quick",jesse_quick)
print("Barry Allen",barry_allen)
print("Wally West",wally_west)
print("Dr Whells",dr_whells)
print("Jay Garrick",jay_garrick)
print("Max Mercury",max_mercury)