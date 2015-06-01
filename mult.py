#!/usr/bin/python

import sys
import time
import random

NUM_MULT = 10
MAX_MULT = 10

def main(argv):
    table_selected = False
    while not table_selected:
        print('Which times table do you want to practice (1-{}, empty for all)? >> '.format(MAX_MULT), end='', flush=True)
        table = sys.stdin.readline()
        if table == '\n':
            table = 0
            table_selected = True
        else:
            try:
                table = int(table)
            except ValueError:
                pass
            else:
                if table > 0 and table <= MAX_MULT:
                    table_selected = True

    correct_answers = 0
    start_time = time.time()
    for i in range(0, NUM_MULT):
        multiplicand = random.randint(2, MAX_MULT)
        if table == 0:
            multiplier = random.randint(2, MAX_MULT)
        else:
            multiplier = table
        print('{: >-2d} x {} = '.format(multiplicand, multiplier), end='', flush=True)
        try:
            product = int(sys.stdin.readline())
        except ValueError:
            pass
        else:
            if product == multiplicand * multiplier:
                print("Juste\n")
                correct_answers += 1
            else:
                print("Faux\n")
    end_time = time.time()
    total_time = end_time - start_time
    print("You needed {:.2f} seconds with a grade of {}/{}.".format(total_time, correct_answers, NUM_MULT))

if __name__ == "__main__":
    main(sys.argv[1:])
