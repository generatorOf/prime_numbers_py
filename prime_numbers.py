"""
(c) Evgeny Mironov
            _.            __.
    __ . /  ( ..      __/ /
<   o  )))       . . -  \(
    `   ´´ \| ´           
"""
# unten folgt ein objected basiertes Primzahlengenerator
# es dauert ca 1-2 min bis die Reihe der Primzahlen kleiner 1 mln erzeugt wird
# hat einer von euch lust daran weiter zu arbeiten um den Verlauf zu optimieren oder
# oder was objektiv ist funktional darzustellen
# oder generatoren, expression, comprehension etc einzubauen?

# willst du mitmachen? -
# einfach clonen, verändern und unter deinem Namen in den gleichen Ordner hochladen

from math import sqrt

def gebrauchte_zeit(f):
    def wrapper():
        import time
        t1 = time.time()
        f()
        t2 = time.time()
        print(t2 - t1)
    return wrapper


def isprime(this_num):
    last = int(sqrt(PrimeNumbers.primes[-1])) + 1  # Wurzel des letzten Prims
    last_i = len(PrimeNumbers.primes) // 2
    while PrimeNumbers.primes[last_i] < last:
        last_i += 1
        print(last_i, '***')
    # print(last, last_i, PrimeNumbers.primes[last_i])
    for n in PrimeNumbers.primes[:last_i]:
        if this_num % n == 0:
            return False
    return True


class PrimeNumbers:
    primes = [2, 3]

    def __init__(self, num):
        self.candidate = (i + 2 for i in range(3, num, 2))

    # @gebrauchte_zeit  # - klappt irgendwie nicht
    def fill(self):
        for n in self.candidate:
            if isprime(n):
                PrimeNumbers.primes.append(n)
        return self.primes


primnumbers = PrimeNumbers(100_000).fill()
prim2 = PrimeNumbers(100).fill()
print(len(primnumbers))
print(primnumbers)
print(prim2)

# 1 3 7 9
# 1 3 5 7 9
