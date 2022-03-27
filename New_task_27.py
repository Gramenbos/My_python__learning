# Составить список простых множителей натурального числа N


def factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


x = int(input("Введите число N: "))
print(*factor(x))
