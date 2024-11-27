# useful for data processing and analysis

# pandas data frame is 2D tabular data structure with labeled axis(rows,columns)

import pandas as pd 

# creating pandas dataframe
# importing california housing
from sklearn.datasets import fetch_california_housing
california_dataset = fetch_california_housing()
# print(type(california_dataset))
# print(california_dataset)

# pandas dataframe
california_df = pd.DataFrame(california_dataset.data, columns=california_dataset.feature_names)

# print(california_df.head()) #print first five rows
# print(california_df) #print all rows

print(california_df.shape)


# importing data from csv 
diabetes_df = pd.read_csv(r"C:\Users\HP\Downloads\machine learning notes\Machine_Learning-notes-\machine learning notes\Datasets\diabetes.csv")
print(type(diabetes_df))
print(diabetes_df.shape)
print(diabetes_df.head())


# import excel file
# excel = pd.read_excel("path")

# exporting a dataframe to a CSV file
california_df.to_csv('boston_Csv')
diabetes_df.to_excel('diabetes.xlsx')
