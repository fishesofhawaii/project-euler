import pandas as pd
import math

def get_problem(): 
    return 1

def get_sum_from_max(m):
    rolling_sum = 0

    for i in range(0, m):
        if i % 3 == 0:
            # add it to the sum
            rolling_sum += i
        elif i % 5 == 0:
            # add it to the sum
            rolling_sum += i

    return rolling_sum

def main(): 
    print("Problem01's answer:", get_sum_from_max(1000))

main()