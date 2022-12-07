# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях).
from pathlib import Path

def compar(x : int ,dict1: dict): #  Функция парса по последнему элементу
  temp = []
  if 'x^' in dict1[x]:
    temp = dict1[x].split('x^')
  elif 'x' in dict1[x]:
    temp = dict1[x].split('x')
  elif '=' in dict1[x]:
    temp = dict1[x].split('=')
  return (temp[-1])

def comparison(x : int ,dict1: dict): # Функция парса по превому элементу
  temp = []
  if 'x^' in dict1[x]:
    temp = dict1[x].split('x^')
  elif 'x' in dict1[x]:
    temp = dict1[x].split('x')
  elif '=' in dict1[x]:
    temp = dict1[x].split('=')
  return int(temp[0])

def fill(x, list):                 # Функция заполнения текста в многочлен
  cout = 0
  temp = ''
  result = ''
  for i in range(x):
    num = list[i]
    temp = str(list[i]) +'x^'+str(x-i)
    result += temp +'+'
    cout +=1 
    if cout == x-1:
      temp = str(list[i+1]) +'x'
      result += temp +'+'
      num = list[i+2]
      temp = str(num)
      result += temp +'=0'
      break
  return result

firstFile = Path('text', 'test04.txt')
firstList = []
firstDict={}
secondFile = Path('text', 'test05.txt')
secondList = []
secondDict={}
saveFile = Path('text', 'test05_cons.txt')
lst =[]                  # список для хранения суммы чисел двух многочленов
with open(firstFile, 'r') as firstPolynomial:
  firstList = firstPolynomial.read().split('+')
  for i in range(len(firstList)):
    firstDict[i] = firstList[i]
    
with open(secondFile, 'r') as secondPolynomial:
  secondList = secondPolynomial.read().split('+')
  for i in range(len(secondList)):
    secondDict[i] = secondList[i]

if len(firstDict)<len(secondDict):    # если длина словаря первого меньше втрого
  n = len(firstDict)-1
  strdict = secondDict[0]             # 1 значение словаря присваеваеться
else:
  n = len(secondDict)-1
  strdict = firstDict[0]

for i in range(len(firstDict)):
  for j in range(len(secondDict)):
    if compar(i,firstDict) == compar(j,secondDict):
      lst.append(comparison(i,firstDict)+comparison(j,secondDict))

with open(saveFile, 'w') as save:
  save.write(strdict+'+'+(fill(n, lst)))
      
print(strdict +'+'+ (fill(n,lst)))
print(firstDict)
print(secondDict)