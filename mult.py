#!/usr/bin/python

import sys
import time
import random

NUM_MULT = 10

def main(argv):
    table_selected = False
    while not table_selected:
        print('Quelle table veux-tu pratiquer? (2-10) >> ', end='', flush=True)
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
                if table >= 2 and table <= 10:
                    table_selected = True

    correct_answers = 0
    start_time = time.time()
    for i in range(0, NUM_MULT):
        multiplicand = random.randint(2, 10)
        if table == 0:
            multiplier = random.randint(2, 10)
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
    print("Tu as pris {:.2f} secondes et as une note de {}/{}.".format(total_time, correct_answers, NUM_MULT))

if __name__ == "__main__":
    main(sys.argv[1:])
