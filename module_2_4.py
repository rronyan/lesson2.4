numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for a in numbers:
    if a == 1:
        continue
    is_prime = True
    for b in range(2, a):
        if a % b == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(a)
    else:
        not_primes.append(a)
print(primes)
print(not_primes)
