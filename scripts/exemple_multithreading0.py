# coding: utf-8

# PyCon DE, Darmstadt 2026
# Demystifying Parallel Programming in Python
# Gaël Pegliasco

# 1. run script several times
# 2. run script and interrupt with Ctrl-C
# 3. comment time.sleep(1) and run script several times

import time
from threading import Thread as Task


def f(name):
    for i in range(10):
        print(f"{i} : {name}")
        time.sleep(1)


def run():
    t1 = Task(target=f, args=("Alice",))
    t2 = Task(target=f, args=("Bob",))

    # start tasks
    t1.start()
    t2.start()

    # main script
    f("Charly\n")

    # wait tasks to be finished
    t1.join()
    t2.join()

    # end of script
    print('The end')


if __name__ == "__main__":
    start = time.perf_counter()
    run()
    print(f"Durée : {time.perf_counter() - start:.2f} s")
