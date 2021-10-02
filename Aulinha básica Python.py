
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
	
      