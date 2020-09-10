print('Cofre v.1')

senha = input('Insira sua senha: ')

p = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
x = -1
y = -1
r = '0'

while r != senha:
	x= -1
	for i in range(0,35):
		if r == senha:
			break
		x+=1
		y= 0
		for i in range (0,35):
			if r == senha:
				break
			y+=1
			z = 0
			for i in range (0,35):
				if r == senha:
					break
				z+=1
				a = 0
				for i in range (0,35):
					a+=1
					b = 0
					for i in range (0,35):
						if r == senha:
							break
						r = p[x] + p[y] +p[z] + p[a] + p[b]
						print('                            ' + '\033[1;32m' + r)
						b+=1