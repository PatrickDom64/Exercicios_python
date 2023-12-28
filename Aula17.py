import os 
os.system('cls')


x = input("Digite um numero:")
y = input("Digite um numero:")

def soma():
    res = int(x) + int(y)
    print(str(x),"+", str(y),"=",str(res))

def sub():
    res = int(x) - int(y)
    print(str(x),"-", str(y),"=",str(res))

def mult():
    res = int(x) * int(y)
    print(str(x),"*", str(y),"=",str(res))

def div():
    res = int(x) / int(y)
    print(str(x),"/", str(y),"=",str(res))

soma()
sub()
mult()
div()