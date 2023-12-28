cidade = "Belo Horizonte"
dia = 15
mes = "Dezembro"
ano = 2023

data = "{}, {} de {} de {} \n{}"

curso = "Curso de Python"

print("Cidade:", cidade, 
      " Dia:",str(dia), 
      " Mês:", mes, 
      " Ano:", str(ano))

print(data.format(cidade,dia,mes,ano,curso))
