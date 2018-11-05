import argparse

# ______________________________________________________________________
# Goldbach Calculator
# ======================================================================

def isPrime(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif (n%2==0) or (n%3==0): return False
    i = 5
    while (i*i <= n):
        if (n%i==0) or (n%(i+2)==0): return False
        i = i +6
    return True


def primeAdders(n):
    for i in range(n+1):
        a = n - i
        if isPrime(a) and isPrime(i):
            return [a, i]
    print('nothing found for n =', n)
    exit(1)


def goldbach(n):
    if (n <= 3):
        return
    elif (n%2 is 0):
        a,b = primeAdders(n)
        print('{0} = {1} + {2} + 1'.format(n, a, b))
    else:
        a,b = primeAdders(n-1)
        print('{0} = {1} + {2}'.format(n, a, b))

# ______________________________________________________________________
# Main
# ----------------------------------------------------------------------
        
parser = argparse.ArgumentParser(
    description='inputs an integer n and finds 2 primes whose sum equls n.'
)
parser.parse_args()

while True:
    line = input()
    if line is "": break
    n = int(line)
    goldbach(n)
