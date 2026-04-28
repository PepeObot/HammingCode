sol = ""

def hamminization_not8(n1):
	long = len(n1)
	p = 0
	while (2**p < len(n1)+p+1):
		p+=1

	trama = ['0'] * (long+p)
	j = 0
	for i in range(long+p):
		if (((i + 1) & i) != 0):
			trama[i] = n1[j]
			j += 1
	for l in range(p):
		i = (2**l)
		sum = 0
		for cont1 in range(long):
			preal = cont1 + 1
			if(preal & i) != 0:
				if preal != i:
					sum = sum ^ int(trama[cont1])
		trama[i-1] = str(sum)
	sum=0

	while l < len(trama):
		sum += int(trama[l])
		l+=1
	if sum%2 == 0:
		trama[len(trama)-1] = "1"
	else:
		trama[len(trama)-1] = "0"

	sol = "".join(trama)
	return sol

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
	

n1 = "00001001010101110110000100000010100011011011110110111001100011001100101011100000111010001101111001000000110010001100101001000001011000100110100101110100001000000110010101110011001000000110011001110101011011100110010001100001011011010110010101101110011101000011000010110110000100000011001010110111000100000011011000110000100100000011010010110111001100110011011110111001001101101110000111010000101110100011010010110001101100001001011100010000001010101011011100010000001100010011010010111010000100000011100100110010010111000001110010011001010111001101100101011011100111010001100001001000000111010101101110001000000110010101110011011101000110000101100100011011110010000001101100110000111011001101100111011010010110001101101111001011000010000001100011011001010111001001101111001000000110111100100000011101010110111001101111001011100010000001000001011011000010000001100001011001110111001001110101011100000110000101110010001000000110111101100011011010000110111100100000011000100110100101110100011100110010000001100110011011110111001"
# 000010000101
n2 = "00001001010101110110000100000010100011011011110110111001100011001100101011100000111010001101111001000000110010001100101001000001011000100110100101110100001000000110010101110011001000000110011001110101011011100110010001100001011011010110010101101110011101000011000010110110000100000011001010110111000100000011011000110000100100000011010010110111001100110011011110111001001101101110000111010000101110100011010010110001101100001001011100010000001010101011011100010000001100010011010010111010000100000011100100110010010111000001110010011001010111001101100101011011100111010001100001001000000111010101101110001000000110010101110011011101000110000101100100011011110010000001101100110000111011001101100111011010010110001101101111001011000010000001100011011001010111001001101111001000100110111100100000011101010110111001101111001011100010000001000001011011000010000001100001011001110111001001110101011100000110000101110010001000000110111101100011011010000110111100100000011000100110100101110100011100110010000001100110011011110111001" # --0-100-0101

def hamming_ver8(n1): #N1 a Cadena Hamming a verificar, N2 Cadena ya Hamminizada
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
	l = hamminization(x)
	
	print(l)

	if (l != n1):
		i = 1
		y = ""
		z = ""
		j = 0
		while i <= len(n1):
			if i-1 < len(l):
				y += n1[i-1]
				z += l[i-1]
			j += 1
			i = 2**j
		xy = ""
		for k in range(0,len(y)):
			xy += str(int(y[k]) ^ int(z[k]))
		xy_r = xy[::-1]
		#print(xy_r)
		if int(xy_r,2) == 0 or (int(xy_r) & (int(xy_r) - 1)) == 0:
			return l
		xy_r = int(xy_r,2)
		#print (xy_r)
		listapp = list(n1)
		if xy_r <= len(listapp):
			if listapp[xy_r-1] == '0':
				listapp[xy_r-1] = '1'
			else:
				listapp[xy_r-1] = '0'
		sol = "".join(listapp)
		return sol
	else:
		return n1
		


