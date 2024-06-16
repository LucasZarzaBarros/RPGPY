import csv

with open ('Personagem e Objetivo.txt') as objetivo:
    historia = objetivo.read()

## Aqui e a Primeira funcao que imprime todas as aventuras
def imprime(copia):
   ## Usei um For para entrar varias vezes no vetor e depois imprimir as aventuras
   for i in copia:
        ## Aqui e o print que faz a impressao das aventuras
        print(f"Aventura: {i['aventura']}")

##
def imprimeUm(copia2, j):
    for i in copia2:
        if i == j:
             print(f"Aventura: {i['aventura']}")


def apagaUm(copia3, l):
    for i in copia3:
        if i != l:
            print(f"Aventura: {i['aventura']}")




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
    for i in copia4:
        if n == "a" and n == "A":
            print("Você escolheu a opção A")
            
        else:
            print("Você escolheu a Opção B")

plani = []


with open ('planilhajogo.csv', 'r') as planilha:
    aventuras = csv.DictReader(planilha)

    for n in aventuras:
         plani.append(n)
        

n = plani[1]
j = plani[3]
extra(plani, n)
imprime(plani)
imprimeUm(plani, n)
apagaUm(plani, j)
