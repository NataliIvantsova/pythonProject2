# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
import random

number_monet = int(input('Введите количество монет '))
orel = 0 # Создаем счетчик числа орлов
reshka = 0 # Создаем счетчик числа решек
for i in range(number_monet):
    monet = random.randint(0, 1)# рандомно вводим монеты
    print(monet)
    if monet == 1:
        orel += 1 # Списком считаем число орлов
    else:
        reshka += 1 # Списком считаем число решек
print("количество монет, которые нужно перевернуть:")
print(orel if orel <= reshka else reshka) # сравниваем и выводим меньшее