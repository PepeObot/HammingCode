sol = ""

def hamminization(n1):
	long = len(n1)
	p = 0

	while (2**p < len(n1)+p+1):
		p+=1

	print(p)

	trama = ['0'] * (long + p)

	j=0

	for i in range(1, long+p+1):
		if(i & (i-1)) != 0:
			trama[i-1] = n1[j]
			j+=1

	for l in range(p):
		i = (2**l)
		#cont1 = 0
		sum = 0
		for cont1 in range (long+p):
			posicion_real = cont1 + 1
			if(posicion_real & i) != 0:
				if posicion_real!=i:
					sum = sum ^ int(trama[cont1])	
		trama[i-1] = str(sum)
		sol = "".join(trama)
	return sol 

print("".join(sol))
