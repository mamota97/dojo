"""
Faça um programa que destaque a diferença entre duas string.
Exemplo: Entradas: O pássaro amarelo caiu. O pássaro vermelho caiu.
Saídas: O pássaro [amarel]o caiu. O pássaro [vermelh]o caiu.
"""
string1 = str(input("digite uma frase: ")).split()
string2 = str(input("digite uma quase igual: ")).split()
indice = 0
lista1 = []
lista2 = []
while indice < len(string1) and indice < len(string2):
    if string1[indice] == string2[indice]:
        lista1.append(string1[indice])
        lista2.append(string2[indice])
        indice += 1
    else:
        lista1.append("[" + string1[indice] + "]")
        lista2.append("[" + string2[indice] + "]")
        indice += 1
for palavra in lista1:
    print(palavra, end=" ")
print("|", end=" ")
for palavra in lista2:
    print(palavra, end=" ")
