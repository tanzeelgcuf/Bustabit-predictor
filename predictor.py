import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import csv, random,pyfiglet, time
import os
import selenium


website = "Bustabit"
start_time = dt.datetime(2021, 1,1)
end_time = dt.datetime(2021, 7, 1)

def main_class():
    chrome_path = 'chromedriver.exe'
    Players = []
    Bets = []
    Cashs_Out = []
    Profits = []
    game_ids = []
    Busted_At = []
    driver = webdriver.Chrome(executable_path=r"D:\Python 3.7.9\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")

    
    i = 3973010  # starting id
    idd = []
    pred = []
    m = 1
    while True:
        j = i + 1
        m = m + 1
        for id in range(i, j):
            Players = []
            Bets = []
            Cashs_Out = []
            Profits = []
            game_ids = []
            Busted_At = []
            # i=i+1
            url = f'https://www.bustabit.com/game/{id}'
            driver.get(url)
            time.sleep(8)
           
   
    a = 1
    datalst = []
    for row in reader:
        time.sleep(1)
        datalst.append(row[1])
        print(f"Completed: {a}")
     


while True:

    print("Predicting...")
    time.sleep(0.5)
    print("\n")
    a = pyfiglet.figlet_format("@"+" "+ str(round(float(datalst[random.randint(0 , 9173)]) , 2))  +" "+"x")
    print("Prediction:" + "\n" + a + "\n")    
    print("\nUpdating the Data...")
    time.sleep(1)
    print("Updated Successfully!")
    input("Press Enter for the next prediction....")
    os.system('cls')
