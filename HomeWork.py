
# Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input('enter a three-digit number:'))
b = a % 10
c = (a // 10) % 10
d = (a // 100) % 10
print(b+c+d)