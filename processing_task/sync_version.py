import time
import logging
from math import sqrt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def find_factors(x):
    """
    Find and returns a factors list of number x.
    """
    factors = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            factors.append(i)
            if i != x // i:
                factors.append(x // i)
    return sorted(factors)


def factorize_sync(*numbers):
    """
    Synchronous calculation of factors for a list of numbers.
    """
    return [find_factors(num) for num in numbers]

if __name__ == '__main__':
    start = time.time()
    
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)

    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

    end = time.time()
    logging.info(f"Виконання синхронної версії : {end - start:.4f} секунд")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    logging.info("All is done!")
