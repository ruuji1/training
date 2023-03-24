import numpy as np

a = np.array([[1,2,3,4], [1,2,3,4], [5,6,7,7]]) #массив трехмерн (две запятые)
c = np.array(range(1,10))

d = a[0:3, 0:4:2]
#print(d, 'Вырезали через 2')
d =[...,(0,1,3)] #выбираем стобики
#print(d, 'вырезали столбики')

x = a[1:3, 2:4] #вырезали строчки и столбцы
#print(x)

#print(c)
#print(a)

b = np.linspace(1.,2., 10) #Возвращает равномерно распределенные числа
#за указанный интервал.
#берет границы интервала и делит на части
#равномерное распределение данных по интервалу значения

#print(b)

x = np.linspace(1., 10., 10) #вектор
#print(x)

#мы можем поменять одно из его значений

x[0] = 2
#print(x)

y = x[3:5] #берем вырезку элементов
#print(y)

z = y.copy()
#print(z)

y[0] = 3 #в исходном массиве поменяли значения 
#print(x)

#мы модем взять все строчки, а столбцы каждый второй:

#arange функция которая генерирует вектор

x = np.arange(1.0, 10.0, 1)
print(x)

e = np.sqrt(4) # извлекаем квадратный корень
print(e)

y = x[x <= 5]
print(y)
#получаем булевские вектора (True False)












