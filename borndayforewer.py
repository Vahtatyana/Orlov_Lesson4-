"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def ask_date(question, date):
    answer = input(question)
    while answer != date:
        print("Не верно")
        answer= input(question)

ask_date('Ввведите день рождения Пушкина?: ', '6')
ask_date('Ввведите год рождения Пушкина?: ', '1799')

print('Верно')