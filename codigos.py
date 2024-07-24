## Aqui estou importando uma bliblioteca
import csv
import random

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Aqui começa para abrir o arquivo txt
## Aqui estou abrindo um arquivo em txt e abrindo ele como objetivo
with open ('Objetivo.txt') as objetivo:
    ## Aqui a variavel esta recebendo o valor do objetivo que e meu arquivo txt e esta lendo ele
    historia = objetivo.read()

## Aqui estou abrindo um arquivo em txt e abrindo ele como objetivo
with open ('Personagem.txt') as personagem:
    ## Aqui a variavel esta recebendo o valor do objetivo que e meu arquivo txt e esta lendo ele
    perso = personagem.read()

## Aqui termina a parte da historia e objetivo do personagem
##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Aqui começa a parte inicial de introdução para o ususario
## Aqui e uma função para deixar mais bonito emq ue vai imprimir varias linhas
def mostraLinha():
  ## Aqui so e um print
  print("---------------------------------------")

## Estou printando a historia do personagem
print("Aqui começa a historia do nosso personagem Niko", perso),
## Estou printando o Objetivo do personagem
print("O objetivo de Niko é: ", historia)
mostraLinha()

## Aqui estou printando algumas formas do usuario jogar
print("Você pode escolher entre três começos")
## Aqui vai ser o print da primeira opção dele
print("Opção 1: Começar no  começo da Historia")
## Aqui vai ser o print da segunda opção dele
print("Opção 2: Começar em uma aventura aleatoria")
## Aqui vai ser o print da terceira opção dele
print("Opção 3: Você escolhe a aventura que quer começar")

## Aqui e uma variavel que vai guardar a resposta do ususario
comeco = input("Qual opção você escolhe 1, 2 ou 3: ")
## Aqui ele so vai entra caso ele não escolha uma das opções fornecidas a ele
while comeco != "1" and comeco != "2" and comeco != "3":
    ## Aqui vai aparecer para ele respoinder de novo
    comeco = input("So pode escolher 1, 2 ou 3: ")

## Aqui termina a parte inicial
##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Aqui começa a Primeira Função

