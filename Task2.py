#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
#2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

n = int(input('Введите N => '))
list =[]
i = 2
while i <= n:
    if n % i == 0:
       list.append(i)
       n //= i
    else:
        i += 1

    

print(list)