def unhamming_not8(n1):
	j = 0
	x = ""
	for i in range (len(n1)):
		if (2**j == i+1):
			j+=1
		else:
			x += n1[i]
	l = hamminization_not8(x)
	i=0
	if (l != n1):
		i = 1
		y = ""
		z = ""
		j = 0
		while i <= len(n1):
			if i-1 < len(l):
				y += n1[i-1]
				z += l[i-1]
			j += 1
			i = 2**j
		xy = ""
		for i in range(0,len(y)):
			xy += str(int(y[i]) ^ int(z[i]))
		xy_r = xy[::-1]
		#print(xy_r)
		if xy_r == 0 or (int(xy_r) & (int(xy_r) - 1)) == 0:
			return l
		xy_r = int(xy_r,2)
		#print (xy_r)
		listapp = list(n1)
		if xy_r <= len(listapp): # <--- ESTE IF EVITA QUE EXPLOTE LA INTERFAZ
			if listapp[xy_r-1] == '0':
				listapp[xy_r-1] = '1'
			else:
				listapp[xy_r-1] = '0'
		sol = "".join(listapp)
		return sol
	else:
		return n1

		
		
def sacarbits():
	with open("Archivos/BTrad1024.txt","r") as f:
		l2 = f.read()
		l1 = ""
		l=""
		i = 0
		c=0
		while i<len(l2):
			if l2[i] == " ":
				break
			i+=1
		l = l2.replace(" ","")
		s_final = ""
		while(c <= len(l)):
			bloque = l[c:c+i+1]
			#print(len(bloque))
			if(len(bloque)<i):
				break
			l1 += fromHtoHH(unhamming_not8(bloque))
			c+=i
		for k in range(0, len(l1), 8):
			btd = l1[k : k + 8]
			if len(btd) == 8:
				if btd != "00000000":
					s_final += chr(int(btd, 2))
	with open("Archivos/Trad.txt","w") as f:
		f.write(s_final)


def sacarbitsSinErrores():
	with open("Archivos/BTrad1024.txt","r") as f:
		l2 = f.read()
		l1 = ""
		l=""
		i = 0
		c=0
		while i<len(l2):
			if l2[i] == " ":
				break
			i+=1
		l = l2.replace(" ","")
		s_final = ""
		while(c <= len(l)):
			bloque = l[c:c+i+1]
			if(len(bloque)<i):
				break
			l1 += fromHtoHH(bloque)
			c+=i
		for k in range(0, len(l1), 8):
			btd = l1[k : k + 8]
			if len(btd) == 8:
				if btd != "00000000":
					s_final += chr(int(btd, 2))
	with open("Archivos/Trad.txt","w") as f:
		f.write(s_final)


def fromHtoHH(l):
	j=0
	l1 = []
	x=""
	for s in range(len(l)):
		if (2**j == s+1):
			j+=1
		else:
			x += l[s]
	return x

def fromHtoHH8(l):
	j = 0	
	x=""
	x1=""
	y = l[0:8]
	y1= l[8:16]
	print(y)
	for i in range(0,8): 
		if (2**j == i+1):
			j+=1
		else:
			x += y[i]
			x1 += y1[i]
	x+=x1
	print(x)
	return x

def sacarbits8():
	with open("Archivos/textoD.HE1","r") as f:
		l = ""
		s_final= ""
		l1 = ""
		l2 = f.read().replace(" ","")
		c = 0
		i = 16
		l = l2
		while c<=len(l):
			bloque = l[c:c+i]
			if(len(bloque)<i):
				break
			l1+=fromHtoHH8(hamming_ver8(bloque))
			c+=i
		for k in range(0, len(l1), 8):
			btd = l1[k : k + 8]
			if len(btd) == 8:
				if btd != "00000000":
					s_final += chr(int(btd, 2))
	with open("Archivos/Trad8.txt","w") as f:
		f.write(s_final)


#x = hamming_ver8(n1,n2)

#print(hamminization_not8("01010"))

#s_pre = "01011101" + ('0' * (1014-500))
#print(s_pre)

#unhamming_not8(n1)
#sacarbits()
sacarbits8()