#Aqui eu chamei a primeira funçaõ passando 6 parametros para ela
def jogoInicial(copia3, j, p1, p2, alezin, comeco):
        ## Usei um For para entrar varias vezes na planilha
        for i in copia3:
            ## Aqui so vai entra caso a variavel comeco for igual a 1
            if comeco == "1":    
                ## Usei um marcador para ver se ele perde ou ganha
                marcador = 0
                ## Aqui ele so vai entrar quando i igual a planilha do indice j
                if i == copia3[j]:
                    ## função para deixar o jogo mais bonito
                    mostraLinha()
                    ## Aqui vai printar a aventura 
                    print(f"Aventura: {i['aventura']}")
                    ## Aqui vai printar informações adicionais
                    print("Você tem duas opções:")
                    ## Aqui vai printar as opções A
                    print(f"Opção A: {i['OpcaoA']}")
                    ## Aqui vai printar as opções B
                    print(f"Opção B: {i['OpcaoB']}")
                    ## função para deixar o jogo mais bonito
                    mostraLinha()

                    ## Aqui vai receber a resposta do ususario 
                    escolha = input("Escolha entre A e B: ")
                    ## Aqui ele so vai entrar se a escolha for diferente de A e b
                    while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                        ## Aqui vai receber a resposta do ususario
                        escolha = input("Escolha entre as opções A e B: ")
                    ## Aqui eu adicionei um auxiliar    
                    aux = 0    
                    ## Aqui eu adicionei um auxiliar
                    aux2 = 0
                    ## Aqui ele so vai entrar se a variavel foi igual a B ou b
                    if escolha == "B" or escolha == "b":     
                        ## Aqui eu usei um for para entrar varias vezes na probabilidade para ele passar um por um
                        for m in p2:
                                ## Aqui ele so vai entrar se o j foi igual o auxiliar
                                if j == aux:
                                        ## Aqui vai printar informações adicionais
                                        print("Você escolheu a Opção:", escolha, "então: ")
                                        ##Aqui ele so vai entra caso o m que é a probabilidade for maior que o alezin que é um numero aleatorio
                                        if m > alezin:
                                            ## função para deixar o jogo mais bonito
                                            mostraLinha()
                                            ## Aqui vai printar o sucesso de B
                                            print(f"Sucesso: {i['Sucesso B']}")
                                        else:
                                            ## Aqui vai printar o fracasso de B
                                            print(f"Fracasso: {i['Fracasso B']}")
                                            ## Aqui vai ser o marcador para avisar que deu fracasso    
                                            marcador = 1
                                ## Aqui vai ser para o auxiliar ir de 1 em 1            
                                aux = aux + 1  

                    ## Aqui ele vai entrar se ele não entrar no if
                    else:
                        ## Aqui eu usei um for para entrar varias vezes na probabilidade para ele passar um por um
                        for o in p1:
                                ## Aqui ele so vai entrar se o j foi igual o auxiliar
                                if j == aux2:
                                        ## Aqui vai printar informações adicionais
                                        print("Você escolheu a Opção: ", escolha, "então:")
                                        ##Aqui ele so vai entra caso O que é a probabilidade for maior que o alezin que é um numero aleatorio
                                        if o > alezin:
                                            ## função para deixar o jogo mais bonito
                                            mostraLinha()
                                            ## Aqui vai printar o sucesso de A
                                            print(f"Sucesso: {i['Sucesso A']}")
                                        else:
                                            ## Aqui vai printar o fracasso de A
                                            print(f"Fracasso: {i['Fracasso A']}")   
                                            ## Aqui vai ser o marcador para avisar que deu fracasso  
                                            marcador = 1 
                                ## Aqui vai ser para o auxiliar ir de 1 em 1     
                                aux2 = aux2 + 1
                    ##Aqui ele vai entrar se o marcador for igual a 0            
                    if marcador == 0:
                        ## função para deixar o jogo mais bonito
                        mostraLinha()        
                        ## Aqui vai ser a variavel que vai guardar a resposta do usuario
                        cont = input("Coloque C para continuar sua aventura ou coloque V para voltar sua aventura: ")
                        ## Aqui so vai entrar se cont que é uma variavel for diferente de C ou de V
                        while cont != "C" and cont != "c" and cont != "V" and cont != "v" :
                            ## Aqui vai ser a variavel que vai guardar a resposta do usuario
                            cont = input("Coloque C para continuar ou coloque V para voltar sua aventura: ")
                        ##Aqui ele so vai entrar se o cont for igual a C ou c    
                        if cont == "C" or cont == "c":
                            ## Aqui quer dizer que j vai de 1 em 1
                            j = j + 1
                            ## Aqui ele vai gerar outro numero aleatorio
                            alezin = random.randint(1, 100) 

                            ## Aqui ele so vai entrar quando J for igual a 20
                            if j == 20:
                                ## função para deixar o jogo mais bonito
                                mostraLinha()     
                                ## Aqui vai printar informações adicionais
                                print(" Chegamos ao final da nossa aventura!")           
                                ## Aqui vai printar informações adicionais       
                                print(" Nico, após uma longa jornada repleta de desafios e sacrifícios, finalmente alcançou a paz interior.")
                                ## Aqui vai printar informações adicionais
                                print(" Ao compreender que a verdadeira vitória reside na superação pessoal e na aceitação do passado, ele encontra a felicidade que tanto buscava.")
                                ## Aqui vai printar informações adicionais
                                print(" Orgulhoso de sua coragem e determinação, ele sorri para o horizonte, sabendo que sua jornada não foi em vão.")
                                ## Aqui vai printar informações adicionais
                                print(" Seja pela justiça feita ou pela redenção encontrada, Nico celebra a nova fase de sua vida, onde a esperança e a paz de espírito reinam em seu coração.")

                        if  cont == "V" or cont == "v":
                              ## função para deixar o jogo mais bonito
                                mostraLinha()
                                ## Aqui vai printar a aventura 
                                print(f"Aventura: {i['aventura']}")
                                ## Aqui vai printar informações adicionais
                                print("Você tem duas opções:")
                                ## Aqui vai printar as opções A
                                print(f"Opção A: {i['OpcaoA']}")
                                ## Aqui vai printar as opções B
                                print(f"Opção B: {i['OpcaoB']}")
                                ## função para deixar o jogo mais bonito
                                mostraLinha()

                                ## Aqui vai receber a resposta do ususario 
                                escolha = input("Escolha entre A e B: ")
                                ## Aqui ele so vai entrar se a escolha for diferente de A e b
                                while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                                    ## Aqui vai receber a resposta do ususario
                                    escolha = input("Escolha entre as opções A e B: ")
                                ## Aqui eu adicionei um auxiliar    
                                aux = 0    
                                ## Aqui eu adicionei um auxiliar
                                aux2 = 0
                                ## Aqui ele so vai entrar se a variavel foi igual a B ou b
                                if escolha == "B" or escolha == "b":     
                                    ## Aqui eu usei um for para entrar varias vezes na probabilidade para ele passar um por um
                                    for m in p2:
                                            ## Aqui ele so vai entrar se o j foi igual o auxiliar
                                            if j == aux:
                                                    ## Aqui vai printar informações adicionais
                                                    print("Você escolheu a Opção:", escolha, "então: ")
                                                    ##Aqui ele so vai entra caso o m que é a probabilidade for maior que o alezin que é um numero aleatorio
                                                    if m > alezin:
                                                        ## função para deixar o jogo mais bonito
                                                        mostraLinha()
                                                        ## Aqui vai printar o sucesso de B
                                                        print(f"Sucesso: {i['Sucesso B']}")
                                                    else:
                                                        ## Aqui vai printar o fracasso de B
                                                        print(f"Fracasso: {i['Fracasso B']}")
                                                        ## Aqui vai ser o marcador para avisar que deu fracasso    
                                                        marcador = 1
                                            ## Aqui vai ser para o auxiliar ir de 1 em 1            
                                            aux = aux + 1  

                                ## Aqui ele vai entrar se ele não entrar no if
                                else:
                                    ## Aqui eu usei um for para entrar varias vezes na probabilidade para ele passar um por um
                                    for o in p1:
                                            ## Aqui ele so vai entrar se o j foi igual o auxiliar
                                            if j == aux2:
                                                    ## Aqui vai printar informações adicionais
                                                    print("Você escolheu a Opção: ", escolha, "então:")
                                                    ##Aqui ele so vai entra caso O que é a probabilidade for maior que o alezin que é um numero aleatorio
                                                    if o > alezin:
                                                        ## função para deixar o jogo mais bonito
                                                        mostraLinha()
                                                        ## Aqui vai printar o sucesso de A
                                                        print(f"Sucesso: {i['Sucesso A']}")
                                                    else:
                                                        ## Aqui vai printar o fracasso de A
                                                        print(f"Fracasso: {i['Fracasso A']}")   
                                                        ## Aqui vai ser o marcador para avisar que deu fracasso  
                                                        marcador = 1 
                                            ## Aqui vai ser para o auxiliar ir de 1 em 1     
                                            aux2 = aux2 + 1

                                ## Aqui J vai de 1 em 1            
                                j = j + 1  
                    ## Aqui ele so vai entrar se ele não entar no if            
                    else:
                        ## função para deixar o jogo mais bonito
                        mostraLinha()   
                        ## Aqui vai printar informações adicionais
                        print(" Nico, após enfrentar inúmeros desafios e batalhas épicas, viu-se diante de um terrível desfecho. O peso da derrota e da impossibilidade de vingar o nome de Elena Hanger abateu-se sobre ele, deixando-o imerso em uma tristeza profunda.")
                        ## Aqui vai printar informações adicionais
                        print(" Assim, o guerreiro destemido aprendeu na dor a mais dura lição: nem toda jornada termina com a vitória almejada.")
                        ## Aqui vai printar informações adicionais
                        print(" A historia do seu personagem chega ao fim você consegui sobreviver até a missão: ", j)
                        ## Aqui o programa vai parar
                        break 

