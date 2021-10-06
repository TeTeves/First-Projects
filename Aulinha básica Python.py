#Formulário e IMC
nome = input("Qual é o seu nome?")
print("Olá,", nome, "prazer em te conhecer!")
peso = float(input("Qual é o seu peso?"))
dia = input("em que dia você nasceu?")
mes = input("em que mês você nasceu?")
ano = float(input("em que ano você nasceu?"))
idade = float((2021 - ano)) 
print(nome,"Você nasceu no dia", dia, "do mês de", mes, "no ano de", ano, "portanto você tem", idade, "de idade, certo?")
print(nome, "sua idade é", idade, "e seu peso é", peso)
a = input("sim ou não: ")
if a != "sim":  
      print("desculpe vamos tentar novamente")
else: print("Obrigado!, adorei conversar com você!")
print ("agora vamos calcular seu IMC - Indíce de Massa Corporal")
altura = float(input("digite sua altura:"))
imc = float(peso / (altura * altura))
print("O seu IMC é:", imc)
	
#Senhas:
print('Hello, User!')
nome = input("Digite sua senha (deve conter somente letras):")
if nome.isalpha():print()
else: print("A senha não contém somente letras")
if nome != "Daniel": print ("Acesso negado")
else: print("Bem-Vindo:")

#Joguinho de Adivinhação:
import random
number = random.randint(1, 20)
player_name = input("Olá, Qual é o seu nome?")
number_of_guesses = 0
print('okay! '+ player_name+ ' suponha um número de 1 a 20:')
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('seu número é muito baixo')
    if guess > number:
        print('seu número é muito alto')
    if guess == number:
        break
if guess == number:
    print('Você advinhou seu número em ' + str(number_of_guesses) + ' tentativas!')
else:
    print('Você não adivinhou o número, o número era ' + str(number))

#Calculadora Básica Python
print('Olá Bem-Vindo - Calculadora Python!')
#var
numero1 = int (input("Digite o primeiro numero: "))
numero2 = int (input("Digite o segundo numero: "))
#escopo
operaçao = int (input('selecione a operação que deseja realizar:[1] somar [2] subtrair [3] dividir: '))
print('-----------------------------------------------------------------')
if operaçao == 1: print('o resultado é:', numero1 + numero2)
if operaçao == 2: print('o resultado é:', numero1 - numero2)
if operaçao == 3: print('o resultado é:', numero1 / numero2)
else: print('error - selecione uma das opções acima.')
