#lambda arg:
import os 
import math

os.system('cls')


soma = lambda a, b: a+b

#H^2 = X^2 + Y^2
hip = lambda x,y: math.sqrt((x**2)+(y**2))


print("Soma", soma(5,5))
print("Hipotenusa:",hip(8,6))

