#TASK 1

'''
Дана строка целых чисел `numbers`, разделенных запятой.
Превратите строку в словарь `result`, где ключ словаря - число в строке, значение - число в кубе.
По возможности сделайте несколько вариантов решений, используя:
- цикл for (опционально while)
- словарное выражение (dict comprehension)
'''

numbers = '1,100,15,17,3,221,9,5,7,2,8,11'
result = {}

number = numbers.split(",")

for i in number:
    result[int(i)] = int(i) ** 3

print(result)

# Тесты
assert all(number in result and result[number] == number * number * number for number in (1, 100, 15, 17, 3, 221, 9, 5, 7, 2, 8, 11))