def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


n = int(input("Введите номер числа Фибоначчи: "))
print("Число Фибоначчи под номером", n, "равно", fibonacci(n))