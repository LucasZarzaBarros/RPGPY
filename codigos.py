## Aqui estou importando uma bliblioteca
import csv
import random


## Aqui estou abrindo um arquivo em txt e abrindo ele como objetivo
with open ('Objetivo.txt') as objetivo:
    ## Aqui a variavel esta recebendo o valor do objetivo que e meu arquivo txt e esta lendo ele
    historia = objetivo.read()

## Aqui estou abrindo um arquivo em txt e abrindo ele como objetivo
with open ('Personagem.txt') as personagem:
    ## Aqui a variavel esta recebendo o valor do objetivo que e meu arquivo txt e esta lendo ele
    perso = personagem.read()

## Estou printando o Objetivo e a historia do personagem
print("Aqui começa a historia do nosso personagem Niko", perso)
print("O objetivo de Niko é: ", historia)
print("--------------------------------------------------------------------------------------------")

print("Você pode escolher entre dois começos")
print("Opção 1 : Começar no  começo da Historia")
print("Opção 2: Começar em uma aventura aleatoria")
comeco = input("Qual opção você escolhe 1 ou 2 ")
while comeco != "1" and comeco != "2":
    comeco = input("So pode escolher 1 ou 2")


## Aqui e a Terceira funcao que imprime apenas uma das aventuras
def caca(copia3, j, p1, p2,comeco):
        if comeco == "1":
        ## Usei um For para entrar varias vezes no vetor e depois remover uma das aventuras
            for i in copia3:
                if i == copia3[j]:
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Aventura: {i['aventura']}")
                    print("Você tem duas opções:")
                    print(f"Opção A: {i['OpcaoA']}")
                    print(f"Opção B: {i['OpcaoB']}")

                    escolha = input("Escolha entre A e B: ")
                    while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                        escolha = input("Escolha entre as opções A e B: ")
                    aux = 0    
                    aux2 = 0
                    if escolha == "B" or escolha == "b":     
                        for m in p2:
                                if j == aux:
                                        print(m)
                                        print("Você escolheu a Opção: ", escolha, "então: ")
                                        if m > 65:
                                            print(f"Sucesso: {i['Sucesso B']}")
                                        else:
                                            print(f"Fracasso: {i['Fracasso B']}")   
                                aux = aux + 1  

                    elif escolha == "a" or escolha == "A":
                        for o in p1:
                                if j == aux2:
                                        print(o)
                                        print("Você escolheu a Opção: ", escolha, "então:")
                                        if o > 65:
                                            print(f"Sucesso: {i['Sucesso A']}")

                                        else:
                                            print(f"Fracasso: {i['Fracasso A']}")        
                                aux2 = aux2 + 1

                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")        
                    cont = input("Coloque C para continuar sua aventura ou coloque V para voltar sua aventura")

                    while cont != "C" and cont != "c" and cont != "V" and cont != "v" :
                        cont = input("Coloque C para continuar ou coloque V para voltar sua aventura: ")
                    if cont == "C" or cont == "c":
                        j = j + 1
                        
    ##===================================================================================================================================================================================================================
                    if  cont == "V" or cont == "v":
                        print("----------------------------------------------------------------------------------------------------------------------------------------")
                        print(f"Aventura: {i['aventura']}")
                        print("Você tem duas opções:")
                        print(f"Opção A: {i['OpcaoA']}")
                        print(f"Opção B: {i['OpcaoB']}")

                        escolha = input("Escolha entre A e B: ")
                        while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                            escolha = input("Escolha entre as opções A e B: ")
                        aux = 0    
                        aux2 = 0
                        if escolha == "B" or escolha == "b":     
                            for m in p2:
                                    if j == aux:
                                            print("Você escolheu a Opção: ", escolha, "então: ")
                                            if m > 65:
                                                print(f"Sucesso: {i['Sucesso B']}")
                                            else:
                                                print(f"Fracasso: {i['Fracasso B']}")   
                                    aux = aux + 1  

                        elif escolha == "a" or escolha == "A":
                            for o in p1:
                                    if j == aux2:
                                            print(o)
                                            print("Você escolheu a Opção: ", escolha, "então:")
                                            if o > 65:
                                                print(f"Sucesso: {i['Sucesso A']}")

                                            else:
                                                print(f"Fracasso: {i['Fracasso A']}")        
                                    aux2 = aux2 + 1
                        j = j + 1

