# professor kkkkkkk 
# se nao fosse pela ajuda do meu amigo pedro eu nunca teria conseguido fazer essa atividade
# muito obrigada pedro por ter salvado minha alma do sofrimento eterno de programador

# inclusive, tentei fazer sozinha o tratamento de erro da atividade de média mas nao consegui :( 
# ainda tenho muita dificuldade e preciso ver muito tutorial pra absorver, 
# sao muitos termos que ainda nao  aprendi as funcionalidades, e sou meio lentinha pra gravar
# coisas que nao sao da minha area de conhecimento :/




def temp_escala1():
    print ("Em qual escala está a temperatura?")
    print ("Digite C para Celsius, F para Fahrenheit e K para Kelvin")
    i = input()
    if ((i != "c") and (i != "C") and (i != "k") and (i != "K") and (i != "f") and (i != "F")) == True:
        print("A escala de temperatura digitada é inválida, tente novamente")
        temp_escala1()
    else:
        global escolha
        escolha = i

def temp_escala2():
    print ("Para qual escala a temperatura será convertida?")
    i = input()
    if ((i != "c") and (i != "C") and (i != "k") and (i != "K") and (i != "f") and (i != "F")) == True :
        print("A escala de temperatura digitada é inválida, tente novamente")
        temp_escala2()
    else:
        global convertendo
        convertendo = i

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def temp_valor():
    print ("Qual é o valor da temperatura na escala escolhida?")
    i = input()
    if is_number(i) == False:
        print("O valor da temperatura digitada é inválida, tente novamente")
        temp_valor()
    else:
        global temperatura
        temperatura = float(i)

temp_escala1()

temp_valor()

temp_escala2()

if (escolha == "c" or escolha == "C") and (convertendo == "k" or convertendo == "K"):
    print ("A temperatura em Kelvin é: ", temperatura+273,"K")

if (escolha == "c" or escolha == "C") and (convertendo == "f" or convertendo == "F"):
    print ("A temperatura em Fahrenheit é: ", 9*temperatura/5 + 32, "F")

if (escolha == "f" or escolha == "F") and (convertendo == "c" or convertendo == "C"):
    print ("A temperatura em Celsius é: ", (temperatura-32)*5/9, "C")

if (escolha == "f" or escolha == "F") and (convertendo == "k" or convertendo == "K"):
    print ("A temperatura em Kelvin é: ", (temperatura-32)*5/9+273, "K")

if (escolha == "k" or escolha == "K") and (convertendo == "c" or convertendo == "C"):
    print ("A temperatura em Celsius é: ", temperatura-273,"C")

if (escolha == "k" or escolha == "K") and (convertendo == "f" or convertendo == "F"):
    print ("A temperatura em Fahrenheit é: ", (temperatura-273)*9/5+32,"F")






