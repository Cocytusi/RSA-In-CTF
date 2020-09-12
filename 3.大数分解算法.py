# n = 0x4333AF6B43F36028D8D9650EC3EED3238541EE5C15E626C58C9EC33674A6D08D5B1F2580A1A0B07E9D853536CD994E197889D122701A62BB2A9E79559F3D5281014535F6C54F83CA8D9700EEB67D99AF318D20A5150AD46D622A6A12DE0A758EE7DF75F5D10F2FE2585F2348537787063321FFDAC91BB3C3D1D88CBD04A824ED

from random import randint
from gmpy2 import *

# 1. Pollard rho方法
def PollardRho(n):
    x2 = 1
    c = 7
    while 1:
        x1 = randint(1, n)
        x2 = pow(x2, 2, n) + c % n

        fac = gcd(abs(x1 - x2), n)

        if fac > 1 and is_prime(fac):
            print(fac)
            break
    print('%d' % (n / fac))


# 2. Pollard rho p-1方法
def PollardRho_p_1(N):
    a = i = 2
    while 1:
        a = pow(a, i, N)
        d = gcd(a - 1, N)
        if d != 1:
            return d
        i += 1


# 3. Fermat方法
def Fermat(n):
    a = isqrt_rem(n)[0] + 1
    b = a ** 2 - n
    while 1:
        q = isqrt_rem(b)
        if q[1] == 0:
            return a - q[0]
        a += 1
        b = a ** 2 - n

if __name__ == '__main__':
    n = 0x4333AF6B43F36028D8D9650EC3EED3238541EE5C15E626C58C9EC33674A6D08D5B1F2580A1A0B07E9D853536CD994E197889D122701A62BB2A9E79559F3D5281014535F6C54F83CA8D9700EEB67D99AF318D20A5150AD46D622A6A12DE0A758EE7DF75F5D10F2FE2585F2348537787063321FFDAC91BB3C3D1D88CBD04A824ED
    PollardRho(n)
    p = PollardRho_p_1(n)
    print(p)
    # f = Fermat(n)
    # print(f)
