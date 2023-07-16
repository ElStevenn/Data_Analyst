import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

path = Path(os.getcwd())
cls = lambda: os.system('cls')
cls()

# Read csv
Laptops_Frame = pd.read_csv(path / 'CSV_Examples/laptops.csv')



"""First of all we are going to review the main methods of pandas"""
Laptops_Frame.shape #How many rows, and how many columns we have

Laptops_Frame.info # Quickly undersdand about the columns we're working with

Laptops_Frame.describe # This is more shorter than .info

Laptops_Frame['Laptop'].mean

Laptops_Frame['Laptop'].median #idk

Laptops_Frame.plot(kind='box', vert=False, figsize=(14, 6))


Laptops_Frame['Model'].value_counts() # group the values by the number there are

Laptops_Frame['Model'].corr # Corralation betweeen some of our propieties

"""Second, we are going to see see some calculations"""

Laptops_simp = Laptops_Frame[['Laptop','Model','Final Price']].rename({'Final Price':'Price'}) # Select necessary columns

Laptops_simp['With Taxes'] = Laptops_simp['Final Price'] * 1.21


(Laptops_Frame['Touch'] != 'No').sum() # How to get how many rows have diferent value

# Laptops_Frame['Final Price'] *= 1.3 # We can increse a value with % with this way, and even if we want te decrese the values, we'd use '*= 0.8' for example


"""Quick filtring"""

# For example we want to show the values that column called 'Touch' is equals to 'Yes'
Laptops_1300 = Laptops_Frame.loc[Laptops_Frame['Touch'] == 'Yes']

# .loc Access a group of rows and columns by supplying label(s) arguments.

# Another larger example using "and", (here is used '&' insead of 'AND' operator)

Good_Laptops =  Laptops_Frame.loc[(Laptops_Frame['RAM'] >= 8) & (Laptops_Frame['Touch'] == 'Yes')][['Laptop','RAM','Final Price']]


# Now,  example usind 'or', remember that here we use '|'