## Aqui termina a primeira função                    
##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Aqui começa a Segunda Função

#Aqui eu chamei a segunda funçaõ passando 6 parametros para ela
def jogoAleatorio(copia4, m, ale1, ale2, aleatorio, com):
        ## Usei um For para entrar varias vezes na planilha
        for i in copia4:
            ## Aqui so vai entra caso a variavel comeco for igual a 1
            if com == "2":
                ## Usei um marcador para ver se ele perde ou ganha
                marcador = 0
                ## Aqui ele so vai entrar quando i igual a planilha do indice m
                if i == copia4[m]:
                    ## função para deixar o jogo mais bonito
                    mostraLinha()
                    print(f"Aventura: {i['aventura']}")
                    print("Você tem duas opções")
                    print(f"Opção A: {i['OpcaoA']}")
                    print(f"Opção B: {i['OpcaoB']}")
                    ## função para deixar o jogo mais bonito
                    mostraLinha()
                    ## Aqui vai receber a resposta do ususario 
                    escolha = input("Escolha entre A e B: ")
                    ## Aqui ele so vai entrar se a escolha for diferente de A e b
                    while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                        ## Aqui vai receber a resposta do ususario
                        escolha = input("Escolha entre as opções A e B: ")
                    ## Aqui eu adicionei um auxiliar    
                    aux = m    
                    ## Aqui eu adicionei um auxiliar
                    aux2 = m

                    ## Aqui ele so vai entrar se a variavel foi igual a B ou b
                    if escolha == "B" or escolha == "b":
                            ## Aqui eu usei um for para entrar varias vezes na probabilidade para ele passar um por um
                            for p in ale2:
                                ## Aqui ele so vai entrar se o m foi igual o auxiliar
                                if m == aux:
                                    ## Aqui vai printar informações adicionais
                                    print("Você escolheu a Opção", escolha, "então: ")
                                    ##Aqui ele so vai entra caso P que é a probabilidade for maior que o aleatorio que é um numero aleatorio
                                    if p > aleatorio:
                                        ## função para deixar o jogo mais bonito
                                        mostraLinha()
                                        ## Aqui vai printar o sucesso de B
                                        print(f"Sucesso: {i['Sucesso B']}")
                                    else:
                                        ## Aqui vai printar o fracasso de B
                                        print(f"Fracasso: {i['Fracasso B']}")
                                        ## Aqui vai ser o marcador para avisar que deu fracasso       
                                        marcador = 1
                                ## Aqui vai ser para o auxiliar ir de 1 em 1           
                                aux = aux + 1

                     ## Aqui ele vai entrar se ele não entrar no if
                    else:
                        ## Aqui eu usei um for para entrar varias vezes na probabilidade para ele passar um por um
                        for b in ale1:
                            ## Aqui ele so vai entrar se o m foi igual o auxiliar
                            if m == aux2:
                                ## Aqui vai printar informações adicionais
                                print("Você escolheu a Opção", escolha, "então:")
                                ##Aqui ele so vai entra caso B que é a probabilidade for maior que o aleatorio que é um numero aleatorio
                                if b > aleatorio:
                                    ## função para deixar o jogo mais bonito
                                    mostraLinha()
                                    ## Aqui vai printar o sucesso de A
                                    print(f"Sucesso: {i['Sucesso A']}")
                                else:
                                    ## Aqui vai printar o fracasso de A
                                    print(f"Fracasso: {i['Fracasso A']}")
                                    ## Aqui vai ser o marcador para avisar que deu fracasso   
                                    marcador = 1
                            ## Aqui vai ser para o auxiliar ir de 1 em 1         
                            aux2 = aux2 + 1

                    ##Aqui ele vai entrar se o marcador for igual a 0   
                    if marcador == 0:
                        ## função para deixar o jogo mais bonito
                        mostraLinha()

                        ## Aqui vai ser a variavel que vai guardar a resposta do usuario
                        cont = input("Coloque C para continuar sua aventura ou coloque V para voltar sua aventura: ")
                        ## Aqui so vai entrar se cont que é uma variavel for diferente de C ou de V
                        while cont != "C" and cont != "c" and cont != "V" and cont != "v" :
                            ## Aqui vai ser a variavel que vai guardar a resposta do usuario
                            cont = input("Coloque C para continuar ou coloque V para voltar sua aventura: ")
                        ##Aqui ele so vai entrar se o cont for igual a C ou c    
                        if cont == "C" or cont == "c":
                            ## Aqui quer dizer que m vai de 1 em 1
                            m = m + 1
                            ## Aqui ele vai gerar outro numero aleatorio
                            aleatorio = random.randint(1, 100) 

                             ## Aqui ele so vai entrar quando M for igual a 20
                            if m == 20:
                                ## função para deixar o jogo mais bonito
                                mostraLinha()     
                                ## Aqui vai printar informações adicionais
                                print(" Chegamos ao final da nossa aventura!")           
                                ## Aqui vai printar informações adicionais       
                                print(" Nico, após uma longa jornada repleta de desafios e sacrifícios, finalmente alcançou a paz interior.")
                                ## Aqui vai printar informações adicionais
                                print(" Ao compreender que a verdadeira vitória reside na superação pessoal e na aceitação do passado, ele encontra a felicidade que tanto buscava.")
                                ## Aqui vai printar informações adicionais
                                print(" Orgulhoso de sua coragem e determinação, ele sorri para o horizonte, sabendo que sua jornada não foi em vão.")
                                ## Aqui vai printar informações adicionais
                                print(" Seja pela justiça feita ou pela redenção encontrada, Nico celebra a nova fase de sua vida, onde a esperança e a paz de espírito reinam em seu coração.")

                        if  cont == "V" or cont == "v":
                             if i == copia4[m]:
                                ## função para deixar o jogo mais bonito
                                mostraLinha()
                                print(f"Aventura: {i['aventura']}")
                                print("Você tem duas opções")
                                print(f"Opção A: {i['OpcaoA']}")
                                print(f"Opção B: {i['OpcaoB']}")
                                ## função para deixar o jogo mais bonito
                                mostraLinha()

                                escolha = input("Escolha entre A e B: ")
                                while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                                    escolha = input("Escolha entre as opções A e B: ")

                                aux = m    
                                aux2 = m

                                if escolha == "B" or escolha == "b":
                                        for p in ale2:
                                            if m == aux:
                                                print("Você escolheu a Opção", escolha, "então: ")
                                                if p > aleatorio:
                                                    ## função para deixar o jogo mais bonito
                                                    mostraLinha()
                                                    print(f"Sucesso: {i['Sucesso B']}")
                                                else:
                                                    print(f"Fracasso: {i['Fracasso B']}")     
                                                    marcador = 1
                                            aux = aux + 1

                                else:
                                    for b in ale1:
                                        if m == aux2:
                                            print("Você escolheu a Opção", escolha, "então:")
                                            if b > aleatorio:
                                                ## função para deixar o jogo mais bonito
                                                mostraLinha()
                                                print(f"Sucesso: {i['Sucesso A']}")
                                            else:
                                                print(f"Fracasso: {i['Fracasso A']}")   
                                                marcador = 1
                                        aux2 = aux2 + 1
                             m = m + 1               
                    else:
                        ## função para deixar o jogo mais bonito
                        mostraLinha()   
                        print(" Nico, após enfrentar inúmeros desafios e batalhas épicas, viu-se diante de um terrível desfecho. O peso da derrota e da impossibilidade de vingar o nome de Elena Hanger abateu-se sobre ele, deixando-o imerso em uma tristeza profunda.")
                        print(" Assim, o guerreiro destemido aprendeu na dor a mais dura lição: nem toda jornada termina com a vitória almejada.")
                        print(" A historia do seu personagem chega ao fim você consegui sobreviver até a missão: ", m)
                        break               

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Função 3
def jogadorEscolhe(planilha, probabilidadeA, probabilidadeB, escolhaUsuario, ale, come):
     for i in planilha:
                if come == "3":
                    marcador = 0
                    if i == planilha[escolhaUsuario]:
                        ## função para deixar o jogo mais bonito
                        mostraLinha()
                        print(f"Aventura: {i['aventura']}")
                        print("Você tem duas opções:")
                        print(f"Opção A: {i['OpcaoA']}")
                        print(f"Opção B: {i['OpcaoB']}")
                        ## função para deixar o jogo mais bonito
                        mostraLinha()
                        escolha = input("Escolha entre A e B: ")
                        while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                            escolha = input("Escolha entre as opções A e B: ")
                        aux = 0    
                        aux2 = 0
                        if escolha == "B" or escolha == "b":     
                            for m in probabilidadeB:
                                    if escolhaUsuario == aux:
                                            print("Você escolheu a Opção: ", escolha, "então: ")
                                            if m > ale:
                                                ## função para deixar o jogo mais bonito
                                                mostraLinha()
                                                print(f"Sucesso: {i['Sucesso B']}")
                                            else:
                                                print(f"Fracasso: {i['Fracasso B']}")   
                                                marcador = 1
                                    aux = aux + 1  

                                
                        else:
                            for o in probabilidadeA:
                                    if escolhaUsuario == aux2:
                                            print("Você escolheu a Opção: ", escolha, "então:")
                                            if o > ale:
                                                ## função para deixar o jogo mais bonito
                                                mostraLinha()
                                                print(f"Sucesso: {i['Sucesso A']}")
                                            else:
                                                print(f"Fracasso: {i['Fracasso A']}") 
                                                marcador = 1
                                    aux2 = aux2 + 1

                        if marcador == 0:
                            ## função para deixar o jogo mais bonito
                            mostraLinha()  
                            cont = input("Coloque C para continuar sua aventura ou coloque V para voltar sua aventura: ")

                            while cont != "C" and cont != "c" and cont != "V" and cont != "v" :
                                cont = input("Coloque C para continuar ou coloque V para voltar sua aventura: ")
                            if cont == "C" or cont == "c":
                                escolhaUsuario= escolhaUsuario+ 1
                                ale = random.randint(1, 100) 

                                if escolhaUsuario == 20:
                                    ## função para deixar o jogo mais bonito
                                    mostraLinha()     
                                    print(" Chegamos ao final da nossa aventura!")                  
                                    print(" Nico, após uma longa jornada repleta de desafios e sacrifícios, finalmente alcançou a paz interior.")
                                    print(" Ao compreender que a verdadeira vitória reside na superação pessoal e na aceitação do passado, ele encontra a felicidade que tanto buscava.")
                                    print(" Orgulhoso de sua coragem e determinação, ele sorri para o horizonte, sabendo que sua jornada não foi em vão.")
                                    print(" Seja pela justiça feita ou pela redenção encontrada, Nico celebra a nova fase de sua vida, onde a esperança e a paz de espírito reinam em seu coração.")
                                
                            elif cont == "v" or cont == "V":
                                    ## função para deixar o jogo mais bonito
                                    mostraLinha()
                                    print(f"Aventura: {i['aventura']}")
                                    print("Você tem duas opções:")
                                    print(f"Opção A: {i['OpcaoA']}")
                                    print(f"Opção B: {i['OpcaoB']}")
                                    ## função para deixar o jogo mais bonito
                                    mostraLinha()
                                    escolha = input("Escolha entre A e B: ")
                                    while escolha != "a" and escolha != "b" and escolha != "A" and escolha != "B":
                                        escolha = input("Escolha entre as opções A e B: ")
                                    aux = 0    
                                    aux2 = 0
                                    if escolha == "B" or escolha == "b":     
                                        for m in probabilidadeB:
                                                if escolhaUsuario == aux:
                                                        print("Você escolheu a Opção: ", escolha, "então: ")
                                                        if m > ale:
                                                            ## função para deixar o jogo mais bonito
                                                            mostraLinha()
                                                            print(f"Sucesso: {i['Sucesso B']}")
                                                        else:
                                                            print(f"Fracasso: {i['Fracasso B']}")   
                                                            marcador = 1
                                                aux = aux + 1  
    
                                    else:
                                        for o in probabilidadeA:
                                            if escolhaUsuario== aux2:
                                                        print("Você escolheu a Opção: ", escolha, "então:")
                                                        if o > ale:
                                                            ## função para deixar o jogo mais bonito
                                                            mostraLinha()
                                                            print(f"Sucesso: {i['Sucesso A']}")
                                                        else:
                                                            print(f"Fracasso: {i['Fracasso A']}") 
                                                            marcador = 1
                                            aux2 = aux2 + 1

                                    escolhaUsuario = escolhaUsuario + 1   
                        else:
                            ## função para deixar o jogo mais bonito
                            mostraLinha() 
                            print(" Nico, após enfrentar inúmeros desafios e batalhas épicas, viu-se diante de um terrível desfecho. O peso da derrota e da impossibilidade de vingar o nome de Elena Hanger abateu-se sobre ele, deixando-o imerso em uma tristeza profunda.")
                            print(" Assim, o guerreiro destemido aprendeu na dor a mais dura lição: nem toda jornada termina com a vitória almejada.")
                            print(" A historia do seu personagem chega ao fim você consegui sobreviver até a missão: ", escolhaUsuario)
                            break


