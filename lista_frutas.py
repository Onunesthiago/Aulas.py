frutas = []
x = int(input('Informe a quantidade de frutas'))

for i in range(x):
    fruta = input ('fruta: ')
    frutas.append(fruta)

#decrescente 
for i in range (len(frutas)-1, -1, -1):
	print (frutas[i])

#crescente
for i in range (len(frutas)):
	print(frutas[i])