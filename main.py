def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime(n):
    if not isinstance(n, int):
        raise ValueError("Аргумент должен быть целым числом")
    if n <= 0:
        raise ValueError("Номер простого числа должен быть положительным")

    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1


try:
    n = int(input("Введите номер простого числа: "))
    result = prime(n)
    print(f"Простое число #{n} = {result}")
except ValueError as e:
    print(e)
