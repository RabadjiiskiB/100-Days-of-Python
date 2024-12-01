
N = 100
primes = 0

for num in range(1,N):
    isPrime = True
    if num == 0 or num == 1: print(num, " is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                isPrime = False
                break
        if isPrime:
            print(num, " is a prime number")
            primes += 1
print(primes)