##---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Aqui começa as variaveis!!

## Aqui vai ser a variavel que vai receber a planilha
plani = []
## Aqui vai ser a variavel que vai receber a probabilidade A
probA = []
## Aqui vai ser a variavel que vai receber a probabilidade A
probB = []

## Aqui estou abrindo a planilha em csv 
with open ('planilhajogo.csv', 'r') as planilha:
    ## Aqui eu coloquei a planilha em uma varivel dizendo que ela esta recebendo a planilha 
    aventuras = csv.DictReader(planilha)

    ## Aqui e o for que faz com que as informações da variavel aventuras entre no vetor plani 
    for n in aventuras:
         ## Aqui estou adicionando um elemento no vetor
         plani.append(n)
         ## Aqui estou guardando os valores de probabilidade A
         probabilidade_a = int(n['Probabilidade de sucesso A'])
         ## Aqui estou guardando os valores de probabilidade B
         probabilidade_b = int(n['Probabilidade de sucesso B'])
         ## Aqui eu estou adicionando as probabilidades A no vetor
         probA.append(probabilidade_a)
         ## Aqui eu estou adicionando as probabilidades B no vetor
         probB.append(probabilidade_b)

##Variavel que vai ser usada na função 3 aonde o usuario vai escolher a aventura
tenta = 0
##Aqui vai conferir se a variavel comeco vai ser igual a 3
if comeco == "3":
    ##Aqui vai fazer com que o ususario digite para escolher a sua aventura
    tenta = int(input("Escolha uma aventura de 0 ate 19: "))
    ##Aqui so vai entrar se o tenta for menor que 20
    while tenta > 20 :
        ##Aqui vai fazer com que o ususario digite para escolher a sua aventura
        tenta = int(input("Coloque um numero entre 0 e 19: "))

## Aqui e a variavel que faz com que j tenha o valor 0
j = 0

## Aqui vai sewr o numero aleatorio para usar na probabilidade
aleatorio1 = random.randint(1, 100)
# Aqui vai ser o numero aleatorio que vamos usar na função 2
aleatorio = random.randint(0, 19)
## Variavel que vai receber todas as probabilidades de A
q = probA
## Variavel que vai receber todas as probabilidades de B
z = probB

## Aqui estou chamando a primeira função e passando 6 parametros
jogoInicial(plani, j, q, z, aleatorio1, comeco)
## Aqui estou chamando a segunda função e passando 6 parametros
jogoAleatorio(plani, aleatorio, q, z, aleatorio1, comeco)
## Aqui estou chamando a terceira função e passando 6 parametros
jogadorEscolhe(plani, q, z, tenta, aleatorio1, comeco)

