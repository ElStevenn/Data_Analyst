from extract_data import  extract_party_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import tqdm

cls = lambda: os.system('cls')
cls()

def get_all_data():
    Barcelona = extract_party_data("barcelona", print_values=False)
    MyDataFrame = pd.DataFrame(Barcelona.Data_Dic)

    print(MyDataFrame)

    return Barcelona

if __name__ == "__main__":
    bcn = get_all_data()
    print(bcn)