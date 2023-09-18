"""
Лабораторная 3 Вариант 9
Написать функцию, которая принимает целочисленный список, состоящий из n элементов, и с помощью генераторного выражения
создает новый массив элементов из тех элементов входящего массива, квадрат которого не превышает 30.
"""

def generate_squared_list(input_list):
    squared_list = [num for num in input_list if num**2 <= 30]
    return squared_list

input_list = [1,2,3,4,5,6,7]
result = generate_squared_list(input_list)
print(result)