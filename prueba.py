n1 = int(input("Ingrese un numerito a ser Hammingnizado: "))
n1b = format(n1,'08b')
#n1b = "0101001"
print(n1b)
long = len(n1b)
p = 0
while (2**p < len(n1b)):
	p+=1
p+=1

trama = [''] * (long + p)
i=2
j=0
m=0

for i in range(1, long+p+1):
	if(i & (i-1)) != 0:
		trama[i-1] = n1b[j]
		j+=1

print(trama)

for l in range(p):
	i = (2**l)
	cont = 0
	cont1 = 0
	sum = 0
	for cont1 in range (long+p):
		posicion_real = cont1 + 1
		if(posicion_real & i) != 0:
			if posicion_real!=i:
				sum = sum ^ int(trama[cont1])	
	trama[i-1] = str(sum)

print(trama)
i=0
j=0

#for i in range((long+p)):
	#if (trama[i]==''):
		#trama[i] = n1b[j]
		#j+=1
#j = 0
#for i in range(long)
print("".join(trama))


