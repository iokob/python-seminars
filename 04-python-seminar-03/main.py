'''
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
'''
#Решение через список
'''
numbers = [1, 1, 2, 0, -1, 3, 4, 4]
numbers_uniq = []

for i in numbers:
    if i not in numbers_uniq:
        numbers_uniq.append(i)
print(len(numbers_uniq))
'''
#Решение через множество
numbers = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(numbers)))

'''
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число
'''
numbers = [1, 1, 2, 0, -1, 3, 4, 4]
k = 2
k = k % len(numbers)
for i in range(k):
    temp = numbers.pop()
    numbers.insert(0, temp)
    print(numbers)

'''
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

dic = [{"V": "S001"}, {"V": "S002"}, 
       {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
       {" V ":" S009 "}, {" VIII":" S007 "}]
print(dic)
outset = set()
for i in dic:
    for k,v in i.items():
        outset.add(v)
print(outset)

