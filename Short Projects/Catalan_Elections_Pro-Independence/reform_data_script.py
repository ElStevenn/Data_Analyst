import numpy as np
import pandas as pd
import os


    

def main():
    RLleida = pd.read_csv(os.getcwd() + "/csv_data/lleida_data.csv", encoding="utf-8")
    RBarcelona = pd.read_csv(os.getcwd() + "/csv_data/barcelona_data.csv", encoding="utf-8")
    RGirona = pd.read_csv(os.getcwd() + "/csv_data/girona_data.csv", encoding="utf-8")
    RTarragona = pd.read_csv(os.getcwd() + "/csv_data/tarragona_data.csv", encoding="utf-8")

    MyNew_dataFrame = pd.concat((RLleida, RBarcelona, RGirona, RTarragona))
    print(MyNew_dataFrame)

    MyNew_dataFrame.to_csv(os.getcwd() + '/csv_data/Town_Data.csv', encoding='utf-8')


if __name__ == '__main__':
    main()

