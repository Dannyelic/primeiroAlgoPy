'''

                            IFPE
                    Lógica de programação
                    Função: Calcular o IMC
        Professor: Antônio Correia de Sá Barreto Neto

'''
nome = (input("Qual o seu nome? "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso: "))
 
imc = peso / altura**2
 
print((nome),", seu IMC é: %.4f" % imc)
 
if imc < 16:
	print("Você está abaixo do peso!")
elif imc < 17:
	print("Você está abaixo do peso!")
elif imc < 18.5:
	print("Você está abaixo do peso!")
elif imc < 25:
	print("Você está no peso ideal!")
elif imc < 30:
	print("Você está no primeiro grau da obesidade!")
elif imc < 35:
	print("Você está no primeiro grau da obesidade!")
elif imc < 40:
	print("Você está no segundo grau da obesidade!")
else:
	print("Você está no terceiro grau da obesidade!")
 