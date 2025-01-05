import os
# Pandas for reading file and cleaning data
import pandas as pd
#Getting the current working directory
os.getcwd()
#Changing the directory
os.chdir("C://Users//Pooja//Dataset")
# Reading a csv file
Admit =pd.read_csv("admit.csv")
# To see first 5 rows 
Admit.head()
#To see the last 5 rows
Admit.tail()
# To display only two rows
pd.set_option('display.max_rows',2)
Admit
