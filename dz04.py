# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
from random import randint
from pathlib import Path

def fill(x, list):  # Функция заполнения принимет самую большу степени и списки индесов
  cout = 0
  temp = ''
  result = ''
  for i in range(x):
    num = list[i]
    if list[i] == 0:               # если значаение 0 то цикл пока n не равно 0
      while list[i] != 0:
        list[i] = randint(0,100)
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

saveFile = Path('text', 'test04.txt')
k = int(input('Введите самиый большую степень: '))
lst = []                         # Список для заполнение индексов

for i in range(k+1):              # цикл заполнения списка рандомными числами
  lst.append(randint(0,100))
print(lst)

with open(saveFile, 'w') as polynomial:
  polynomial.write(fill(k))  
  
print(fill(k, lst))