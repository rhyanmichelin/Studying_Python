valor1 = int(input("Digite o primeiro valor da operação: "))
print("O primeiro valor inserido foi: ", valor1)

operador = input("Digite qual operaração você quer utilizar: \n+ | Para somar, \n- | Para subtrair, \n* | Para multiplicar, \n/ | Para dividir")
print("A operação escolhida foi:", operador)

valor2 = int(input("Digite o segundo valor da operação: "))
print("O sengudo valor inserido foi: ", valor2)

if operador == "+":
    resultado = valor1 + valor2
    print("O resultado da operação é: ", resultado)
    
elif operador == "-":
    resultado = valor1 - valor2
    print("O resultado da operação é: ", resultado)
    
elif operador == "*":
    resultado = valor1 * valor2
    print("O resultado da operação é: ", resultado)
    
elif operador == "/":
    resultado = valor1 / valor2
    print("O resultado da operação é: ", resultado)
