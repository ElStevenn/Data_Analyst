from extract_data import  extract_party_data
from graphic_design import Elections_grafic_design
import numpy as np
import pandas as pd
import os

cls = lambda: os.system('cls')
cls()

def get_all_data():
    #Barcelona = extract_party_data("barcelona", print_values=False)
    Lleida = extract_party_data("barcelona", print_values=False)
    #Girona = extract_party_data("girona", print_values=False)
    #Tarragona = extract_party_data("tarragona", print_values=False)
    
    return Lleida.Data_Dic

def votes_to_numpy(votes):
    Main_Array = None

    for town in votes:
        Array_with = np.array([town['PSC'], town['PP'], town['VOX'], town['Cs'], town['ERC'], town['ECP'], town['JxCat'], town['CUP']])
        Main_Array = Array_with if Main_Array is None else np.vstack((Main_Array, Array_with))

    return Main_Array

def calculate_percentage(num1, num2):
    """Calc percentage of two numbers"""
    total = num1 + num2
    percentage1 = (num1 / total) * 100
    percentage2 = (num2 / total) * 100
    return np.round(percentage1, 2), np.round(percentage2, 2)

def percentage_indep(votes_array):
    """
    Calculate the percentage betweeen independence parties and not and introduce inside a single array.
    Return: left number is pro-independencte whereas right number is no-independence.
    """
    Array_with_percentage = None
    for vote in votes_array:

        # Convert elements to integers
        vote = vote.astype(int)

        # Sum All Independence parties and none independence parties
        indep_parties = np.sum(vote[4:])
        no_indep_parties = np.sum(vote[:4])

        # Function to calc percentage between independentist parties or none independentist parties
        Perc_Yes, Perc_No = calculate_percentage(indep_parties, no_indep_parties)
        Together = np.array([Perc_Yes, Perc_No])

        # Add this data in general array
        Array_with_percentage = Together if Array_with_percentage is None else np.vstack((Array_with_percentage, Together))
    
    return Array_with_percentage        

def sum_all_votes(Votes):
    Array_sum_all_votes = None
    for town in Votes:

        town_numeric = town.astype(np.int32) 
        All_Votes = np.sum(town_numeric)
        Array_sum_all_votes = All_Votes if Array_sum_all_votes is None else np.vstack((Array_sum_all_votes, All_Votes))

    return Array_sum_all_votes
        


def main():
    
    Votes = votes_to_numpy(get_all_data())
    Total_Votes = sum_all_votes(Votes) 
    Percentage = percentage_indep(Votes)
    
    print(Votes)
 
    
    Grpahic = Elections_grafic_design(Percentage, Total_Votes)
    Grpahic.build_scatter()






if __name__ == "__main__":
    main()
    