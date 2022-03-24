'''4 – Faça um programa que:
• Leia o nome, a idade e o sexo de N pessoas
• Escreva o nome da mulher mais velha
• Escreva a idade do homem mais novo'''

from signal import valid_signals


nome_mulher_mais_velha = ""
nome_homem_mais_novo = ""
idade_homem_mais_novo = 10000000000000000000000000000000000000000000000000*10000000000000000000000000000000000000000000000000
idade_mulher_mais_velha = 0
sexo = 1

while True: 
    try:
        while sexo != 0 :
            sexo = int(input("Digite 1 para homem - 2 para mulher - qualquer numero para sair: "))
            if(sexo == 1 or sexo == 2):
                nome = input("Digite o nome: ")
                idade = int(input("Digite a idade: "))

                if(sexo == 2 and idade > idade_mulher_mais_velha):
                    nome_mulher_mais_velha = nome #nome da mulher mais velha
                    idade_mulher_mais_velha = idade #se idade digitada maior que a idade_mulher_mais_velha, faca idade_mulher_mais_velha = idade digitada
            
                elif(sexo == 1 and idade < idade_homem_mais_novo):
                    nome_homem_mais_novo = nome
                    idade_homem_mais_novo = idade
            else:
                break #saida do programa retorna os resultados
        break
    except ValueError:
        print("Digite apenas numeros")
    except KeyboardInterrupt:
        print("\nGoodbye friend") #mensagem para interrupção com ctrl + c
        exit()

if(nome_homem_mais_novo != "" and nome_mulher_mais_velha != ""):
    print("O nome da mulher mais velha é, ",nome_mulher_mais_velha," com ", idade_mulher_mais_velha," anos")
    print("A idade do homem mais novo é, ",idade_homem_mais_novo," e seu nome é ", nome_homem_mais_novo)
else:
    print("Digite alguns nomes primeiro")