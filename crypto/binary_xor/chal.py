from random import choice
from math import sin
from Crypto.Util.number import long_to_bytes

# with open("secret.txt") as f:
#     secret = f.read()
secret = "dummuy"

flag = "flag{" + secret + "}"
flagbin = flag.encode()

while len(flagbin) % 8 != 0:
    flagbin += b"\x00"

pt = list(flagbin)


def ULTIMATE_SUPER_SAFE_FUNCTION(n):
    return (int(sin(n) * 10**10)) % 256


def BlockEncrypt(L, R):
    for i in range(10):
        L, R = R, L ^ ULTIMATE_SUPER_SAFE_FUNCTION(R)
    return L, R


mp = {}
for l in range(0, 200):
    for r in range(0, 200):
        mp[BlockEncrypt(l, r)] = (l, r)

ct = []
for i in range(0, len(pt), 2):
    L = pt[i]
    R = pt[i + 1]
    cL, cR = BlockEncrypt(L, R)
    ct.append(cL)
    ct.append(cR)
print(f"{ct = }")

ct = [
    49, 131, 18, 70, 205, 243, 87, 151, 240, 133, 90, 254, 123, 191, 92, 229, 161, 143, 197, 228, 89, 248, 93, 117, 0,
    79, 206, 166, 149, 144, 146, 63, 63, 132, 130, 161, 180, 14, 18, 199, 133, 22, 158, 156, 85, 71, 18, 199, 145, 24,
    39, 0, 216, 124, 125, 0
]

flagbin = b""

for i in range(0, len(ct), 2):
    a, b = mp[(ct[i], ct[i + 1])]
    flagbin += long_to_bytes(a) + long_to_bytes(b)

print(flagbin.decode())
