# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.

number=int(input('Введите число N =>  '))

for j in range(number):
    number_2=2**j
    if number_2<=number:
        print(number_2)