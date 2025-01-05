import os

# Pandas for reading file and cleaning data
import pandas as pd

#Getting the current working directory
os.getcwd()

#Changing the directory
os.chdir("C://Users//Pooja//Dataset")

# Reading a csv file
Admit =pd.read_csv("admit.csv")
