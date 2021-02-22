print('BruteForceAlg v3.0')


"""	Senha inserida pelo usuário e que o algoritmo vai tentar achar através da força bruta, combinando uma cadeia de caracteres	"""
senha = input('Insira sua senha: ')


"""	Caracteres para testagem de combinação	"""
p = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']


"""	Variáveis de contagem	"""
x = -1
y = -1
r = '0'


"""	Loop de testagem	"""
while r != senha:
	x= -1
	for i in range(0,35): #35 é o número de caracteres para a combinação (alfabeto + 0_9 - 1) 
		if r == senha:
			break
		x+=1
		y= -1
		for i in range (0,35):
			if r == senha:
				break
			y+=1
			z = -1
			for i in range (0,35):
				if r == senha:
					break
				z+=1
				a = -1
				for i in range (0,35):
					a+=1
					b = 0
					for i in range (0,35):
						if r == senha:
							break
						r = p[x] + p[y] +p[z] + p[a] + p[b]
						print('                            ' + '\033[1;32m' + r)
						b+=1
