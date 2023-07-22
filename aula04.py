qtddeanimais = int(input('Digite quantos animais vc quer colocar no celeiro '))

FazendaMaluca = []
for z in range(qtddeanimais):
    y= input('Digite o animal que vai entrar na fazenda: ')
    print('Legal! o novo animal sera um: ', y, "!")
    FazendaMaluca.append(y)



for x in FazendaMaluca:
    print(x)