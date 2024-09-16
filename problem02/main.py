import pandas as pd
import math

# This got out of hand quickly -- not the way I wanted to write this
MAX_VAL = 4000000

def get_problem(): 
    return 2

def does_meet_criteria(num): 
    if num % 2 == 1:
        return False
    elif num < MAX_VAL:
        return True
    else:
        return False

def get_next_fib(a):
    if len(a) < 2:
        return
    
    return a[-1] + a[-2]

def main(): 
    seed = [1, 2]
    even_sum = 2
    while seed[-1] < MAX_VAL:
        next_fib = get_next_fib(seed)
        seed.append(next_fib)
        
        if does_meet_criteria(next_fib):
            even_sum += next_fib
        
    print(even_sum)    


main()
