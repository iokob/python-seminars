"""
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств
"""

list_1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
list_2 = [3, 6, 9, 12, 15, 18]
unsorted_set = set(list_1).intersection(set(list_2))

out = sorted(unsorted_set)
print(*out)

"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки
Входные данные:
На вход программе подается список arr, 
где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. 
Размер списка не превышает 1000 элементов.
Выходные данные:
Программа должна вывести одно целое число - максимальное количество ягод, 
которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.
"""

arr = [5, 8, 6, 4, 9, 2, 7, 3]
max_berries = 0
for i in range(len(arr)):
    berries = arr[i]+arr[i-1]+arr[i-2]
    if berries > max_berries:
        max_berries = berries
print(max_berries)