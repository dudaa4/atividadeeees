print ("Em qual escala está a temperatura?")
print ("Digite C para Celsius, F para Fahrenheit e K para Kelvin")
escolha = input()
print ("Qual é o valor da temperatura na escala escolhida?")
temperatura = float(input())

print ("Para qual escala a temperatura será convertida?")
convertendo = input()

if (escolha == "c" and convertendo == "k"):
    print ("A temperatura em Kelvin é: ", temperatura+273,"K")

if (escolha == "c" and convertendo == "f"):
    print ("A temperatura em Fahrenheit é: ", 9*temperatura/5 + 32, "F")

if (escolha == "f" and convertendo == "c"):
    print ("A temperatura em Celsius é: ", (temperatura-32)*5/9, "C")

if (escolha == "f" and convertendo == "k"):
    print ("A temperatura em Kelvin é: ", (temperatura-32)*5/9+273, "K")

if (escolha == "k" and convertendo == "c"):
    print ("A temperatura em Celsius é: ", temperatura-273,"C")

if (escolha == "k" and convertendo == "f"):
    print ("A temperatura em Fahrenheit é: ", (temperatura-273)*9/5+32,"F")