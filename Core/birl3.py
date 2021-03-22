print('BruteForceAlg v3.0')


"""	Senha inserida pelo usuário e que o algoritmo vai tentar achar através da força bruta, combinando uma cadeia de caracteres	"""
senha = input('Insira sua senha: ')
if not senha:
	senha = input('\nErro!\n\nInsira a senha novamente.\nsenha: ')


"""	Caracteres para testagem de combinação	"""
p = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']


"""	Variáveis de contagem	"""
x = -1
y = -1
r = '0'

comprimento = len(senha) #vai ser usado depois
senha = 'a'*(5 - comprimento) + senha


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
					if r == senha:
						break
					a+=1
					b = 0
					for i in range (0,35):
						if r == senha:
							print(f'\n\n\nSenha quebrada com sucesso!\n\n\033[0;0m\033[1;31m{r[(5-comprimento):]}\033[0;0m')
							break
						r = p[x] + p[y] +p[z] + p[a] + p[b]
						print(' '*50 + '\033[1;32m' + r)
						b+=1

print('\033[0;0m')
