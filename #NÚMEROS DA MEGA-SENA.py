#NÚMEROS DA MEGA-SENA
#O primeiro passo do programa é perguntar ao usuário quantos jogos ele deseja criar, depois é criado jogos com seis números aleatórios.  

from random import randint
from time import sleep

lista = []

jogos = []


tot = 0

print('-'*30)
print('      JOGO DA MEGA-SENA     ')
print('-'*30)
quant = int(input('Digite a quantidade de jogos que deseja sortear: \n'))

while tot < quant:
  contador = 0
  while True:
    num = randint(1,61)
    if num not in lista:
      lista.append(num)
      contador+=1
    if contador > 5:
      break
    
  lista.sort()

  jogos.append(lista[:])

  lista.clear() 

  tot+=1

for num,jogo in enumerate(jogos):
  print(f'\nO {num+1}º sorteado foi \033[1;34m{jogo}\033[0;0m')
  sleep(0.5)

print('\n\033[1;32mBOA SORTE!')

