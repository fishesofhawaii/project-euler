import pandas as pd
from datetime import datetime
import math

n=600851475143
start_time = datetime.now()

def get_problem(): 
    return 3

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def get_factors(num):
    l = []
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            l.append(i)
    print(l)
    return l


def main():
    factors = get_factors(n)
    for i in factors[::-1]:
        if is_prime(i):
            print("ANS:", i)
            return

main()
print()
print("Duration:", datetime.now() - start_time)