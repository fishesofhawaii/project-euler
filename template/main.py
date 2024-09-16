import pandas as pd
import math

def get_problem(): 
    return 1

def main(): 
    # Data
    df = pd.read_csv('input.csv')
    
    # Syntax
    header_list = list(df)
    row_count = len(df)

    print(df)
    

main()