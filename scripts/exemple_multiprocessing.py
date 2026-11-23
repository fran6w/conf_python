# coding: utf-8

# run script several times

import time
from multiprocessing import Pool


def f(name):
    for i in range(10):
        print(f"{i} : {name}")
        time.sleep(1)


def run():
    with Pool() as p:
        p.map(f, ["Alice", "Bob"])

    f("Charly")
    print('Fin')


if __name__ == "__main__":
    start = time.perf_counter()
    run()
    print(f"Durée : {time.perf_counter() - start:.2f} s")
