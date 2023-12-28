#==========continue ===========
x = 1 #int
cfb = "CFB Cursos" #string
y = 12.3 #float
z= True #booleano
n1 = 1; n2=2; w = complex(n1,n2) #complexo
list = ["carro", "avião", "bad", "friend", "boy"] #lista arrey
tupla = ["carro", 1, "bad", 1.2, "boy"] #Tupla
range = range(0,100,2)

dict = {
    "carro": "bmw",
    "Linguagem" : "python",
    "nome" : "Patrick"
}

set = {1,2,7,3,3,2,286,3}

print("Valor:",set)
print("Tipo:",type(set))

print("Valor:",dict["nome"])
print("Tipo:",type(dict))

print(range[2])
print("Tipo:" + str(type(range)))

print(list[2])
print("Tipo:",type(list))

print(tupla[2])
print("Tipo:",type(tupla))

print(w.imag)
print(w.real)
print("Tipo:",type(w))

print("Valor:",x)
print("Tipo:",type(x))

print("Valor:",cfb)
print("Tipo:",type(cfb))

print("Valor:",y)
print("Tipo:",type(y))

print("Valor:",z)
print("Tipo:",type(z))