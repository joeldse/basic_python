"""Aula 01 - Variáveis"""

a = 7
print(type(a))
b = 5.4
print(type(b))
c = 'Olá'
print(type(c))
d = True
print(type(d))

print('O número a é %d e b é %d' %(a,b))
print('O número a é %.2f e b é %.2f' %(a,b))
print(f'O número a é {a} e b é {b}')

num = int(input("Digite um número: "))

"""Aula 02 - Números"""

a = 5
b = 3
soma = a + b
print(soma)
sub = a - b
print(sub)
mult = a*b
print(mult)
div = a/b
print(div)
resto = a%b
print(resto)
pot = a**b
print(pot)

"""Aula 03 - Strings"""

s = "Curso de Python"
print(len(s))
print(s.capitalize())
print(s.count("o"))
print(s.isalnum())
print(s.lower())
print(s.upper())
print(s.title())
print(s.replace(" ",""))

print(s[1:4])
print(s[2:])
print(s[:4])

"""Aula 4 - Listas (Parte I)"""

L = [5, 8.4, [1,2,3], 'morango', "frutas"]
print(L[0])
print(L[3])
print(L[2])
print(L[2][1])

print(L[1:4])
print(L[2:])
print(L[:4])

a = [5.8 , 9]
b = [3, 6]
print(a + b)
print(a*3)

"""Aula 5 - Listas (Parte II)"""

L1 = list(range(5))
L2 = list(range(3, 7))
L3 = list(range(6, 30, 3))
print(f' L1: {L1} \n L2: {L2} \n L3: {L3}')
L = [12, 20, 5, 78, 61, 33]
print(len(L))
print(min(L))
print(max(L))
print(sum(L))
L.append(25)
print(L)
del L[1]
print(L)
L.sort()
print(L)

"""Aula 6 - Bibliotecas"""

import math
from numpy import random 
import pandas as pd

print(math.factorial(5))

v = random.rand(6)
print(v)

dados = pd.read_csv('/content/drive/My Drive/Colab/data.csv', sep=';')
print(dados)
print(dados.observed)
print(dados[:0])

"""Aula 7 - Gráficos"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10)
y = x + np.random.rand(10)*0.02
z = 1.1*x + np.random.rand(10)*0.02

p = np.polyfit(x, y, 1)
f = np.poly1d(p)

plt.plot(x, y, 'o', color='red', label='Australia')
plt.plot(x, z, 'o', color='black',label='New Zealand')
plt.plot(x, f(x), color = "r", label=f"y = {p[0]:.3f}x + {p[1]:.3f}")
plt.xlabel('tempo (h)')
plt.ylabel('posição (km)')
plt.title("Título do gráfico")
plt.legend()

"""Aula 7.5 - Case I (Item A)"""

import pandas as pd

data = pd.read_csv('/content/drive/My Drive/Colab/dataset/BikeCount.csv', sep=';')

max_temp = data.High_Temp.max()

min_temp = data.Low_Temp.min()

qde_dias = len(data.Date)
total_prec = sum(data.Precipitation)
media_prec = total_prec/qde_dias

soma = sum(data.Total)

print(f'máxima temperatura: {max_temp}')
print(f'mínima temperatura: {min_temp}')
print(f'média de precipitação: {media_prec:.2f}')
print(f'total de ciclistas: {soma}')

"""Aula 7.5 - Case I (Item B)"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('/content/drive/My Drive/Colab/dataset/BikeCount.csv', sep=';')

dia = data.Date
broklyn = data.Brooklyn_Bridge
manhattan = data.Manhattan_Bridge
williamsburg = data.Williamsburg_Bridge
queensboro = data.Queensboro_Bridge

plt.plot(dia, broklyn, color='r', label='Broklyn')
plt.plot(dia, manhattan, color='y', label='Manhattan')
plt.plot(dia, williamsburg, color='black', label='Williamsburg')
plt.plot(dia, queensboro, color='g', label='Queensboro')
plt.xlabel('dias')
plt.ylabel('Número de ciclistas')
plt.title("Número de ciclistas nas pontes do East River")
plt.legend(loc='upper center', bbox_to_anchor=(1.2, 0.8))

"""Aula 8 - Estruturas de decisão"""

idade = int(input('Qual é a sua idade: '))

if idade < 18:
  print('Você não pode dirigir')

nota = float(input('Digite a nota: '))
freq = float(input('Digite a frequência: '))
if (nota >= 5) and (freq >= 0.7):
  print('Aprovado!')
else:
  print('Reprovado por nota ou frequência')

if idade < 12:
  print('criança')
elif idade < 18:
  print('adolescente')
elif idade < 60:
  print('adulto')
else:
  print('idoso')

"""Aula 9 - Estruturas de repetição (Parte I)"""

senha = "12345"
leitura = " "
while (leitura != senha):
  leitura = input("Digite uma senha: ")
  if leitura == senha:
    print("Acesso Liberado!")
  else:
    print("Senha Incorreta. Tente novamente")

"""Aula 10 - Estruturas de repetição (Parte II)"""

soma = 0
for i in range(1,10,1):
  soma += i
print(soma)

nomes = ['Arthur', 'Barbara', 'Priscila']
for i in nomes:
  print(i)

"""Aula 11 - Funções"""

def op(x,y):
  soma = x + y
  sub = x - y
  return (soma, sub)

calc1 = op(10, 15)
calc2 = op(12,50)
print(calc1, calc2)

def maior(x,y):
  if x > y:
    print(f'{x} é maior que {y}')
  else:
    print(f'{y} é maior que {x}')

print(maior(25,50))

"""Aula 12 - Matrizes"""

a = [[1,2,3],[4,5,6]]
print(a)
print(a[0][0])

import numpy as np

b = np.array([[2,4],[3,6]])
c = np.array([[1,2],[2,3]])
print(np.transpose(b))
print(np.matmul(b,c))
print(np.zeros([2,3]))
print(np.ones([2,3]))
print(np.identity(3))