# Дано четное число N (>0) и символы C1 и C2.
# Вывести строку длины N, которая состоит из чередующихся символов C1 и С2 начиная с С1.
def alternating_characters(n, c1, c2):
    if n % 2 != 0:
        return "Число N должно быть четным"

    result = ""
    for i in range(n // 2):
        result += c1 + c2

    return result
import random
N = random.randint(0, 999)
C1 = 'A'
C2 = 'B'
print(alternating_characters(N, C1, C2))

