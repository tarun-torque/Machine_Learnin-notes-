# useful for data processing and analysis

# pandas data frame is 2D tabular data structure with labeled axis(rows,columns)

import pandas as pd 
import numpy as np

# creating pandas dataframe
# importing california housing
# from sklearn.datasets import fetch_california_housing
# california_dataset = fetch_california_housing()
# print(type(california_dataset))
# print(california_dataset)

# pandas dataframe
# california_df = pd.DataFrame(california_dataset.data, columns=california_dataset.feature_names)

# print(california_df.head()) #print first five rows
# print(california_df) #print all rows

# print(california_df.shape)


# importing data from csv 
diabetes_df = pd.read_csv(r"C:\Users\HP\Downloads\machine learning notes\Machine_Learning-notes-\machine learning notes\Datasets\diabetes.csv")
# print(type(diabetes_df))
# print(diabetes_df.shape)
# print(diabetes_df.head())


# import excel file
# excel = pd.read_excel("path")

# exporting a dataframe to a CSV file
# california_df.to_csv('boston_Csv')
# diabetes_df.to_excel('diabetes.xlsx')

# create dataframe with random value
randomDf = pd.DataFrame(np.random.randint(10,20,(20,10)))
# print(randomDf.head())

# inspecting a DataFrame
# print(randomDf.shape)
# last five rows of data frame
# print(randomDf.tail())
# print(randomDf.info())

# finding number of missing values on each columns
# print(randomDf.isnull().sum())


#  counting the values based on labels
# print(diabetes_df.value_counts('Outcome'))
print(diabetes_df.value_counts('Pregnancies'))

# print(diabetes_df.groupby('Outcome').mean())


# statistical measures
# print(diabetes_df.count())  #gives number of values in each columns

# mean value column wise
# print(diabetes_df.mean())


#standard deviation column wise
# print(diabetes_df.std())

# minimum value in each column
# print(diabetes_df.min())
# print(diabetes_df.max())

# all the statical measures about the dataframe
print(diabetes_df.describe())

# manipulating a dataframe
# adding a column to the dataframe
