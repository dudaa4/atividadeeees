print("Quantas notas há no total?")
n = int(input())

soma = 0

for notinhas in range(n):
    nota = float(input("Qual é a próxima nota? "))
    soma = soma + nota

print ("A média do aluno é: ", soma/n)
