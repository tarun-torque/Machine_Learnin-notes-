# seaborn basics
# data should be in pandas data frame
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#<==== circular import ===>

# seaborn has some in-built data set 
tips = sns.load_dataset('tips')
# print(tips.head())

# sns.set_theme()  => to set the theme

# visualize the tip data frame
# sns.relplot(data=tips,x='total_bill', y='tip', col='time', hue='smoker',style='smoker',size='size')
# plt.show()

# iris= sns.load_dataset('iris')
# print(iris.columns)


# sns.scatterplot(data=iris,x='sepal_length',y='petal_length',hue='species')
# plt.show()



# loading titanic dataset
titanic = sns.load_dataset('titanic')
# print(titanic.head())

# sns.countplot(data=titanic,x='class')
# plt.show()


# Bar chart
# sns.barplot(data=titanic,x='sex',y='survived',hue='who')
# plt.show()



