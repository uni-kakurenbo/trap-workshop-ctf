from random import randrange
from Crypto.Util.number import isPrime, bytes_to_long
from math import gcd

p, q = 0, 0


def far_far_away(a, b):
    for i in range(1000):
        a, b = b, a + b
    return a, b


while 1:
    a, b = randrange(0, 2**32), randrange(0, 2**32)
    p, q = far_far_away(a, b)
    if isPrime(p) and isPrime(q):
        break

print(a, b, p, q)

e = 0x10001
N = p * q
print(f"{e = }")
print(f"{N = }")

with open("flag.txt") as f:
    flag = bytes_to_long(f.read().encode())

cipher = pow(flag, e, N)
print(f"{cipher = }")
