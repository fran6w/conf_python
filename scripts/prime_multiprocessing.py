# coding: utf-8

import time
from math import sqrt
from multiprocessing import Pool


def f(n):
    is_prime = n > 1 and all(n % d for d in range(2, int(sqrt(n)) + 1))
    print(n, is_prime)


def run():
    numbers = [
    999_999_999_863,
    999_999_999_877,
    999_999_999_959,
    999_999_999_961,
    999_999_999_989,
    1_000_000_000_039,
    1_000_000_000_061,
    1_000_000_000_063,
    1_000_000_000_091,
    1_000_000_000_121,
    ]

    # CODE A COMPLETER
    with Pool() as p:
        p.map(f, numbers)


if __name__ == "__main__":
    start = time.perf_counter()
    run()
    print(f"Durée : {time.perf_counter() - start:.2f} s")
