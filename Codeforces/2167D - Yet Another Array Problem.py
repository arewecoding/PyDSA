'''
def is_prime(n, primes):
    if n < 2:
        return False
    for p in primes:
        if n % p == 0:
            return False
    return True

def primes_till(n):
    primes = []
    for i in range(2, n):
        if is_prime(i, primes):
            primes.append(i)
    return primes

print(primes_till(50)) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
a = 1
for i in primes_till(50):
    a *= i
print(a)
'''

ar = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
n_test = int(input())
for i in range(n_test):
    found = False
    n = int(input())
    l_int = list(map(int, input().split()))
    for p in ar:
        for j in l_int:
            if j % p != 0:
                print(p)
                found = True
                break
        if found: break
    if not found: print(-1)