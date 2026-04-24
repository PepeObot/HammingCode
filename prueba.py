sol = ""

def hamminization(n1):
	long = len(n1)
	p = 0
	
	while (2**p < len(n1)+p+1):
		p+=1

	trama1 = ['0'] * (long)
	trama = ['0'] * (long)

	j=0

	for i in range(1, long):
		if((i & (i-1)) != 0 ):
			trama[i-1] = n1[j]
			j+=1

	for i in range(1,long):
		if ((i&(i-1))!=0):
			trama1[i-1] = n1[j]
			j+=1

	for l in range(p):
		i = (2**l)
		sum = 0
		sum1 = 0
		for cont1 in range (long):
			posicion_real = cont1 + 1
			if(posicion_real & i) != 0:
				if posicion_real!=i:
					sum = sum ^ int(trama[cont1])
					sum1 = sum1 ^ int(trama1[cont1])	
		trama[i-1] = str(sum)
		trama1[i-1] = str(sum1)

	sum = 0
	sum1 = 0

	while l < len(trama):
		sum += int(trama[l]) 
		sum1 += int(trama1[l])
		l+=1

	if sum%2 == 0:
		trama[len(trama)-1] = "1"
	else:
		trama[len(trama)-1] = "0"

	if sum1%2 == 0:
		trama1[len(trama1)-1] = "1"
	else:
		trama1[len(trama1)-1] = "0"

	sol = "".join(trama)
	sol += "".join(trama1)

	return sol 
	

n1 = "1001100101001011" # 000010000101
n2 = "1001100101001011" # --0-100-0101

def hamming_ver8(n1,n2): #N1 a Cadena Hamming a verificar, N2 Cadena ya Hamminizada
	j = 0	
	x=""
	x1=""
	y = n1[0:7]
	y1= n1[8:15]
	for i in range(0,7): 
		if (2**j == i+1):
			j+=1
		else:
			x += y[i]
			x1 += y1[i]

	x+=x1

	j=0

	y = ""

	"""
	for i in range(0,7):
		if (2**j == i+1):
			j+=1
		else:
			x +=y1[i]
	"""
	
	l = hamminization(x)
	
	print(l)

	if(n1!=n2):
		if (l == n2):
			print("ERROR EN BIT DE PARIDAD")

x = hamming_ver8(n1,n2)