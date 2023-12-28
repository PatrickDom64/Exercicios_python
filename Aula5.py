import random

num_i = 1
num_f = 0.5
num_c =1j

x = num_i

y = num_f
y_int = int(num_f)

z = num_c

num_r = [
    random.randrange(0,90),
    random.randrange(0,10),
    random.randrange(80,90),
    random.randrange(50,60)
]

r=num_r

print ("Valor 1: ", str(num_r[0]))
print ("Valor 2: ", str(num_r[1]))
print ("Valor 3: ", str(num_r[2]))
print ("Valor 4: ", str(num_r[3]))


#print ("Valor: ", str(num_r), "- Tipo: ", str(type(num_r)))

print ("Valor: ", str(x), "- Tipo: ", str(type(x)))

print ("Valor: ", str(y), "- Tipo: ", str(type(y)))

print ("Valor: ", str(y_int), "- Tipo: ", str(type(y_int)))

print ("Valor: ", str(z), "- Tipo: ", str(type(z)))