# Найти наименьшее общее кратное двух чисел

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(x, y):
    return (x * y) // gcd(x, y)


m = int(input("Введите число a "))
n = int(input("Введите число b "))
print(lcm(m, n))
