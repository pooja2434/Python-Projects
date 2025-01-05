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
# To display only two columns
pd.set_option('display.max_columns',2)
Admit

#To see how many row and columns
Admit.shape

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)

# Describing the dataset
Admit.describe()

# To list the columns
Admit.columns

# To find the mean of a column
Admit['GRE'].mean()
# Standard Deviation
Admit['GRE'].std()
# Count
Admit['GRE'].count()
#Finding the minimum value 
Admit['GRE'].min()
#Finding the maximum value 
Admit['GRE'].max()
# First Quantile
Admit['GRE'].quantile(0.25)
# Second Quantile
Admit['GRE'].quantile(0.50)
# Third Quantile
Admit['GRE'].quantile(0.75)
# Range
dis_range=Admit['GRE'].max() - Admit['GRE'].min()
dis_range
