# coding: utf-8

# PyCon DE, Darmstadt 2026
# Demystifying Parallel Programming in Python
# Gaël Pegliasco

# run script several times

import time
from concurrent.futures import ThreadPoolExecutor


def f(name):
    for i in range(10):
        print(f"{i} : {name}")
        time.sleep(1)


def run():
    with ThreadPoolExecutor() as executor:
        executor.map(f, ["Alice", "Bob"])

    f("Charly")


if __name__ == "__main__":
    start = time.perf_counter()
    run()
    print(f"Durée : {time.perf_counter() - start:.2f} s")
