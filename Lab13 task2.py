import my_module1
import random
N = int(input("Введіть кількість чисел: "))
numbers = []
for i in range(N):
    value = random.randint(1, 100)
    number = my_module1.Nat(value)
    number.CalcDivs()
    numbers.append(number)
for number in numbers:
    number.DisplayValue()
    number.DisplayDivs()