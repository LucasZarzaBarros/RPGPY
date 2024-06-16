## Aqui estou importando uma bliblioteca
import csv

## Aqui estou abrindo um arquivo em txt e abrindo ele como objetivo
with open ('Personagem e Objetivo.txt') as objetivo:
    ## Aqui a variavel esta recebendo o valor do objetivo que e meu arquivo txt e esta lendo ele
    historia = objetivo.read()

## Estou printando o Objetivo e a historia do personagem
print(historia)

## Aqui e a Primeira funcao que imprime todas as aventuras
def imprime(copia):
   ## Usei um For para entrar varias vezes no vetor e depois imprimir as aventuras
   for i in copia:
        ## Aqui e o print que faz a impressao das aventuras
        print(f"Aventura: {i['aventura']}")

## Aqui e a Segunda funcao que imprime apenas uma das aventuras
def imprimeUm(copia2, j):
    ## Usei um For para entrar varias vezes no vetor e depois imprimir uma aventura
    for i in copia2:
        ## usei um if para dizer que quando o i for igual o j (que sifnifica o indice) ele vai printar apenas essa aventura 
        if i == j:
             ## Aqui e o print de uma aventura
             print(f"Aventura: {i['aventura']}")

## Aqui e a Terceira funcao que imprime apenas uma das aventuras
def apagaUm(copia3, v):
    ## Usei um For para entrar varias vezes no vetor e depois remover uma das aventuras
    for i in copia3:
        ## Aqui eu estou dizendo que se meu i for diferente do v que significa o indice do vetor ele vai imprimir caso i for igual que v ele não vai entrar ele passara reto
        if i != v:
            ## Aqui e o print das aventuras
            print(f"Aventura: {i['aventura']}")



## Tentativa de uma funão que mostra apenas uma aventura e faça o usuario escolher entre Opção A e Opção B
def extra(copia4, n):
    for i in copia4:
        if i == n:
            print(f"Aventura: {i['aventura']}")
            print("Você tem Duas Opções")
            print(f"Opção A: {i['OpcaoA']}" )
            print(f"Opção B: {i['OpcaoB']}")

    escolha = input("Escolha entre A e B: ")
    while escolha != 'a' and escolha != 'A' and escolha != 'b' and escolha != 'B':
        escolha = input("Escolha entre A e B: ") 

    if escolha == "b" and escolha == "B":
        print("Você escolheu a opção b")

    else:
        print("Você escolheu a Opção a")


## Aqui vai ser a variavel que vai receber a planilha
plani = []

## Aqui estou abrindo a planilha em csv 
with open ('planilhajogo.csv', 'r') as planilha:
    ## Aqui eu coloquei a planilha em uma varivel dizendo que ela esta recebendo a planilha 
    aventuras = csv.DictReader(planilha)

    ## Aqui e o for que faz com que as informações da variavel aventuras entre no vetor plani 
    for n in aventuras:
         ## Aqui estou adicionando um elemento no vetor
         plani.append(n)
        
## Aqui e a variavel que faz com que n tenha o valor atribuido a plani indice [1]
n = plani[1]

## Aqui e a variavel que faz com que j tenha o valor atribuido a plani indice [3]
j = plani[3]

## Aqui estou chamando a função extra e passando dois parametros  
extra(plani, n)

## Aqui estou chamando a Primeira função e estou passando apenas um parametro
imprime(plani)

## Aqui estou chamando a Segunda função e estou passando dois parametros
imprimeUm(plani, n)

## Aqui estou chamando a Terceira função e estou passando dois parametros
apagaUm(plani, j)