## ====================================================================================================================================================================================================


def imprimeAleatorio(copia4, m, ale1, ale2, com):
        for i in copia4:
            if com == "2":
                if i == copia4[m]:
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print(f"Aventura: {i['aventura']}")
                    print("Você tem duas opções")
                    print(f"Opção A: {i['OpcaoA']}")
                    print(f"Opção B: {i['OpcaoB']}")
                    print("----------------------------------------------------------------------------------------------------------------------------------------")

                    escolha = input("Escolha entre A e B: ")
                    while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                        escolha = input("Escolha entre as opções A e B: ")

                    if escolha == "B" or escolha == "b":
                        print("Você escolheu a Opção", escolha, "então: ")
                        if ale2 > 65:
                            print(f"Sucesso: {i['Sucesso B']}")
                        else:
                            print(f"Fracasso: {i['Fracasso B']}")     

                    else:
                        print("Você escolheu a Opção", escolha, "então:")
                        if ale1 > 65:
                            print(f"Sucesso: {i['Sucesso A']}")

                        else:
                            print(f"Fracasso: {i['Fracasso A']}")   

                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    cont = input("Coloque C para continuar sua aventura ou coloque V para voltar sua aventura") 
                    aux3 =m

                    while cont != "C" and cont != "c" and cont != "V" and cont != "v" :
                        cont = input("Coloque C para continuar ou coloque V para voltar sua aventura: ")
                    if cont == "C" or cont == "c":
                        m = aux3 + 1

                    if  cont == "V" or cont == "v":
                        print("----------------------------------------------------------------------------------------------------------------------------------------")
                        print(f"Aventura: {i['aventura']}")
                        print("Você tem duas opções")
                        print(f"Opção A: {i['OpcaoA']}")
                        print(f"Opção B: {i['OpcaoB']}")
                        print("----------------------------------------------------------------------------------------------------------------------------------------")

                        escolha = input("Escolha entre A e B: ")
                        while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                            escolha = input("Escolha entre as opções A e B: ")

                        if escolha == "B" or escolha == "b":
                            print("Você escolheu a Opção", escolha, "então: ")
                            if ale2 > 65:
                                print(f"Sucesso: {i['Sucesso B']}")
                            else:
                                print(f"Fracasso: {i['Fracasso B']}")     

                        else:
                            print("Você escolheu a Opção", escolha, "então:")
                            if ale1 > 65:
                                print(f"Sucesso: {i['Sucesso A']}")

                            else:
                                print(f"Fracasso: {i['Fracasso A']}")   
## Aqui vai ser a variavel que vai receber a planilha
plani = []

probA = []

probB = []

## Aqui estou abrindo a planilha em csv 
with open ('planilhajogo.csv', 'r') as planilha:
    ## Aqui eu coloquei a planilha em uma varivel dizendo que ela esta recebendo a planilha 
    aventuras = csv.DictReader(planilha)

    ## Aqui e o for que faz com que as informações da variavel aventuras entre no vetor plani 
    for n in aventuras:
         ## Aqui estou adicionando um elemento no vetor
         plani.append(n)
         probabilidade_a = int(n['Probabilidade de sucesso A'])
         probabilidade_b = int(n['Probabilidade de sucesso B'])

         probA.append(probabilidade_a)
         probB.append(probabilidade_b)


## Aqui e a variavel que faz com que j tenha o valor atribuido a plani indice [3]
j = 0



aleatorio = random.randint(0, 19)

m = aleatorio

q = probA[aleatorio +1]
z = probB[aleatorio +1]



imprimeAleatorio(plani, m, q, z, comeco)


op1 = probA
op2 = probB

caca(plani, j, op1, op2, comeco)