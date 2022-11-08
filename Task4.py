#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

#Пример:

#- k=2 => 2*x² + 4*x + 5 = 0 

#k = 6
#    ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h = 0
#
#   a, b, c, d, e, h - рандом
from random import randint

k = int(input('Введите степень k: '))
for i in range(k, 0, -1):
    a = randint(1, 101)
    if a == 1:
        a = ''
    else:
        if i != 1:
            a = f'{a}*x^{i} +'
        else:
            a = f'{a}*x +'
        print(a, end =' ')
print(f'{randint(1, 101)}=0')
